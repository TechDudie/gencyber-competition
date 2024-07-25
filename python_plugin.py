# Jython 2.7; Minecraft 1.16.5

from mcapi import *

import json
import time
import urllib

from org.bukkit.event.player import PlayerJoinEvent

@asynchronous()
def join_event(e):
    while True:
        try:
            data = json.loads(urllib.urlopen("http://localhost:5000/actions"))
        except:
            continue

        for action in data["actions"]:
            if action["id"] == "button":
                yell("Button pressed!")
        
        time.sleep(1)

listener = add_event_listener(PlayerJoinEvent, join_event)