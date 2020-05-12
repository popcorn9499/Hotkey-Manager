import evdev
import time
import asyncio
from EventHandler import EventHandler
from InputHandler import InputHandler
from ProgramHandler import ProgramHandler 
import KeyPressHandler

from evdev.ecodes import *

device = InputHandler("/dev/input/by-path/platform-i8042-serio-0-event-kbd",grabbed=True)
e = evdev.ecodes
uinput = evdev.UInput()



@device.eventHandler(KEY_A)
async def foo(event):
    ProgramHandler("cat /home/popcorn9499/iommuGroups.sh")
    
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_M])
        await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)


@device.eventHandler(KEY_B)
async def bar(event):
    print("This is bar's first handler")
    print(evdev.categorize(event))



asyncio.get_event_loop().run_forever()