const express = require('express');
const router = express.Router();
const catchAsync = require('../utils/catchAsync')
const Campground = require('../models/campgrounds')
const { isLoggedIn, validateCampground, isAuthor } = require('../middleware.js')
const campgrounds = require('../controllers/campgrounds')

// section 54: multer middleware
const { storage } = require('../cloudinary') // index file automatically found by node
const multer = require('multer');
const upload = multer({ storage })

// section 53: moved all functions to campgrounds object in controllers/campgrounds
// also added router.route instead of individual .get, .post, etc
router.route('/')
    .get(catchAsync(campgrounds.index))
    .post(isLoggedIn, upload.array('image'), validateCampground, catchAsync(campgrounds.createCampground))

router.get('/new', isLoggedIn, campgrounds.renderNewForm)

router.route('/:id')
    .get(catchAsync(campgrounds.showCampgrounds))
    .put(isLoggedIn, isAuthor, upload.array('image'), validateCampground, catchAsync(campgrounds.updateCampground))
    .delete(isLoggedIn, isAuthor, catchAsync(campgrounds.deleteCampground))

router.get('/:id/edit', isLoggedIn, isAuthor, catchAsync(campgrounds.renderEditForm))

module.exports = router;