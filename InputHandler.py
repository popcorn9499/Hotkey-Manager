import asyncio
import evdev
from evdev import InputDevice,ecodes
from EventHandler import EventHandler



class InputHandler(): #handles the input from the keyboard. allowing for taking exclusive control of the input device
    def __init__(self,device,grabbed=False):
        self.dev = evdev.InputDevice(device)
        self.eventHandler = EventHandler()
        print("Grabbed: {0}".format(grabbed))
        if grabbed:
            self.dev.grab() #takes exclusive control over the keyboard

    async def init(self):
        asyncio.create_task(self.keyboardHandler()) #starts the keyboad handler loop

    async def keyboardHandler(self): #continuously grabs input from the keyboard. 
        async for ev in self.dev.async_read_loop():
            if ev.type == evdev.ecodes.EV_KEY: #specifys only keyboard input
                print(evdev.categorize(ev)) #prints debug info on which key was pressed and how it was pressed
                await self.eventHandler.call(ev.code,ev) #sends keyboard event