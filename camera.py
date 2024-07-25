from picamera import PiCamera
from time import sleep

CAMERA = PiCamera()

def capture():
    CAMERA.start_and_capture_file("image.jpg")

if __name__ == "__main__":
    CAMERA.start_and_capture_file("capture.jpg")