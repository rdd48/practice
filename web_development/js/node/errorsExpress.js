// https://expressjs.com/en/guide/error-handling.html

const express = require('express')
const app = express();

// define custom error class
class AppError extends Error {
    constructor(message, status) {
        super();
        this.message = message;
        this.status = status;
    }
}

app.get('/error', () => {
    throw new AppError('This is my AppError custom class', 400)
})

function wrapAsync(fn) {
    return function (req, res, next) {
        fn(req, res, next).catch(e => next(e))
        // this is written so that we don't need try/catch for all potential async issues
        // basically adding on .catch to every function it is used on
    }
}

app.get('/asyncerror', wrapAsync(async (req, res, next) => {
    return next(new AppError('Need to handle async errors with next', 404));
    // also use try/catch to handle mongoose errors, in catch do:
    // catch(e) {next(e)} (with next in callback fxns args)
    // wrapAsync does something like this
}))

// if error is thrown in above path, this runs
app.use((err, req, res, next) => {
    console.log('first error')
    const { status = 'defaultValue', message = 'defaultMessage' } = err;

    // mongoose errors have name attribute
    console.log(err.name);
    if (err.name === 'ValidationError') {
        console.log('I am a Mongoose validation error')
    }
    res.status(status).send(message)

    // lets you go to next error-handling middleware 
    // next() would just go to next middleware
    next(err);
})

app.listen(3000, () => {
    console.log('listening')
})