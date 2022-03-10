// nodemon mongo_express.js

const express = require('express');
const app = express();
const path = require('path');
const mongoose = require('mongoose');
const methodOverride = require('method-override')

const Product = require('./models/product');
const Farm = require('./models/farm');


app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'ejs')
app.use(express.urlencoded({ extended: true }))
app.use(methodOverride('_method'))

mongoose.connect('mongodb://localhost:27017/farmstand')
    .then(() => {
        console.log('connection open!')
    })
    .catch(err => {
        console.log(err)
    })

// farm routes

app.get('/farms', async (req, res) => {
    const farms = await Farm.find({});
    res.render('farms/index', { farms })
})

app.get('/farms/new', (req, res) => {
    res.render('farms/new')
})

app.post('/farms', async (req, res) => {
    const farm = new Farm(req.body);
    await farm.save();
    res.redirect('/farms')
})

app.get('/farms/:id', async (req, res) => {
    const { id } = req.params
    const farm = await Farm.findById(id)
        .populate('products')
    res.render('farms/show', { farm })
})

app.get('/farms/:id/products/new', async (req, res) => {
    const { id } = req.params;
    const farm = await Farm.findById(id)
    res.render('products/new', { farm });
})

app.post('/farms/:id/products', async (req, res) => {
    const { id } = req.params
    const farm = await Farm.findById(id);
    const product = new Product(req.body);

    farm.products.push(product);
    product.farm = farm;

    await farm.save();
    await product.save();

    res.redirect(`/farms/${id}`)
})

app.delete('/farms/:id', async (req, res) => {
    const deleted = await Farm.findByIdAndDelete(req.params.id);
    res.redirect('/farms')
})

// products routes

app.get('/products', async (req, res) => {
    const products = await Product.find({});
    // console.log(products)
    res.render('products/index', { products })
})

app.get('/products/new', (req, res) => {
    res.render('products/new')
})

app.get('/products/:id', async (req, res) => {
    const { id } = req.params
    const product = await Product.findById(id)
        .populate('farm', 'name')
    res.render('products/show', { product })
})

app.get('/products/:id/edit', async (req, res) => {
    const { id } = req.params
    const product = await Product.findById(id)
    res.render('products/edit', { product })
})

// edit using PUT request. why not PATCH as before?
app.put('/products/:id', async (req, res) => {
    const { id } = req.params;
    const product = await Product.findByIdAndUpdate(id, req.body, { runValidators: true, new: true })
    res.redirect(`/products/${product._id}`)
})

app.delete('/products/:id', async (req, res) => {
    const { id } = req.params;
    const deleted = await Product.findByIdAndDelete(id)
    res.redirect('/products')
})

app.post('/products', async (req, res) => {
    const newProduct = await new Product(req.body); // shoud really check that req.body object fits schema first
    newProduct.save();
    res.redirect(`/products/${newProduct._id}`)
})

app.listen(3000, () => {
    console.log('listening on 3000')
})