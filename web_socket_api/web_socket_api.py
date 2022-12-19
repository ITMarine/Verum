from fastapi import FastAPI, WebSocket


app = FastAPI()

UNSENT = "/app/unsent/unsent_queue"


async def get_output_message():
    """extracts processed reversed message
    from file"""
    with open(UNSENT, 'r') as f:
        output_message = f.read()
        if output_message:
            with open(UNSENT, 'wb'):
                pass
            return output_message
    return


@app.websocket("/listen_results")
async def websocket_endpoint(websocket: WebSocket):
    """returns reversed message to the listen_result.py"""
    await websocket.accept()
    try:
        while True:
            message = await get_output_message()
            if message:
                await websocket.send_text(f"{message}")
    except KeyboardInterrupt:
        await websocket.close()

