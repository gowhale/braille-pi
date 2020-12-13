import RPi.GPIO as GPIO
import time

channel = 21
TIME_BETWEEN_READINGS = 0.1


GPIO.setmode(GPIO.BCM)
# Setup your channel
GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel, GPIO.LOW)

GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.HIGH)


for i in range(1000):
    time.sleep(TIME_BETWEEN_READINGS)
    if GPIO.input(channel):
        print("{} Pin {} is HIGH".format(i, channel))
    else:
        print(i, "Low")


print("Reading temp")
