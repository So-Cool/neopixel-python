from __future__ import print_function

import atexit
import neopixel as npx
import threading
import time

# LED strip configuration:
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_COUNT      = 16      # Number of LED pixels.
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = npx.ws.WS2811_STRIP_GRB   # Strip type and colour ordering

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

class DriveLED(threading.Thread):
    """
    Usage example:
        rr = DriveLED(pattern="none")
        rr.start()

        rr.switch_pattern("pulse")
        rr.switch_pattern("still")
        rr.switch_pattern("none")
        rr.switch_pattern("test")

        rr.set_brightness(255)
        rr.set_brightness(100)

        rr.stop()
    """

    def __init__(self, pattern="pulse", brightness=100, fade=True,
            led_count=None, led_pin=None, led_freq_hz=None, led_dma=None,
            led_invert=None, led_brightness=None, led_channel=None,
            led_strip=None):

        # Init the thread.
        super(DriveLED, self).__init__()
        self.active = threading.Event()
        self.daemon = True

        # Init the strip
        self.strip = self._init_strip(led_count, led_pin, led_freq_hz, led_dma,
                led_invert, led_brightness, led_channel, led_strip)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()
        # Remove neopixel built in exit handler and execute it manually on thread stop (__init__.py)
        atx = atexit._exithandlers[:]
        for a in atx:
            try:
                if isinstance(a[0].im_self, npx.Adafruit_NeoPixel):
                    atexit._exithandlers.remove(a)
            except AttributeError:
                pass

        # Init pattern changer
        self.pattern_map = {"brightness": self._set_brightness, "switch": self._switch_pattern}

        self.LED_number = self.strip.numPixels()
        self.strip.setBrightness(brightness)
        self._dark()

        self.brightness = self.strip.getBrightness()

        # Default pattern
        self.pattern = pattern
        self.previous_pattern = pattern

        # To fade, or not to fade
        self.switch_fade = fade

        # (Almost) infinite loop for displaying colour patterns
        self.colour_loop_break = threading.Event()

        # Init patterns
        self._init_default_patterns()
        try:
            self._init_custom_patterns()
        except NotImplementedError:
            print("Warning: custom patterns undefined (_init_custom_patterns).")

    def _init_strip(self, led_count, led_pin, led_freq_hz, led_dma, led_invert,
            led_brightness, led_channel, led_strip):
        # Create NeoPixel object with appropriate configuration.
        if led_count is None:
            led_count = LED_COUNT
        if led_pin is None:
            led_pin = LED_PIN
        if led_freq_hz is None:
            led_freq_hz = LED_FREQ_HZ
        if led_dma is None:
            led_dma = LED_DMA
        if led_invert is None:
            led_invert = LED_INVERT
        if led_brightness is None:
            led_brightness = LED_BRIGHTNESS
        if led_channel is None:
            led_channel = LED_CHANNEL
        if led_strip is None:
            led_strip = LED_STRIP
        strip = npx.Adafruit_NeoPixel(led_count, led_pin, led_freq_hz,
                                      led_dma, led_invert, led_brightness,
                                      led_channel, led_strip)
        return strip

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

    def pause(self):
        self.colour_loop_break.set()

    def restart(self):
        self.colour_loop_break.clear()

    def run(self):
        while not self.active.is_set():
            if self.pattern in self.pattern_map:
                self.pattern_map[self.pattern]()
            else:
                print("Unknown pattern {}.".format(self.pattern))
                print("Switching to *pulse*.")
                self._update_pattern("pulse")
    def stop(self):
        self.colour_loop_break.set()
        self.active.set()
        self._dark()
        # Manually call neopixel cleanup method
        self.strip._cleanup()

    # Predefined general patterns -- necessary inits
    def _init_default_patterns(self):
        default_patterns_map = {"pulse": self._pulse, "still": self._still, "none": self._none}
        self.pattern_map.update(default_patterns_map)

        # Pulse
        self.pulse_colour = npx.Color(128, 0, 128)
        self.pulse_brightness = self.strip.getBrightness()
        # Still
        self.still_colour = npx.Color(0, 128, 128)
        # Switch
        self.switch_ms_time = 5

    # Predefined general patterns
    def _dark(self):
        for i in range(self.LED_number):
            self.strip.setPixelColor(i, 0)
        self.strip.show()
    def _none(self, ms_time=1000):
        self._dark()
        self._switch_fade_back()  # Fade back after switch
        while not self.colour_loop_break.is_set():
            time.sleep(ms_time/1000.0)
    def _still(self, ms_time=1000):
        for i in range(self.LED_number):
            self.strip.setPixelColor(i, self.still_colour)
        self._switch_fade_back()  # Fade back after switch
        self.strip.show()
        while not self.colour_loop_break.is_set():
            time.sleep(ms_time/1000.0)
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

    ############################################################################
    def _init_custom_patterns(self):
        raise NotImplementedError
