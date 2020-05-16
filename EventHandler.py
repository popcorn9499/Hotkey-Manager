import asyncio

class EventHandler: 
    def __init__(self):
        self.handlers = {} #creates a list of the handlers

    async def call(self, type,*args, **kargs): #calls any of handlers with the required key presses
        if type in self.handlers:
            for h in self.handlers[type]:
                await h(*args,**kargs)

    def __call__(self, type, *args, **kwargs): #handles adding the handler to the handler list
        def registerhandler(handler):
            if type in self.handlers:
                self.handlers[type].append(handler)
            else:
                self.handlers[type] = [handler]
            return handler
        return registerhandler