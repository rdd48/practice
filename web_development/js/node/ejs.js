// ejs (embedded js) used to make website templates, i.e. pages that are similar but with dynamic elements

const express = require('express');
const app = express();
const path = require('path'); // built into ejs

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));

// serve static files, i.e. css, js, etc being in a public directory
app.use(express.static(path.join(__dirname, 'public')))

app.get('/', (req, res) => {
    res.render('home'); // renders views/home.ejs
})

app.get('/random', (req, res) => {
    const num = Math.floor(Math.random() * 10) + 1;
    res.render('random', { rand: num })
})

app.get('/r/:subreddit', (req, res) => {
    const { subreddit } = req.params;
    res.render('subreddit', { subreddit })
})

app.get('/pugs', (req, res) => {
    const pugs = ['Teddy', 'Stu', 'Thor'];
    res.render('pugs', { pugs })
})

app.listen(3000, () => {
    console.log('listening on port 3000')
})