from flask import Flask, request, Response
import hashlib
import threading
import time
import gpio

import camera
import chatgpt
import colorama
import sentiment
import time
import tts

global pressed
global i
global action_stack
global door

pressed = False
i = 0
action_stack = []
door = False

load = lambda file: open(file).read()

with open("/home/pi/.env") as f:
    e = f.read().split("\n")
    OPENAI_API_KEY = e[0].split("=")[1].strip()
    SENTIMENT_API_KEY =e[1].split("=")[1].strip()

def button_listener():
    global pressed
    global i
    global action_stack

    while True:
        pressed = not bool(gpio.get_state())

        if pressed:
            i += 1
        
        if not pressed:
            i = 0
        
        if i >= 5:
            action_stack.append({"id": "button"})
            i = -10000
        
        time.sleep(0.05)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return load("index.html")

@app.route('/dashboard.html', methods=['POST'])
def dashboard():
    username = request.form.get('username')
    password = request.form.get('password')

    hash = hashlib.sha256(password.encode('utf-8')).hexdigest() == load("hash.txt").strip()
    if username == "admin" and hash:
        html = load("dashboard.html")
        return html
    else:
        return load("index.html")

@app.route('/open_door', methods=['GET'])
def open_door():
    global door
    door = True
    html = load("dashboard.html")
    return html

@app.route('/close_door', methods=['GET'])
def close_door():
    global door
    door = False
    html = load("dashboard.html")
    return html

@app.route('/actions', methods=['GET'])
def actions():
    global action_stack
    e = action_stack
    action_stack = []
    return str({"actions": e})

@app.route('/led_on', methods=['GET'])
def led_on():
    gpio.on()
    print("on")
    return "on"

@app.route('/led_off', methods=['GET'])
def led_off():
    gpio.off()
    print("off")
    return "off"

@app.route('/camera', methods=['GET'])
def cammy():
    camera.capture()
    text = chatgpt.ask_image("image.jpg", OPENAI_API_KEY)
    print("=" * 80)
    color, sent = sentiment.get_sentiment(text, SENTIMENT_API_KEY)
    print(f"{color}{sent}: {text}{colorama.Style.RESET_ALL}")
    tts.speak("sentiment" + sent)
    time.sleep(0.5)
    tts.speak(text)
    print("=" * 80)
    return text

@app.route('/check_door', methods=['GET'])
def check_door():
    global door
    print(door)
    return Response("open", status=200) if door else Response("closed", status=500)

if __name__ == '__main__':
    gpio_thread = threading.Thread(target=button_listener)
    gpio_thread.start()
    app.run(host="0.0.0.0", port=80)