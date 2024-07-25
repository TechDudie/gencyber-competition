from picamera2 import Picamera2
from time import sleep

CAMERA = Picamera2()

def capture():
    CAMERA.start_and_capture_file("image.jpg")

if __name__ == "__main__":
    CAMERA.start_and_capture_file("capture.jpg")