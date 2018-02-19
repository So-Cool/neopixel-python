from __future__ import print_function

import neopixel as npx
import random
import threading
import time

# LED strip configuration:
#LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_PIN        = 12      # Google AIY voice hat -- Servo 4 -- GPIO 12.
LED_COUNT      = 16      # Number of LED pixels.
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = npx.ws.WS2811_STRIP_GRB   # Strip type and colour ordering

# Signals
# https://www.g-loaded.eu/2016/11/24/how-to-terminate-running-python-threads-using-signals/
# https://christopherdavis.me/blog/threading-basics.html

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return npx.Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return npx.Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return npx.Color(0, pos * 3, 255 - pos * 3)

def extract_colour(colour, colour_component):
    if colour_component.lower() == "r":
        return (colour & 0b111111110000000000000000) >> 16
    elif colour_component.lower() == "g":
        return (colour & 0b000000001111111100000000) >> 8
    elif colour_component.lower() == "b":
        return (colour & 0b000000000000000011111111)
    else:
        raise "Unknown colour component"

def extract_colours(colour):
    r = (colour & 0b111111110000000000000000) >> 16
    g = (colour & 0b000000001111111100000000) >> 8
    b = (colour & 0b000000000000000011111111)
    return r, g, b

def colour_shift(colour, divider=1.1):
    r = ((colour & 0b111111110000000000000000) >> 16) / divider
    g = ((colour & 0b000000001111111100000000) >> 8 ) / divider
    b = ((colour & 0b000000000000000011111111)      ) / divider
    if int(r) == 0 or int(g) == 0 or int(b) ==0:
        return 0
    return (int(r)<<16)+(int(g)<<8)+int(b)

def sign(a):
    if a < 0: return -1
    elif a > 0: return 1
    else: return 0

class RingLED(threading.Thread):
    """
    Usage example:
        rr = RingLED(pattern="none")
        rr.start()

        rr.switch_pattern("rainbow")

        rr.switch_pattern("shake")

        rr.switch_pattern("bounce")

        rr.switch_pattern("pulse")

        rr.switch_pattern("still")

        rr.switch_pattern("wave")

        rr.switch_pattern("test")

        rr.switch_pattern("none")

        rr.set_brightness(255)

        rr.set_brightness(100)

        rr.stop()
    """

    def __init__(self, pattern="rainbow", brightness=100, fade=True):
        # Init the thread.
        super(RingLED, self).__init__()
        self.active = threading.Event()

        # Create NeoPixel object with appropriate configuration.
        self.strip = npx.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,
                                      LED_DMA, LED_INVERT, LED_BRIGHTNESS,
                                      LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
        self.LED_number = self.strip.numPixels()
        self.strip.setBrightness(brightness)
        self._dark()

        self.brightness = self.strip.getBrightness()

        # Default pattern
        self.pattern = pattern
        self.previous_pattern = pattern

        # (Almost) infinite loop for displaying colour patterns
        self.colour_loop_break = threading.Event()

        # Rainbow
        self.rainbow_state = 0
        # Shake
        self.shake_state = 1
        self.shake_red = npx.Color(217, 80, 64)
        self.shake_green = npx.Color(88, 165, 92)
        self.shake_blue = npx.Color(79, 134, 237)
        self.shake_yellow = npx.Color(243, 189, 66)
        self.shake_one = 0
        self.shake_two = 4
        self.shake_three = 8
        self.shake_four = 12
        self.shake_pattern = [(self.shake_one, self.shake_red), \
                              (self.shake_two, self.shake_green), \
                              (self.shake_three, self.shake_blue), \
                              (self.shake_four, self.shake_yellow)]
        # Bounce
        self.bounce_state = 0
        self.bounce_bg = npx.Color(0, 0, 0)
        self.bounce_fg = npx.Color(0, 0, 128)
        # Pulse
        self.pulse_colour = npx.Color(128, 0, 128)
        self.pulse_brightness = self.strip.getBrightness()
        # Still
        self.still_colour = npx.Color(0, 128, 128)
        # Wave
        self.wave_origin = {"one":0, "two":8}
        self.wave_state = {"one":0, "two":0}
        self.wave_queue = {"one":[], "two":[]}
        self.wave_colour = {"one": npx.Color(127,0,127), "two":npx.Color(0,127,127)}
        self.wave_colour_current = {"one": 0, "two": 0}
        # Switch
        self.switch_fade = fade
        self.switch_ms_time = 5

    def get_led_id(self, x):
        return x & (self.LED_number - 1)

    def switch_pattern(self, new_pattern):
        self._update_pattern(new_pattern)
        self._update_pattern("switch")
        self.pause()
    def _switch_pattern(self):
        self.restart()
        self._revert_pattern()
        if self.switch_fade:
            for i in range(self.strip.getBrightness()-1, 0-1, -1):
                self.strip.setBrightness(i)
                self.strip.show()
                time.sleep(self.switch_ms_time/1000.0)
        self._dark()
    def _switch_fade_back(self, overwrite=None):
        if self.switch_fade and self.previous_pattern != "brightness":
            max_brightness = self.brightness if overwrite is None else overwrite
            for i in range(0+1, max_brightness+1):
                self.strip.setBrightness(i)
                self.strip.show()
                time.sleep(self.switch_ms_time/1000.0)
        if not self.switch_fade and self.previous_pattern != "brightness":
            self.strip.setBrightness(self.brightness)
    def _update_pattern(self, new_pattern):
        self.previous_pattern = self.pattern
        self.pattern = new_pattern
    def _revert_pattern(self):
        c = self.pattern
        self.pattern = self.previous_pattern
        self.previous_pattern = c

    def set_brightness(self, brightness):
        self.brightness = brightness
        self._update_pattern("brightness")
        self.pause()
    def _set_brightness(self, wait_ms=5):
        def bright_me(current_brightness, target_brightness):
            if target_brightness <= current_brightness:
                return range(current_brightness-1, target_brightness-1, -1)
            else:
                return range(current_brightness+1, target_brightness+1)

        for i in bright_me(self.strip.getBrightness(), self.brightness):
            self.strip.setBrightness(i)
            self.strip.show()
            time.sleep(wait_ms/1000.0)
        self.restart()
        self._revert_pattern()

    def _update_wave(self, part):
        def range_colour(current_range, target_range, colour):
            if target_range - current_range < 0:
                r = range(current_range, target_range-1, -1)
                colour = 0
            else:
                r = range(current_range, target_range+1)
            return r, colour

        if len(self.wave_queue[part]) == 0:
            self.wave_queue[part], self.wave_colour_current[part] = range_colour(self.wave_state[part],
                                                                                 random.randint(0, 3 if part == "one" else 4),
                                                                                 self.wave_colour[part])
        if len(self.wave_queue[part]) != 0:
            self.wave_state[part] = self.wave_queue[part].pop(0)
            self.strip.setPixelColor(self.get_led_id(self.wave_origin[part] + self.wave_state[part]),
                                     self.wave_colour_current[part])
            self.strip.setPixelColor(self.get_led_id(self.wave_origin[part] - self.wave_state[part]),
                                     self.wave_colour_current[part])
            self.strip.show()

    def _dark(self):
        for i in range(self.LED_number):
            self.strip.setPixelColor(i, 0)
        self.strip.show()
    def _none(self, ms_time=1000):
        self._dark()
        self._switch_fade_back()  # Fade back after switch
        while not self.colour_loop_break.is_set():
            time.sleep(ms_time/1000.0)
    def _rainbowCycle(self, wait_ms=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for i in range(self.LED_number):
            self.strip.setPixelColor(i, wheel((int(i * 256 / self.LED_number) + self.rainbow_state) & 255))
        self.strip.show()
        self._switch_fade_back()  # Fade back after switch
        while not self.colour_loop_break.is_set():
            for i in range(self.LED_number):
                self.strip.setPixelColor(i, wheel((int(i * 256 / self.LED_number) + self.rainbow_state) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)
            self.rainbow_state = (self.rainbow_state + 1) & 255
    def _shake_four(self, ms_time=600, shakes_number=5):
        for i, c in self.shake_pattern:
            self.strip.setPixelColor(self.get_led_id(i), c)
            self.strip.setPixelColor(self.get_led_id(i+self.shake_state), c)
            self.strip.setPixelColor(self.get_led_id(i-self.shake_state), 0)
        self.strip.show()
        self._switch_fade_back()  # Fade back after switch
        while not self.colour_loop_break.is_set():
            for _ in range(shakes_number):
                self.shake_state *= -1
                for i, c in self.shake_pattern:
                    self.strip.setPixelColor(self.get_led_id(i), c)
                    self.strip.setPixelColor(self.get_led_id(i+self.shake_state), c)
                    self.strip.setPixelColor(self.get_led_id(i-self.shake_state), 0)
                self.strip.show()
                if self.colour_loop_break.is_set():
                    break
                time.sleep(ms_time/1000.0)
            if not self.colour_loop_break.is_set():
                time.sleep(4*ms_time/1000.0)
    def _bounce(self, ms_time=100):
        for i in range(self.LED_number):
            self.strip.setPixelColor(i, self.bounce_bg)
        px = self.bounce_state % self.LED_number
        if self.bounce_state <= self.LED_number:
            self.strip.setPixelColor(self.get_led_id(px), self.bounce_fg)
        else:
            self.strip.setPixelColor(self.get_led_id(self.LED_number + 1 - px), self.bounce_fg)
        self._switch_fade_back()  # Fade back after switch
        while not self.colour_loop_break.is_set():
            px = self.bounce_state % self.LED_number
            if self.bounce_state <= self.LED_number:
                self.strip.setPixelColor(self.get_led_id(px), self.bounce_fg)
                self.strip.setPixelColor(self.get_led_id(px - 1), self.bounce_bg)
            else:
                self.strip.setPixelColor(self.get_led_id(self.LED_number + 1 - px), self.bounce_fg)
                self.strip.setPixelColor(self.get_led_id(self.LED_number + 2 - px), self.bounce_bg)
            self.strip.show()
            time.sleep(ms_time/1000.0)
            self.bounce_state = (self.bounce_state + 1) % (2 * self.LED_number + 2)
    def _pulse(self, ms_time=20):
        for i in range(self.LED_number):
            self.strip.setPixelColor(i, self.pulse_colour)
        self._switch_fade_back(overwrite=self.pulse_brightness)  # Fade back after switch
        if self.previous_pattern != "brightness":
            for i in range(self.pulse_brightness, self.brightness+1):
                self.pulse_brightness = i
                self.strip.setBrightness(self.pulse_brightness)
                self.strip.show()
                if self.colour_loop_break.is_set():
                    break
                time.sleep((100*ms_time)/(self.brightness+1-self.pulse_brightness)/1000.0)
        #
        axis = range(self.brightness, 0, -1)
        axis += [0] + axis[::-1]
        while not self.colour_loop_break.is_set():
            for i in axis:
                self.pulse_brightness = i
                self.strip.setBrightness(self.pulse_brightness)
                self.strip.show()
                if self.colour_loop_break.is_set():
                    break
                time.sleep((100*ms_time)/int((len(axis)/2))/1000.0)
    def _still(self, ms_time=1000):
        for i in range(self.LED_number):
            self.strip.setPixelColor(i, self.still_colour)
        self._switch_fade_back()  # Fade back after switch
        self.strip.show()
        while not self.colour_loop_break.is_set():
            time.sleep(ms_time/1000.0)
    def _wave(self, slow_down=1):
        # Restore last known state
        for i in ["one", "two"]:
            for j in range (self.wave_state[i]):
                self.strip.setPixelColor(self.get_led_id(self.wave_origin[i] + j), self.wave_colour[i])
                self.strip.setPixelColor(self.get_led_id(self.wave_origin[i] - j), self.wave_colour[i])

            self.strip.setPixelColor(self.get_led_id(self.wave_origin[i] + self.wave_state[i]),
                                     self.wave_colour_current[i])
            self.strip.setPixelColor(self.get_led_id(self.wave_origin[i] - self.wave_state[i]),
                                     self.wave_colour_current[i])

        self._switch_fade_back()  # Fade back after switch
        self.strip.show()

        while not self.colour_loop_break.is_set():
            for i in random.sample(["one", "two"], 2):
                self._update_wave(i)
                time.sleep(random.randint(slow_down*40, slow_down*80)/1000.0)

    def pause(self):
        self.colour_loop_break.set()
    def restart(self):
        self.colour_loop_break.clear()

    def run(self):
        while not self.active.is_set():
            if self.pattern == "brightness":
                self._set_brightness()
            elif self.pattern == "switch":
                self._switch_pattern()
            elif self.pattern == "rainbow":
                self._rainbowCycle()
            elif self.pattern == "shake":
                self._shake_four()
            elif self.pattern == "bounce":
                self._bounce()
            elif self.pattern == "pulse":
                self._pulse()
            elif self.pattern == "still":
                self._still()
            elif self.pattern == "wave":
                self._wave()
            elif self.pattern == "none":
                self._none()
            else:
                print("Unknown pattern {}.".format(self.pattern))
                print("Switching to *rainbow*.")
                self._update_pattern("rainbow")

        self._dark()
    def stop(self):
        self.colour_loop_break.set()
        self.active.set()
