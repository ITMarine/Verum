import asyncio
from fastapi import FastAPI, WebSocket


app = FastAPI()

unsent = "../unsent/unsent_queue"


async def get_output():  #здесь буду забирать данные из файла
    with open(unsent, 'r') as f:
        output = f.read()
        if output:
            with open(unsent, 'wb'):
                pass
            return output
    return


@app.websocket("/listen_results")
async def websocket_endpoint(websocket: WebSocket):
    path = "../unsent/unsent_queue"
    await websocket.accept()
    try:
        while True:
            message = await get_output()
            await asyncio.sleep(1)
            if message:
                await websocket.send_text(f"{message}")
    except KeyboardInterrupt:
        await websocket.close()
