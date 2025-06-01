from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from src.feature.get_last_detection_service import GetLastDetectionServiceFactory


app = FastAPI()


get_last_detection_service = GetLastDetectionServiceFactory.create()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        result = await get_last_detection_service.get_last_detection()

        data = result.model_dump_json(by_alias=True)
        
        print(data, type(data), "data")

        await websocket.send_text(data)