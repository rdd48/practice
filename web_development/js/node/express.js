// express framework is used to launch servers
// to install: npm init then npm i express

const express = require('express');
const app = express();
// console.dir(app)

// this runs whenever server is reached
// req (request) and res (response) are default objects
// app.use((req, res) => {
//     console.log('i print to the terminal when app is used')
//     res.send('<h1>Hello, world! I am sent to the server</h1>')
// })

app.get('/', (req, res) => {
    res.send('home GET request @ localhost:3000!')
})

app.get('/cats', (req, res) => {
    res.send('cat GET request @ localhost:3000/cats!')
})

app.post('/cats', (req, res) => {
    res.send('cat POST request @ localhost:3000/cats!')
})

// this goes to anything after /cats/?
app.get('/cats/:newVar', (req, res) => {
    const { newVar } = req.params
    res.send(`cat/${newVar} POST request @ localhost:3000/cats/${newVar}!`)
})

app.get('/search', () => {
    // query string: ?key=value&key2=value2
    const { myQueryStr } = req.query // returns an obj
})

app.post('*', (req, res) => {
    res.send('I dont know that path')
})

// this starts a new server
app.listen(3000, () => {
    // goes to localhost:3000
    console.log('i start the server and will print to terminal')
})

// to automatically reload server when code is changed
// then run nodemon express.js