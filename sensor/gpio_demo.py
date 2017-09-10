import RPi.GPIO as GPIO
import time

out1 = 38
out2 = 40

GPIO.setmode(GPIO.BOARD)
# GPIO.setup(40, GPIO.IN)
GPIO.setup(out1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(out2, GPIO.OUT, initial=GPIO.LOW)

while (True):
    print ("HH")
    GPIO.output(out1, GPIO.HIGH)
    GPIO.output(out2, GPIO.HIGH)
    time.sleep(3)
    print ("HL")
    GPIO.output(out1, GPIO.HIGH)
    GPIO.output(out2, GPIO.LOW)
    time.sleep(3)
    print ("LL")
    GPIO.output(out1, GPIO.LOW)
    GPIO.output(out2, GPIO.LOW)
    time.sleep(3)
    print ("LH")
    GPIO.output(out1, GPIO.LOW)
    GPIO.output(out2, GPIO.HIGH)
    time.sleep(3)
