import base64
import requests
import sys

from openai import OpenAI # why is this here? OpenAI module not used 

def ask_image(image_path, api_key):

    with open(image_path, "rb") as f:
        image = base64.b64encode(f.read()).decode("utf-8")

    response = requests.post("https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }, json={
            "model": "gpt-4o-mini",
            "messages": [
            {
                "role": "user",
                "content": [
                {
                    "type": "text",
                    "text": "What's in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                    "url": f"data:image/jpeg;base64,{image}"
                    }
                }
                ]
            }
            ],
            "max_tokens": 300
        }
    )

    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    image_path = input("Enter the path to your image file: ")
    text = ask_image(image_path)
    print(text)