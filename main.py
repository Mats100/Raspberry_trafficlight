import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.OUT)       # red
GPIO.setup(21, GPIO.OUT)       # yellow
GPIO.setup(22, GPIO.OUT)       # green
while True:
    now = datetime.datetime.now().time()
    if now.hour == 17 and now.minute == 20:
        print("It's ON")
        GPIO.output(20, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.HIGH)
        time.sleep(4)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(22, GPIO.LOW)
        break
    else:
        print("It's Off")
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        break
GPIO.cleanup()
