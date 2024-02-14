import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/':'./public/'
})

@sio.event
def connect(sid, environ):
    # sid is the client id which is connected
    # environ is header containing info
    print('New Client', sid)


@sio.event
def disconnect(sid):
    print('Disconnected', sid)

