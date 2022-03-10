// section 54: set env vars either in production or develop mode
if (process.env.Node_ENV !== 'production') {
    require('dotenv').config();
}

const express = require('express');
const ejsMate = require('ejs-mate');
const path = require('path');
const session = require('express-session');
const flash = require('connect-flash');
const mongoose = require('mongoose');
const passport = require('passport');
const LocalStrategy = require('passport-local');

const ExpressError = require('./utils/ExpressError')
const methodOverride = require('method-override');

const User = require('./models/user')
const userRoutes = require('./routes/users');
const campgroundRoutes = require('./routes/campgrounds')
const reviewRoutes = require('./routes/reviews');

const mongoSanitize = require('express-mongo-sanitize');
const helmet = require('helmet');
const MongoDBStore = require('connect-mongo');


dbUrl = process.env.DB_URL || 'mongodb://localhost:27017/campground';
// dbUrl = 'mongodb://localhost:27017/campground'

mongoose.connect(dbUrl, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})

// this part was replaced with then/catch in lecture 381, but also works 
// (though it seems outdated according to mongoose docs)
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
    console.log('Database connected');
});

const app = express();

// ejs-mate lets you use templates to put in each ejs file
app.engine('ejs', ejsMate)
app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'ejs')

app.use(express.urlencoded({ extended: true }))
app.use(methodOverride('_method'))
app.use(express.static(path.join(__dirname, 'public')))

// section 58: prevent mongo injections, other vulnerabilities
app.use(mongoSanitize());
app.use(helmet({ crossOriginEmbedderPolicy: false, }));
const scriptSrcUrls = [
    "https://stackpath.bootstrapcdn.com/",
    "https://api.tiles.mapbox.com/",
    "https://api.mapbox.com/",
    "https://kit.fontawesome.com/",
    "https://cdnjs.cloudflare.com/",
    "https://cdn.jsdelivr.net",
    "https://code.jquery.com",
    "https://maxcdn.bootstrapcdn.com"
];
const styleSrcUrls = [
    "https://kit-free.fontawesome.com/",
    "https://stackpath.bootstrapcdn.com/",
    "https://api.mapbox.com/",
    "https://api.tiles.mapbox.com/",
    "https://fonts.googleapis.com/",
    "https://use.fontawesome.com/",
    "https://maxcdn.bootstrapcdn.com/",
];
const connectSrcUrls = [
    "https://api.mapbox.com/",
    "https://a.tiles.mapbox.com/",
    "https://b.tiles.mapbox.com/",
    "https://events.mapbox.com/",
];
const fontSrcUrls = [];
app.use(
    helmet.contentSecurityPolicy({
        directives: {
            defaultSrc: [],
            connectSrc: ["'self'", ...connectSrcUrls],
            scriptSrc: ["'unsafe-inline'", "'self'", ...scriptSrcUrls],
            styleSrc: ["'self'", "'unsafe-inline'", ...styleSrcUrls],
            workerSrc: ["'self'", "blob:"],
            objectSrc: [],
            imgSrc: [
                "'self'",
                "blob:",
                "data:",
                "https://res.cloudinary.com/dtgrctfwa/", //SHOULD MATCH YOUR CLOUDINARY ACCOUNT! 
                "https://images.unsplash.com/",
            ],
            fontSrc: ["'self'", ...fontSrcUrls],
        },
    })
);

const secret = process.env.SECRET || 'backup-secret'
const store = MongoDBStore.create({
    mongoUrl: dbUrl,
    secret,
    touchAfter: 24 * 60 * 60
})

store.on('error', function (e) {
    console.log('Session store error: ', e)
})

const sessionConfig = {
    store,
    name: 'needToChangeForSecurityReasons',
    secret,
    resave: false,
    saveUninitialized: true,
    cookie: {
        // Date.now() in millisec
        expires: Date.now() + (1000 * 60 * 60 * 24 * 7),
        maxAge: 1000 * 60 * 60 * 24 * 7,
        httpOnly: true,
        // secure: true,
    }
}
app.use(session(sessionConfig))
app.use(flash());

// section 51 on passport... woof
app.use(passport.initialize());
app.use(passport.session());
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

app.use((req, res, next) => {
    // get any flash local vars
    res.locals.currentUser = req.user;
    res.locals.success = req.flash('success');
    res.locals.error = req.flash('error');
    next();
})

app.use('/', userRoutes)
app.use('/campgrounds', campgroundRoutes)
app.use('/campgrounds/:id/reviews', reviewRoutes)

app.get('/', (req, res) => {
    res.render('home')
})

app.get('/fakeUser', async (req, res) => {
    const user = new User({ email: 'teddy@gmail.com', username: 'teddy' })
    const newUser = await User.register(user, 'teddyPassword')
})

app.all('*', (req, res, next) => {
    next(new ExpressError('Page not found', 404))
})

// ERRORS
app.use((err, req, res, next) => {
    const { statusCode = 500 } = err;
    if (!err.message) err.message = 'Oh no!'
    res.status(statusCode).render('error', { err })
})

// START
const port = process.env.PORT || 3000
app.listen(port, () => {
    console.log(`listening on ${port}`)
})