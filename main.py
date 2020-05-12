import evdev
import time
import asyncio
from EventHandler import EventHandler
from InputHandler import InputHandler

from evdev.ecodes import *

device = InputHandler("/dev/input/by-path/platform-i8042-serio-0-event-kbd")


@device.eventHandler.event(KEY_A)
async def foo():
    print("This is foo's first handler")

@device.eventHandler.event(KEY_B)
async def bar():
    print("This is bar's first handler")



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


