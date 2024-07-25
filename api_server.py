from flask import Flask, request
import threading
import time

import gpio

global pressed
pressed = False
i = 0
j = 0

global action_stack
action_stack = []

def button_checker():
    global pressed
    global action_stack
    pressed = gpio.get_state()
    time.sleep(0.05)

    if pressed:
        i += 1
        j -= 1
    
    if not pressed:
        j += 1
    
    if j > 10:
        i = 0
    
    if i > 10:
        action_stack.append('button')

app = Flask(__name__)

@app.route('/actions', methods=['GET'])
def actions():
    global action_stack
    e = action_stack
    action_stack = []
    return str(e)

@app.route('/authenticate', methods=['POST'])
def authenicate():
    # Handle POST request on /authenticate
    data = request.get_json()
    # Perform authentication logic here
    return 'Handling POST request on /authenticate'

if __name__ == '__main__':
    gpio_thread = threading.Thread(target=button_checker)
    app.run()