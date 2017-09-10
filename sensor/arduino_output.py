from Arduino import Arduino
import time

pin = 6
board = Arduino('9600') #plugged in via USB, serial com at rate 9600
board.pinMode(pin, "OUTPUT")

while True:
    board.digitalWrite(pin, "LOW")
    time.sleep(1)
    print("low")
    board.digitalWrite(pin, "HIGH")
    time.sleep(1)
    print("high")