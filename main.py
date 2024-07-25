import time

import chatgpt
import camera

while True:
    camera.capture()
    text = chatgpt.ask_image("image.jpg")
    print("=" * 80)
    print(text)
    print("=" * 80)
    time.sleep(3)