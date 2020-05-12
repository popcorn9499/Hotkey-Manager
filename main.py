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



# e = evdev.ecodes
# uinput = evdev.UInput()

# for event in dev.read_loop():
#     if event.type == evdev.ecodes.EV_KEY:
#         print(evdev.categorize(event))
#         print(dirs(event))

# async def keyboardHandler(dev):
#     async for ev in dev.async_read_loop():
#         print(evdev.categorize(ev))
#         print(repr(ev))
#         if ev.type == evdev.ecodes.EV_KEY:
#             print(ev.code == evdev.ecodes.KEY_A)


# asyncio.get_event_loop().run_until_complete(keyboardHandler(dev))



#ui.write(e.EV_KEY,e.KEY_LEFTCTRL,1)
# ui.write(e.EV_KEY,e.KEY_M,1)
# time.sleep(0.1)
# ui.syn()

# time.sleep(0.1)
# ui.write(e.EV_KEY,e.KEY_M,0)
# ui.write(e.EV_KEY,e.KEY_LEFTCTRL,0)

# ui.syn()

# #ui.write(e.EV_KEY,e.KEY_F13,1)
# #ui.write(e.EV_KEY,e.KEY_F13,0)
# #time.sleep(5)
# #ui.syn()


