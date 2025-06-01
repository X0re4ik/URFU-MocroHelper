from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from src.feature.get_last_detection_service import GetLastDetectionServiceFactory
from src.feature.get_server_info import GetServerInfoServiceFactory


app = FastAPI()


get_last_detection_service = GetLastDetectionServiceFactory.create()

get_server_info_service = GetServerInfoServiceFactory.create()



@app.get("/api/v1/micro-helper/server-info")
async def server_info_router():
    results = await get_server_info_service.get_server_info()
    return results.model_dump(by_alias=True)

@app.websocket("/api/v1/micro-helper/last-detection")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        result = await get_last_detection_service.get_last_detection()

        data = result.model_dump_json(by_alias=True)
        
        print(data, type(data), "data")

        await websocket.send_text(data)