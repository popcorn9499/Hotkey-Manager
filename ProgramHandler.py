import asyncio

class ProgramHandler():
    def __init__(self,cmd):
        self.cmd = cmd
        loop = asyncio.get_event_loop()
        loop.create_task(self.run())

    async def run(self):
        proc = await asyncio.create_subprocess_shell(
        self.cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()
        if stdout:
            print(f'[stdout]\n{stdout.decode()}')
        if stderr:
            print(f'[stderr]\n{stderr.decode()}')