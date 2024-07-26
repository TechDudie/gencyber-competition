import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

def on():
    GPIO.output(4, GPIO.HIGH)
    print("LED on")

def off():
    GPIO.output(4, GPIO.LOW)
    print("LED off")

def tell():
    GPIO.output(3, GPIO.HIGH)

def get_state():
    return GPIO.input(17)