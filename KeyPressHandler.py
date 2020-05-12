import asyncio
import evdev

class KEY_STATE:
    KEY_DOWN = 1
    KEY_UP = 0
    KEY_HOLD = 2
    KEY_TOGGLE = 3 #toggle the key. Unofficial keystate to toggle the key

ECODES = evdev.ecodes
UINPUT = evdev.UInput()

class key():
    def __init__(self):
        pass

    async def addKey(self,keyCode,keyState):
        UINPUT.write(ECODES.EV_KEY,keyCode,keyState)

    async def sync(self):
        UINPUT.syn()


class keyPress():
    def __init__(self, keys = []):
        self.keys = keys

    async def _pressHandler(self,keyState):
        for key in self.keys: #press the required keys
            await super.addKey(key,KEY_STATE.KEY_TOGGLE)
    
    async def keyPress(self,keyState=KEY_STATE.KEY_TOGGLE,pressDuration=0):
        if keyState == KEY_STATE.KEY_TOGGLE:
            await self._pressHandler(KEY_STATE.KEY_DOWN)
            await asyncio.sleep(pressDuration)
            await super.sync()
            await asyncio.sleep(pressDuration)
            await self._pressHandler(KEY_STATE.KEY_UP)
        else:
            await self._pressHandler(keyState)