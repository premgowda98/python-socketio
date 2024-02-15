import socketio
import eventlet
import random

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/':'./public/'
})

total_client = 0
a_groub = 0
b_group = 0

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
    global total_client
    global a_groub
    global b_group
    total_client  = total_client + 1
    sio.emit('client_count', total_client) # will broadcast for everyone

    if random.random()>0.5:
        sio.enter_room(sid, 'a')
        a_groub += 1
        sio.emit('group_info', f'You are in group A along with {a_groub} members', to='a')
    else:
        sio.enter_room(sid, 'b')
        b_group += 1
        sio.emit('group_info', f'You are in group B along with {b_group} members', to='b')


@sio.event
def from_client(sid, data):
    print(sid, data)
    sio.start_background_task(task, sid)
    # sio.emit('from_server', {'message': 'from server'}, to=sid)
    # print('emitted')

    return 'from server, you will get results in 5s'

@sio.event
def disconnect(sid):
    global total_client
    global a_groub
    global b_group
    total_client  = total_client-1
    sio.emit('client_count', total_client)

    if 'a' in sio.rooms(sid):
        sio.enter_room(sid, 'a')
        a_groub -= 1
        sio.emit('group_info', f'You are in group A along with {a_groub} members', to='a')
    elif 'b' in sio.rooms(sid):
        sio.enter_room(sid, 'a')
        b_group -= 1
        sio.emit('group_info', f'You are in group B along with {b_group} members', to='b')


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

    # command line code
    # gunicorn -k eventlet -w 1 --reload main:app -b 0.0.0.0:5000

