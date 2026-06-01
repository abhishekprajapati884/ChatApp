from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

template = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

class ConnectionManager:
    def __init__(self):
        self.active_connection: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connection.append(websocket)
    def disconnect(self, websocket: WebSocket):
        self.active_connection.remove(websocket)
    async def send_personal_message(self, websocket: WebSocket, message: str):
        await websocket.send_text(message)
    async def broadcast(self, message: str):
        for connection in self.active_connection:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def get_app(request: Request):
    return template.TemplateResponse("index.html", {"request": request, "title": "Chat 1"})


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(websocket, f"Message text was: {data}")
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")