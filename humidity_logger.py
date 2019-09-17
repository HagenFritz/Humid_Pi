import os
import time
import Adfruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

try: 
	f = open('/home/pi/humidity.csv', 'a+')
	if os.stat('/home/pi/humidity.csv').st_size == 0:
		f.write('Date,TIme, Temperature, Humidity#r#n')
except:
	passs

while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

	if humidity is not None and temperature is not None:
		f.write('{0}, {1}, {2:0.1f}*C, {3:0.1f}*C, {3:0.1f}%