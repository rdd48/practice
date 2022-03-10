// section 45, mongoRelationshipsExpress
const mongoose = require('mongoose');
const { Schema } = mongoose;
const Product = require('./product')

const farmSchema = Schema({
    name: {
        type: String,
        required: [true, 'farm must have a name']
    },
    city: String,
    email: {
        type: String,
        required: [true, 'email required']
    },
    products: [{
        type: Schema.Types.ObjectId,
        ref: 'Product'
    }]
})

// schema middleware to delete related products in farm
// for .post(), see mongoose.js
// tbh don't really understand wtf is happening here
farmSchema.post('findOneAndDelete', async function (farm) {
    if (farm.products.length) {
        const res = await Product.deleteMany({ _id: { $in: farm.products } })
    }
})

const Farm = mongoose.model('Farm', farmSchema)
module.exports = Farm;