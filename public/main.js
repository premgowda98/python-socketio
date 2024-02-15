const sio = io({
    transportOptions : {
        polling: {
            extraHeaders: {
                'X-Username': window.location.hash.substring(1)
                }
            }
        }
    }
);

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

sio.on('from_basckground', (data, cb)=>{
    console.log(data)
    cb(`client response for server response, this is what you sent ${JSON.stringify(data)}`)
})

sio.on('client_count', (data)=>{
    console.log(`Total Connected Members ${data}`)
})

sio.on('group_info', (data)=>{
    console.log(`${data}`)
})