from picamera import PiCamera
from time import sleep

CAMERA = PiCamera()

if __name__ == "__main__":
    CAMERA.start_preview()
    sleep(60)
    CAMERA.stop_preview()