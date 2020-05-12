import asyncio

class EventHandler:
    def __init__(self,states=()):
        self.handlers = {}
        self.states=states

    async def call(self, type,*args, **kargs):
        if type in self.handlers:
            for h in self.handlers[type]:
                await h(*args,**kargs)

    def __call__(self, type):
        def registerhandler(handler):
            if type in self.handlers:
                self.handlers[type].append(handler)
            else:
                self.handlers[type] = [handler]
            return handler
        return registerhandler