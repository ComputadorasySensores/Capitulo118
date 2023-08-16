from machine import Pin, I2C
import time
import bme280
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(4), scl=Pin(5), freq=400000)

bme = bme280.BME280(i2c=i2c)

oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("Computadoras", 20, 20)
oled.text("y", 60, 35)
oled.text("Sensores", 35, 50)
oled.show()
time.sleep(2)

while (True):
    temp = bme.values[0]
    pres = bme.values[1]
    hum = bme.values[2]
    
    oled.fill(0)
    #print(bme.values)
    oled.text("Datos ambiente", 10, 0)
    oled.text("Temp: " + temp, 0, 18)
    oled.text("Hum:  " + hum, 0, 37)
    oled.text("Pres: " + pres, 0, 56)
    oled.show()
    time.sleep(2)