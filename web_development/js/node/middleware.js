const express = require('express');
const app = express();

// defining our own middleware follows this format
app.use((req, res, next) => {
    console.log('hello middleware world!');
    next(); // i.e., go to next middleware
})

// define separate function, only runs on homepage
const addDate = function (req, res, next) {
    req.requestTime = Date.now(); // creates custom attr in all reqs.
    next();
}
app.use('/dogs', addDate)


// using existing middleware, morgan
const morgan = require('morgan');

// npm i morgan
// morgan logs info to the console/terminal
// app.use means run this function each time any request is sent to the app
// app.use(morgan('tiny'));
app.use(morgan('common'));

app.get('/', (req, res) => {
    console.log(req.requestTime)
    res.send('home page!')
})

app.get('/dogs', (req, res) => {
    console.log(req.requestTime)
    res.send('dogs page!')
})

// can pass middleware as first of two callbacks to a get request
app.get('/secret', addDate, (req, res) => {
    res.send('Console has the date!')
    console.log(req.requestTime)
})

// define 404 with app.use for case when nothing is matched
app.use((req, res) => {
    // this only runs if no above routes are matched
    // res.send('404 not found!')
    throw new Error('404 error here')

})

app.listen(3000, () => {
    console.log('port 3000')
})