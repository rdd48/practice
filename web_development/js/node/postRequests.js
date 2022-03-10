const express = require('express');
const app = express();
const path = require('path');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));
// app.use(express.static(path.join(__dirname, 'public')))
app.use(express.urlencoded({ extended: true }))
// could also do app.use(express.json())

app.get('/post_request', (req, res) => {
    res.render('post_request')
})

app.post('/post_request', (req, res) => {
    res.send('posted data!')
    // req.body is an obj with key myVar and form-submitted text as the value
    const { myVar } = req.body;
    console.log(`posting ${myVar} to localhost:3000/restful`);
})

app.listen(3000, () => {
    console.log('listening on port 3000')
})