const mongoose = require('mongoose');
const Campground = require('../models/campgrounds')

const cities = require('./cities')
const { places, descriptors } = require('./seedHelpers')

mongoose.connect('mongodb://localhost:27017/campground', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
//
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
    console.log('Database connected');
});

const sample = (array) => array[Math.floor(Math.random() * array.length)]

const seedDb = async () => {
    await Campground.deleteMany({});
    for (let i = 0; i < 100; i++) {
        const random1000 = Math.floor(Math.random() * 1000);
        const price = Math.floor(Math.random() * 20) + 10;
        const camp = new Campground({
            author: '62170d5977becd9947cd68bd',
            location: `${cities[random1000].city}, ${cities[random1000].state}`,
            title: `${sample(descriptors)} ${sample(places)}`,
            images: [
                {
                    url: 'https://res.cloudinary.com/dtgrctfwa/image/upload/v1646601622/YelpCamp/wqkjkgj2e9haa61gmasx.png',
                    filename: 'YelpCamp/wqkjkgj2e9haa61gmasx',
                },
                {
                    url: 'https://res.cloudinary.com/dtgrctfwa/image/upload/v1646601622/YelpCamp/a07nc3fydkzaloruudgg.png',
                    filename: 'YelpCamp/a07nc3fydkzaloruudgg',
                }
            ],
            description: 'lorem ipsum',
            price,
            geometry: {
                type: 'Point',
                coordinates: [cities[random1000].longitude, cities[random1000].latitude]
            }
        })
        await camp.save()
    }

}

seedDb();