from utils import config
import simpleobsws
import asyncio


class obsWSHandler:
    '''
    this constructor takes takes
        self
        confName string
    returns
        none
    '''
    def __init__(self, confName):
        conf = config.load(confName)
        self._url = conf["obs_ws_url"]
        self._password = conf["obs_ws_password"]
        parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False) # Create an IdentificationParameters object (optional for connecting)

        self._ws = simpleobsws.WebSocketClient(url = self._url, password = self._password, identification_parameters = parameters) # Every possible argument has been passed, but none are required. See lib code for defaults.

    #function to be called when starting the program
    async def init(self):
        await self.connect()
        request = simpleobsws.Request('GetVersion') # Build a Request object
        while (True):
            ret = await self._call(request) # Perform the request
            if ret.ok(): # Check if the request succeeded
                print("Request succeeded! Response data: {}".format(ret.responseData))
            else:
                print("failed " + str(ret.requestStatus))
                await self._ws.disconnect()
                await self.connect()
            await asyncio.sleep(30)
        await ws.disconnect() # Disconnect from the websocket server cleanly

    '''
    this function takes
        self
        name string
    returns
        none
    '''
    async def toggleMute(self,name):
        request = simpleobsws.Request("ToggleInputMute", requestData={"inputName": name})
        ret = await self._call(request)

    '''
    this function takes
        self
        name string
    returns
        none
    '''
    async def setCurrentScene(self,name):
        request = simpleobsws.Request("SetCurrentProgramScene", requestData={"sceneName": name})
        ret = await self._call(request)

    '''
    this function takes
        self
        name string
    returns
        none
    '''
    async def saveReplayBuffer(self):
        request = simpleobsws.Request("SaveReplayBuffer")
        ret = self._call(request)
    '''
    this function takes
        self
        request simpleobsws.Request
    returns
        simpleobsws.RequestResponse
    '''
    async def _call(self, request):
        ret = simpleobsws.RequestResponse("")
        try:
            ret = await self._ws.call(request)
        except simpleobsws.NotIdentifiedError:
            print("Stop pressing these keys without obs launched")
        return ret

    async def connect(self):
        connected = False
        while (not connected):
            try:
                await self._ws.connect()
                await self._ws.wait_until_identified()
                connected = True
            except OSError:
                await asyncio.sleep(20)            
            

    