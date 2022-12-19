import asyncio
import websockets


URL = 'ws://localhost:8001/listen_results'


async def listen():
    try:
        async with websockets.connect(URL, ping_interval=None) as websocket:
            while True:
                response = await websocket.recv()
                print(response)
    except asyncio.TimeoutError:
        print("TimeoutError connecting")

asyncio.run(listen())
