// this file is used to "seed" our mongo database

const mongoose = require('mongoose');
const Product = require('./models/product');

mongoose.connect('mongodb://localhost:27017/farmstand')
    .then(() => {
        console.log('connection open!')
    })
    .catch(err => {
        console.log(err)
    })

const p = new Product({
    name: 'Grapefruit',
    price: 1.99,
    category: 'fruit'
})

// p.save().then(p => {
//     console.log(p)
// })
//     .catch(e => console.log(e))

const seedProducts = [
    {
        name: 'Onion',
        price: 0.99,
        category: 'vegetable'
    },
    {
        name: 'Cheddar cheese',
        price: 4.99,
        category: 'dairy'
    },
]

Product.insertMany(seedProducts)