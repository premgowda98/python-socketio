import socketio
import eventlet

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

@sio.event
def from_client(sid, data):
    print(sid, data)
    sio.emit('from_server', {'message': 'from server'}, to=sid)
    print('emitted')


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

