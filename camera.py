from picamera import PiCamera

CAMERA = PiCamera()

if __name__ == "__main__":
    CAMERA.start_preview()