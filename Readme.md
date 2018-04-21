# NeoPixel Python #
A thread-based Python library to control WS281X LEDs (AdaFruit's NeoPixels).

## Requirements ##
This library requires [`rpi_ws281x`](https://github.com/jgarff/rpi_ws281x) and its corresponding [Python library](https://github.com/jgarff/rpi_ws281x/tree/master/python). Detailed installation instructions are available on [AdaFruit's website](https://learn.adafruit.com/neopixels-on-raspberry-pi/software).

If you want to install the `rpi_ws281x` library:
```
# Update OS packages
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig

# Install WS281X driver...
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons

# ...and the corresponding Python package
cd python
sudo python setup.py install
```
