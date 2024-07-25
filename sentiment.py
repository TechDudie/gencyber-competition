import colorama
import requests
import sys

def get_sentiment(text, api_key):
    r = requests.post("https://api.meaningcloud.com/sentiment-2.1", data={
        "key": api_key,
        "lang": "en",
        "model": "general",
        "txt": text
    })

    result =  r.json()["score_tag"]

    if result == "P+":
        return colorama.Fore.LIGHTGREEN_EX, "STRONG POSITIVE"
    elif result == "P":
        return colorama.Fore.GREEN, "POSITIVE"
    elif result == "NEU":
        return colorama.Fore.YELLOW, "NEUTRAL"
    elif result == "N":
        return colorama.Fore.RED, "NEGATIVE"
    elif result == "N+":
        return colorama.Fore.LIGHTRED_EX, "STRONG NEGATIVE"
    elif result == "NONE":
        return colorama.Fore.WHITE, "NO SENTIMENT"

if __name__ == "__main__":
    text = input("Enter some text: ")
    color, text = get_sentiment(text)
    print("=" * 10)
    print(color + text + colorama.Style.RESET_ALL)
    print("=" * 10)