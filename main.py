import evdev
import time
import asyncio
from EventHandler import EventHandler
from InputHandler import InputHandler
from ProgramHandler import ProgramHandler 
import KeyPressHandler
from utils import config
from evdev.ecodes import *
import obsWSHandler


'''
note to anyone using this software. please dont use modifier keys with it 
Ctrl+c and ctrl+z will activate other software as macros a singlq key presses
'''



device = InputHandler("/dev/input/by-path/platform-i8042-serio-0-event-kbd",grabbed=True)
e = evdev.ecodes
uinput = evdev.UInput()

obsWS = obsWSHandler.obsWSHandler("WS_Config.json")

#@device.eventHandler(KEY_A)
#async def foo(event):
    #ProgramHandler("cat /home/popcorn9499/iommuGroups.sh")
    
    #if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        #key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_M])
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)


@device.eventHandler(KEY_Q)
async def micMuteStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_L])
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)
        await obsWS.toggleMute("Mic/Aux")
        
        
@device.eventHandler(KEY_1)
async def gameMuteStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_1])
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEYq_TOGGLE,pressDuration=0.1)
        await obsWS.toggleMute("Desktop Audio")
        await obsWS.toggleMute("Elgato HD 1080P")

@device.eventHandler(KEY_A)
async def discordMuteStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_SEMICOLON])
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)
        await obsWS.toggleMute("Communication Audio")

@device.eventHandler(KEY_Z)
async def musicMuteStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_P])
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)
        await obsWS.toggleMute("Music")

@device.eventHandler(KEY_X)
async def brbSceneStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_SLASH])
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)
        await obsWS.setCurrentScene("Be Right Back")

@device.eventHandler(KEY_S)
async def gameSceneStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_J])
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)
        await obsWS.setCurrentScene("Game")

@device.eventHandler(KEY_W)
async def endingSceneStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_W])
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)
        await obsWS.setCurrentScene("Ending")

@device.eventHandler(KEY_2)
async def startingSceneStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_2])
        #await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)
        await obsWS.setCurrentScene("Starting")

@device.eventHandler(KEY_C)
async def toggleNDICaptureStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_K])
        await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)

@device.eventHandler(KEY_D)
async def toggleLookingGlassCaptureStream(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_D])
        await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)

@device.eventHandler(KEY_F1)
async def musicVolumeDown(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN or event.value == KeyPressHandler.KEY_STATE.KEY_HOLD:
        ProgramHandler("mpc --host 192.168.1.119 volume -1")

@device.eventHandler(KEY_F2)
async def musicVolumeUp(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN or event.value == KeyPressHandler.KEY_STATE.KEY_HOLD:
        ProgramHandler("mpc --host 192.168.1.119 volume +1")

@device.eventHandler(KEY_F3)
async def discordVolumeDown(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN or event.value == KeyPressHandler.KEY_STATE.KEY_HOLD:
        ProgramHandler("/home/popcorn9499/Scripts/perSinkVolumeControl Communication_Audio -1%")

@device.eventHandler(KEY_F4)
async def discordVolumeUp(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN or event.value == KeyPressHandler.KEY_STATE.KEY_HOLD:
        ProgramHandler("/home/popcorn9499/Scripts/perSinkVolumeControl Communication_Audio +1%")

@device.eventHandler(KEY_G)
async def discordMicMute(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_F13])
        await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)

@device.eventHandler(KEY_B)
async def discordDeffen(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_F14])
        await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)

@device.eventHandler(KEY_GRAVE)
async def replayBufferSave(event):
    if event.value == KeyPressHandler.KEY_STATE.KEY_DOWN:
        key = KeyPressHandler.KeyPress(keys=[KEY_LEFTCTRL,KEY_COMMA])
        await key.keyPress(keyState=KeyPressHandler.KEY_STATE.KEY_TOGGLE,pressDuration=0.1)
        await obsWS.saveReplayBuffer()


# @device.eventHandler(KEY_B)
# async def bar(event):
#     print("This is bar's first handler")
#     print(evdev.categorize(event))

async def run(device,obsWS):
    await device.init()
    await obsWS.init()
    while (True):
        await asyncio.sleep(60)


asyncio.run(run(device,obsWS))