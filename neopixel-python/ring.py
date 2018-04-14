from __future__ import print_function

import neopixel as npx
import neopixel_python as npxp
import random
import time

RING_LED_PIN        = 12      # Google AIY voice hat -- Servo 4 -- GPIO 12.
RING_LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
RING_LED_COUNT      = 16      # Number of LED pixels.

# TODO: set upright pixel offset for the ring (just like square rotation

class RingLED(npxp.DriveLED):
    """
    Usage example:
        rr = RingLED(pattern="none")
        rr.start()

        rr.switch_pattern("rainbow")
        rr.switch_pattern("shake")
        rr.switch_pattern("bounce")
        rr.switch_pattern("wave")

        rr.stop()
    """

    def _init_strip(self, led_count, led_pin, led_freq_hz, led_dma, led_invert,
            led_brightness, led_channel, led_strip):
        # Create NeoPixel object with appropriate configuration.
        if led_count is None:
            led_count = RING_LED_COUNT
        if led_pin is None:
            led_pin = RING_LED_PIN
        if led_freq_hz is None:
            led_freq_hz = npxp.LED_FREQ_HZ
        if led_dma is None:
            led_dma = npxp.LED_DMA
        if led_invert is None:
            led_invert = npxp.LED_INVERT
        if led_brightness is None:
            led_brightness = npxp.LED_BRIGHTNESS
        if led_channel is None:
            led_channel = RING_LED_CHANNEL
        if led_strip is None:
            led_strip = npxp.LED_STRIP
        strip = npx.Adafruit_NeoPixel(led_count, led_pin, led_freq_hz,
                                      led_dma, led_invert, led_brightness,
                                      led_channel, led_strip)
        return strip

    # Predefined circular patterns -- necessary inits
    def _init_custom_patterns(self):
        custom_patterns_map = {"rainbow": self._rainbowCycle,
                "shake": self._shake_four, "bounce": self._bounce,
                "wave": self._wave}
        self.pattern_map.update(custom_patterns_map)

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
        # Wave
        self.wave_origin = {"one":0, "two":8}
        self.wave_state = {"one":0, "two":0}
        self.wave_queue = {"one":[], "two":[]}
        self.wave_colour = {"one": npx.Color(127,0,127), "two":npx.Color(0,127,127)}
        self.wave_colour_current = {"one": 0, "two": 0}

    # Predefined circular patterns
    def _rainbowCycle(self, wait_ms=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for i in range(self.LED_number):
            self.strip.setPixelColor(i, npxp.wheel((int(i * 256 / self.LED_number) + self.rainbow_state) & 255))
        self.strip.show()
        self._switch_fade_back()  # Fade back after switch
        while not self.colour_loop_break.is_set():
            for i in range(self.LED_number):
                self.strip.setPixelColor(i, npxp.wheel((int(i * 256 / self.LED_number) + self.rainbow_state) & 255))
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

    # Custom patterns -- helper functions
    def get_led_id(self, x):
        return x & (self.LED_number - 1)

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
