// section 47
// npm i cookie-parser
// https://expressjs.com/en/api.html

const express = require('express')
const cookieParser = require('cookie-parser')
const app = express();

// secret-string (usually much more complex) is used to "sign" cookies
// i.e., ensure that the cookie wasn't tampered with.
app.use(cookieParser('secret-string'));

app.get('/cookies', (req, res) => {
    const { name } = req.cookies
    console.log(req.cookies, name)
    res.send(req.cookies)
})

app.get('/setname', (req, res) => {
    // permanently sends a name cookie k/v pair to localhost:3000
    res.cookie('name', 'teddy divine')
    res.send('sent you a cookie')
})

app.get('/signedcookie', (req, res) => {
    res.cookie('name', 'teddy divine signed', { signed: true })
    res.send(req.signedCookies)
})

app.listen(3000, () => {
    console.log('localhost:3000')
})