import colorama
import requests
import sys

with open("/home/pi/.env" if sys.argv[1] != "dev" else "/home/codespace/.env") as f:
    API_KEY = f.read().split("\n")[1].split("=")[1].strip()
    print(API_KEY)

def get_sentiment(text):
    r = requests.post("https://api.meaningcloud.com/sentiment-2.1", data={
        "key": API_KEY,
        "lang": "en",
        "model": "general",
        "txt": text
    })

    result =  r.json()["score_tag"]

    match result:
        case "P+":
            return colorama.Fore.LIGHTGREEN_EX, "STRONG POSITIVE"
        case "P":
            return colorama.Fore.GREEN, "POSITIVE"
        case "NEU":
            return colorama.Fore.YELLOW, "NEUTRAL"
        case "N":
            return colorama.Fore.RED, "NEGATIVE"
        case "N+":
            return colorama.Fore.LIGHTRED_EX, "STRONG NEGATIVE"
        case "NONE":
            return colorama.Fore.WHITE, "NO SENTIMENT"

if __name__ == "__main__":
    text = input("Enter some text: ")
    color, text = get_sentiment(text)
    print("=" * 10)
    print(color + text + colorama.Style.RESET_ALL)
    print("=" * 10)