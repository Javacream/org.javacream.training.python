#pip install websocket-client
import websocket

ws = websocket.WebSocket()
ws.connect("ws://localhost:8000/ws/echo/")
ws.send("Hello, Server")
print(ws.recv())
ws.close()