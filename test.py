import asyncio
import websockets


async def test_websocket():
    uri = "ws://localhost:8000/ws"  # адрес твоего WebSocket-сервера
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, server!")
        response = await websocket.recv()
        print(f"Received from server: {response}")


asyncio.run(test_websocket())
