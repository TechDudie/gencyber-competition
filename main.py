import argparse
import camera
import chatgpt
import colorama
import sentiment
import time
import tts

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--dev", help="Development mode", action="store_true")
    parser.add_argument("-s", "--sentiment", help="Sentiment analysis", action="store_true")
    parser.add_argument("-t", "--tts", help="Text to Speech on analyzed image", action="store_true")

    args = parser.parse_args()

    with open("/home/codespace/.env" if args.dev else "/home/pi/.env") as f:
        OPENAI_API_KEY = f.read().split("\n")[0].split("=")[1].strip()
        SENTIMENT_API_KEY = f.read().split("\n")[1].split("=")[1].strip()

    while True:
        camera.capture()
        text = chatgpt.ask_image("image.jpg", OPENAI_API_KEY)

        print("=" * 80)
        if args.sentiment:
            color, sent = sentiment.get_sentiment(text, SENTIMENT_API_KEY)
            print(f"{color}{sent}: {text}{colorama.Style.RESET_ALL}")
            tts.speak(sent)
        else:
            print(text)
        
        if args.tts:
            time.sleep(0.5)
            tts.speak(text)
        
        print("=" * 80)
        time.sleep(7 if args.sentiment else 3)