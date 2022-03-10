// section 48
// sessions: store data on server in "data store" (unlike cookies, which store in browser)
// seems that browser sends a session id (small key) to get larger dataset from server

// npm i express-session connect-flash
// express-session sets up sessions
// connect-flash displays messages
const express = require('express');
const app = express();

const session = require('express-session')
const flash = require('connect-flash');

// pass in session options. secret is needed (?)
// memory storage is leaky, not for production, as designed. need to set for data permanence
app.use(session({
    secret: 'my-secret',
    resave: false,
    saveUninitialized: false,
}))
app.use(flash());

app.use((req, res, next) => {
    // get any flash local vars
    res.locals.messages = req.flash('success');
    next();
})

app.get('/viewcount', (req, res) => {
    if (req.session.count) {
        req.session.count += 1;
    } else {
        req.session.count = 1;
    }

    if (res.locals.messages.length) {
        res.send(`Hello ${res.locals.messages}, You have viewed this page ${req.session.count} times!`)
    } else {
        res.send(`You have viewed this page ${req.session.count} times!`)
    }

})

app.get('/register', (req, res) => {
    // add to req.session via query strings
    // ie http://localhost:3000/register?username=teddy
    const { username = 'Anonymous' } = req.query;
    req.session.username = username;

    // req.flash() takes a key arg and then a message. typically before a redirect
    req.flash('success', req.session.username)

    res.redirect('/viewcount')
    // res.send(`Hello ${username}`)
})

app.listen(3000, () => {
    console.log('localhost:3000')
})