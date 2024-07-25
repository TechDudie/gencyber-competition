from flask import Flask, request
import threading
import time

import gpio

global pressed
global i
global action_stack

pressed = False
i = 0
action_stack = []

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

@app.route('/actions', methods=['GET'])
def actions():
    global action_stack
    e = action_stack
    action_stack = []
    return str({"actions": e})

@app.route('/authenticate', methods=['POST'])
def authenicate():
    data = request.get_json()
    return str({"response": "authenicated"})

if __name__ == '__main__':
    gpio_thread = threading.Thread(target=button_listener)
    gpio_thread.start()
    app.run()