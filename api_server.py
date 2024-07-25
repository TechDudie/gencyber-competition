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

def button_checker():
    global pressed
    global i
    global action_stack
    
    while True:
        pressed = gpio.get_state()
        print(pressed)

        if pressed:
            i += 1
        
        if not pressed:
            i = 0
        
        if i >= 5:
            action_stack.append('button')
            i = -10000
        
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