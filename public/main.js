const sio = io();
const emit_buttton = document.getElementById('emit_buttton')

sio.on('connect', ()=>{
    console.log('Connected')
    // rmit takes two args, event name and event data
})

emit_buttton.addEventListener('click', ()=>{
    sio.emit('from_client', {
        connected: 'from cient guru'
    }, (response)=>{
        console.log(response)
    })
})

sio.on('disconnect', ()=>{
    console.log('disconnected')
})

sio.on('from_basckground', (data)=>{
    console.log('This is from background task')
    console.log(data)
})