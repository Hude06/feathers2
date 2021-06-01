
ambient light sensor is at board.i04

example code

``` python
import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
 
pin = AnalogIn(board.IO4)
 
def get_voltage(pin):
	return (pin.value * 3.3) / 65536
 
while True:
    print(get_voltage(pin))
    #print(pin.value)
    time.sleep(1)# Write your code here :-)
```

this is is example code for the presure humid sensor for the feather s2

```
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import time
import board
import adafruit_bme280

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# OR create sensor object, using the board's default SPI bus.
# spi = board.SPI()
# bme_cs = digitalio.DigitalInOut(board.D10)
# bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    time.sleep(2)
```
