from picamera import PiCamera
from time import sleep

CAMERA = PiCamera()

def capture():
    CAMERA.capture("capture.jpg")

if __name__ == "__main__":
    CAMERA.capture("capture.jpg")