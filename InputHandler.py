import asyncio
import evdev
from evdev import InputDevice,ecodes
from EventHandler import EventHandler



class InputHandler():
    def __init__(self,device,grabbed=False):
        self.dev = evdev.InputDevice(device)
        self.eventHandler = EventHandler()
        if grabbed:
            self.dev.grab()
        asyncio.get_event_loop().create_task(self.keyboardHandler())

    async def keyboardHandler(self):
        async for ev in self.dev.async_read_loop():
            if ev.type == evdev.ecodes.EV_KEY:
                print(evdev.categorize(ev))
                await self.eventHandler.call(ev.code)