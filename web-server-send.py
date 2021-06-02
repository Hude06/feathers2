import board
import busio
from digitalio import DigitalInOut
import feathers2
import wifi
import socketpool
import adafruit_requests
import ssl


try:
    from secrets import secrets
except ImportError:
    print("secrets are missing")
    raise
print("it works YAY")

#help(board)

TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"

try:
    wifi.radio.connect("SSID","YOUR PASCODE")
except Exeception as e:
    print("error trying to connect" + str(e))
    exit(1)
    
print("were are connected???")

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

print("we setup the pool")

response = requests.get("http://10.0.0.51:3000/")
print("got a response")
data = response.json()
print("raw data is",data)
print("got data. state is",data["jude"])
print("age is",data["age"])

data["age"] = 11
print("sending out some new data", data)

response = requests.post("http://10.0.0.51:3000/",json=data)

print("data was sent")
print("-" *40)
print("the new response is",response.text)

