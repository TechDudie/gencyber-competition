from flask import Flask, request
import threading
import time

import gpio

global pressed
pressed = False
i = 0

global action_stack
action_stack = []

def button_checker():
    global pressed
    global action_stack
    pressed = gpio.get_state()

    if pressed:
        i += 1
    
    if not pressed:
        i = 0
    
    if i >= 5:
        action_stack.append('button')
    
    time.sleep(0.05)

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
    gpio_thread.start()
    app.run()