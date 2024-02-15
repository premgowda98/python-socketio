const sio = io();

sio.on('connect', ()=>{
    console.log('Connected')
    // rmit takes two args, event name and event data
    sio.emit('from_client', {
        connected: 'from cient guru'
    }, (response)=>{
        console.log(response)
    })

})

sio.on('disconnect', ()=>{
    console.log('disconnected')
})

// sio.on('from_server', (data)=>{
//     console.log(data)
// })