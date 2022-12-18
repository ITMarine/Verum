import asyncio
import websockets


url = 'ws://localhost:8001/ws'


async def test():
    async with websockets.connect(url) as websocket:
        while True:
            response = await websocket.recv()
            print(response)


asyncio.run(test())
