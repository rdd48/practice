// moongoosejs.com
// npm i mongoose
// make sure mongod is running

const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/moviesDb') // creates or connects to moviesDb
    .then(() => {
        console.log('connection open!')
    })
    .catch(err => {
        console.log(err)
    })

// define a schema
const movieSchema = new mongoose.Schema({
    // schema types (e.g. default) in docs under guides > schema types
    title: {
        type: String,
        required: true,
        default: 'defaultMovieName',
        maxlength: 60,
    },
    year: {
        type: Number,
        min: [1900, 'custom error message here'],
    },
    score: Number,
    rating: {
        type: String,
        enum: ['G', 'PG', 'PG13', 'R'] // enum requires val be in provided array
    },
    categories: [String], // lets you pass an array of str
    myObj: {
        key1: String,
        key2: Boolean
    }
})

// define custom instance methods for our schema
// available on model (Movie.getTitle()) or found items
movieSchema.methods.getTitle = function () {
    console.log(`${this.title}`)
    // return this.save()
}
movieSchema.methods.findAndUpdateTitle = async (oldTitle, newTitle) => {
    const foundMovie = await Movie.findOne({ title: oldTitle })
    foundMovie.title = newTitle;
    await foundMovie.getTitle();
}

// define static method
movieSchema.statics.incrementYear = function () {
    this.updateMany({}, { year: year + 1 }) // does the year + 1 work? not sure
}

// virtual schema
movieSchema.virtual('titlePlusYear').get(function () {
    return `${this.title} - ${this.year}`
})
// now amadeus.titlePlusYear returns 'Amadeus - 1985'

// middleware. first str argument takes a method
movieSchema.pre('save', async function () {
    // this.title = 'newTitle' // i.e. you can update attrs in middleware
    console.log('saving...')
})
movieSchema.post('save', async function () {
    console.log('saved!')
})

// model name should be singular and uppercase
// mongoose will turn this name ('Movie'), lowercases and pluralizes it
const Movie = mongoose.model('Movie', movieSchema)

// add db (collection?) entries
const amadeus = new Movie({ title: 'Amadeus', score: 1985, score: 9.2, rating: 'R' })
amadeus.save() // adds new Movie instance to movies database
// Movie.insertMany([myMovieObj1, myMovieObj2])
//     .then(data => console.log(data)) // logs db object, so Movie.insertMany must return the db?

// find. can use .find(), .findOne(), .findById()
// still takes operators like $gte
Movie.find({ rating: { $in: ['PG13', 'R'] } })
    .then(data => console.log(data))

// update. .updateOne(), .updateMany()
// .findOneAndUpdate() takes same args and works same but returns old version. pass {new: true} to get new update
Movie.updateMany({ title: 'Amadeus' }, { year: 1983 }) // updates year to 1983
    .then(res => console.log(res))
Movie.findOneAndUpdate(newObj, { new: true, runValidators: true }) // new means return the new obj, runValidators runs schema validators


// delete. .deleteOne(), .deleteMany(), .findOneAndDelete()
Movie.deleteOne({ title: 'Amadeus' })