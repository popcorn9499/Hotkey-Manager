# Hotkey-Manager
Hotkey Manager
Simple tool to use EVDev to wrap a keyboard and map keys to function calls. Has built in functionality to launch commands, send commands to an obs client view obs websockets etc. 


## Dependecies
- Python 3.6+
- evdev
- simpleobsws
- asyncio
- json

## Usage
Run `main.py`

## Examples
`@device.eventHandler(KEY_Q)` Maps a function to a key.

### Example of using the obs websocket in a keypress function
```
@device.eventHandler(KEY_Q) #key you are mapping this to
async def micMuteStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_L]) # any key presses on the system you wish to do
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)
        await obsWS.toggleMute("Mic/Aux")  # where Mic/Aux is the name of the device you wish to mute.
```

### Example of running a program from within a keypress function
```
@device.eventHandler(KEY_F1)
async def musicVolumeDown(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN or event.value == KeyPressHandler.KEY_STATE.KEY_HOLD:
        ProgramHandler("mpc --host 192.168.1.119 volume -1")
```
