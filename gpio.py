import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

def on():
    GPIO.output(4, GPIO.HIGH)
    print("LED on")

def off():
    GPIO.output(4, GPIO.LOW)
    print("LED off")

def get_state():
    return GPIO.input(17)
    return 1