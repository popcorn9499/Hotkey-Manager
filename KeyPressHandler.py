import asyncio
import evdev

class KEY_STATE:
    KEY_DOWN = 1
    KEY_UP = 0
    KEY_HOLD = 2
    KEY_TOGGLE = 3 #toggle the key. Unofficial keystate to toggle the key

ECODES = evdev.ecodes
UINPUT = evdev.UInput()

class Key():
    def __init__(self):
        pass

    async def addKey(self,keyCode,keyState):
        UINPUT.write(ECODES.EV_KEY,keyCode,keyState)

    async def sync(self):
        UINPUT.syn()


class KeyPress(Key):
    def __init__(self, keys = []):
        self.keys = keys
        super()

    async def _pressHandler(self,keyState):
        for key in self.keys: #press the required keys
            await self.addKey(key,keyState)
    
    async def keyPress(self,keyState=KEY_STATE.KEY_TOGGLE,pressDuration=0):
        if keyState == KEY_STATE.KEY_TOGGLE:
            await self._pressHandler(KEY_STATE.KEY_DOWN)
            await asyncio.sleep(pressDuration)
            await self.sync()
            await asyncio.sleep(pressDuration)
            await self._pressHandler(KEY_STATE.KEY_UP)
            await self.sync()
        else:
            await self._pressHandler(keyState)
            await asyncio.sleep(pressDuration)
            await self.sync()
