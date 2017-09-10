import RPi.GPIO as GPIO
import time

out1 = 38
out2 = 40

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(out1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(out2, GPIO.OUT, initial=GPIO.LOW)

def sendGreen():
    GPIO.output(out1, GPIO.HIGH)
    GPIO.output(out2, GPIO.HIGH)

def sendYellow():
    GPIO.output(out1, GPIO.LOW)
    GPIO.output(out2, GPIO.LOW)

def sendRed():
    GPIO.output(out1, GPIO.HIGH)
    GPIO.output(out2, GPIO.LOW)

def close():
    GPIO.cleanup(out1);
    GPIO.cleanup(out2);
