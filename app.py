import Adafruit_DHT
import requests
import time
from requests import exceptions

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 3
host = 'http://server-ip/input'
app_key = "Wd8TrB3G36gf7pf"

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    raspberry_time = time.strftime("%Y-%m-%d %H:%M:%S")

    if humidity is not None and temperature is not None:
        try:
            r = requests.post(host, json={"temp": str(round(temperature, 1)), "rh": str(
                round(humidity, 1)), "time": str(raspberry_time), "key": str(app_key)})
            print(r.json()["msg"])
            time.sleep(10)
        except requests.exceptions.RequestException as e:
            time.sleep(10)
    else:
        try:
            r = requests.post(host, json={
                "temp": "-", "rh": "-", "time": str(raspberry_time), "key": str(app_key)})
            print(r.json()["msg"])
        except requests.exceptions.RequestException as e:
            time.sleep(10)
