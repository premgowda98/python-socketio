import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/':'./public/'
})

def task(sid):
    sio.sleep(5)
    sio.emit('from_basckground', {'resp': 'Gowda'}, to=sid)

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
    sio.start_background_task(task, sid)
    # sio.emit('from_server', {'message': 'from server'}, to=sid)
    # print('emitted')

    return 'from server, you will get results in 5s'


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

