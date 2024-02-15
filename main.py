import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/':'./public/'
})

total_client = 0

def cb(data):
    print(data)


def task(sid):
    sio.sleep(5)
    # sio.emit('from_basckground', {'resp': 'Gowda'}, to=sid, callback=cb)
    result = sio.call('from_basckground', {'resp': 'Gowda'}, to=sid)
    print(result)

@sio.event
def connect(sid, environ):
    # sid is the client id which is connected
    # environ is header containing info
    print('New Client', sid)
    global total_client
    total_client  = total_client + 1
    sio.emit('client_count', total_client) # will broadcast for everyone


@sio.event
def from_client(sid, data):
    print(sid, data)
    sio.start_background_task(task, sid)
    # sio.emit('from_server', {'message': 'from server'}, to=sid)
    # print('emitted')

    return 'from server, you will get results in 5s'

@sio.event
def disconnect(sid):
    print('Disconnected', sid)
    global total_client
    total_client  = total_client-1
    sio.emit('client_count', total_client)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

    # command line code
    # gunicorn -k eventlet -w 1 --reload main:app -b 0.0.0.0:5000

