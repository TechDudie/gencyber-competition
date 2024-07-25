import time

import chatgpt
import camera

while True:
    camera.capture()
    text = chatgpt.ask_image("image.jpg")
    print(text)
    time.sleep(10)