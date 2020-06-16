# NeoPixel Python #
A thread-based Python library to control WS281X LEDs (AdaFruits NeoPixels).

## Installation ##
(Dependencies are installed automatically with this method.)
```
git clone https://github.com/So-Cool/neopixel-python.git
cd neopixel-python
pip install .
```

## Dependencies ##
This library requires [`rpi_ws281x`](https://github.com/jgarff/rpi_ws281x) and its corresponding [Python library](https://github.com/rpi-ws281x/rpi-ws281x-python).
It can be installed either with `pip` (recommended) or manually -- see below.
Detailed installation instructions are available on [AdaFruit's website](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage).

### Dependency Installation via pip ###
```
sudo pip install rpi_ws281x
```

### Manual Dependency Installation ###
If you want to install the `rpi_ws281x` library manually:
```
# Update OS packages
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig

# Install WS281X driver...
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons

# ...and the corresponding Python package
sudo pip install rpi_ws281x
# `cd python && sudo python setup.py install` has been deprecated
```

---

Test with: `rpi_ws281x/python/examples/strandtest.py`.
Adjust `LED_PIN` to 13 or 18 and `LED_CHANNEL` 0 to 1.

## Notes ##
This library is distributed with a file (`neopixel_python/neopixel.py`) adapted from the [`rpi_ws281x` library](https://github.com/jgarff/rpi_ws281x/blob/master/python/neopixel.py).
It is required for the proper functioning of this package but it is not distributed with the pip's version of `rpi_ws281x`, which superseded the Python library distributed as a part of [`rpi_ws281x`](https://github.com/jgarff/rpi_ws281x).

## To Do ##
- [ ] Consider [Unicorn Hat](https://github.com/pimoroni/unicorn-hat) as a Linux service written in C and controlled from Python instead. Also have a look at [Unicorn Paint](https://learn.pimoroni.com/tutorial/unicorn-hat/getting-started-with-unicorn-paint) and [OctaPi](https://projects.raspberrypi.org/en/projects/build-an-octapi)'s use of Unicorn Hat.
