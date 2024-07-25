import time
import chatgpt
import camera
import colorama
import sys

_SENTIMENT = True if sys.argv[2] == "sentiment" else False

while True:
    camera.capture()
    text = chatgpt.ask_image("image.jpg")

    print("=" * 80)
    if _SENTIMENT:
        color, sentiment = sentiment.get_sentiment(text)
        print(f"{color}{sentiment}: {text}{colorama.Style.RESET_ALL}")
    else:
        print(text)
    print("=" * 80)
    time.sleep(3)