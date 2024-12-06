import socketio
import uvicorn

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/':'./public/'
})

@sio.event
async def connect(sid, environ):
    # sid is the client id which is connected
    # environ is header containing info
    print('New Client', sid)


@sio.event
async def disconnect(sid):
    print('Disconnected', sid)

if __name__ == '__main__':
    uvicorn.run(__name__+':app', port=5000)

