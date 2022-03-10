// section 53
// this file exports functions to organize our app
const Campground = require('../models/campgrounds')
const { cloudinary } = require('../cloudinary')

// section 55 mapbox docs: https://github.com/mapbox/mapbox-sdk-js
const mbxGeocoding = require('@mapbox/mapbox-sdk/services/geocoding')
const mapboxToken = process.env.MAPBOX_TOKEN
const geocoder = mbxGeocoding({ accessToken: mapboxToken })

module.exports.index = async (req, res) => {
    const campgrounds = await Campground.find({})
    res.render('campgrounds/index', { campgrounds })
}

module.exports.renderNewForm = (req, res) => {
    res.render('campgrounds/new')
}

module.exports.createCampground = async (req, res, next) => {
    const geoData = await geocoder.forwardGeocode({
        query: req.body.campground.location,
        limit: 1,
    }).send()


    // use req.body.campground instead of just req.body b/c name attr in views/new.ejs is campground[pattern]
    const newCampground = new Campground(req.body.campground);
    newCampground.author = req.user._id; // section 52, user is auto-added
    newCampground.geometry = geoData.body.features[0].geometry;

    // req.files from multer, section 54
    newCampground.images = req.files.map(f => ({ url: f.path, filename: f.filename }))

    await newCampground.save();
    console.log(newCampground)
    console.log(newCampground)
    req.flash('success', 'Successfully made a new campground!');
    res.redirect(`/campgrounds/${newCampground._id}`)
}

module.exports.showCampgrounds = async (req, res) => {
    const { id } = req.params
    const campground = await Campground.findById(id)
        .populate({
            path: 'reviews',
            populate: {
                path: 'author'
            }
        }).populate('author');
    // this above .populate mess comes from the last vid in section 52
    if (!campground) {
        req.flash('error', 'Cannot find this campground');
        return res.redirect('/campgrounds')
    }
    res.render('campgrounds/show', { campground })
}

module.exports.renderEditForm = async (req, res) => {
    const { id } = req.params
    const campground = await Campground.findById(id)
    if (!campground) {
        req.flash('error', 'Cannot edit this campground');
        return res.redirect('/campgrounds')
    }
    res.render('campgrounds/edit', { campground })
}

module.exports.updateCampground = async (req, res) => {
    const { id } = req.params;
    const campground = await Campground.findByIdAndUpdate(
        id,
        { ...req.body.campground }, // same as req.body.campground
        { runValidators: true, new: true })
    const images = req.files.map(f => ({ url: f.path, filename: f.filename }))
    campground.images.push(...images)
    await campground.save()
    if (req.body.deleteImages) {
        for (let filename of req.body.deleteImages) {
            await cloudinary.uploader.destroy(filename);
        }
        await campground.updateOne({
            $pull: { images: { filename: { $in: req.body.deleteImages } } }
        })
    }
    console.log(campground)
    req.flash('success', 'Successfully updated campground!');
    res.redirect(`/campgrounds/${campground._id}`)
}

module.exports.deleteCampground = async (req, res) => {
    const { id } = req.params;
    const campground = await Campground.findById(id);
    if (!campground.author.equals(req.user._id)) {
        req.flash('error', 'You do not have permission to do that');
        return req.redirect(`/campgrounds/${id}`)
    }
    const deleted = await Campground.findByIdAndDelete(id)
    req.flash('success', 'Successfully deleted campground!');
    res.redirect('/campgrounds')
}