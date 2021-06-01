
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
