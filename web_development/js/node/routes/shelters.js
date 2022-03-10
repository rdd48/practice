const express = require('express');

const router = express.Router();

// middleware example
// needs to be before routes it seems
// uncomment to view indiv pages w/o permission message
router.use((req, res, next) => {
    if (req.query.isAdmin) {
        next();
    } else {
        res.send('sorry, you need permission first')
    }
})

router.get('/', (req, res) => {
    res.send('home shelters message')
})

router.post('/', (req, res) => {
    res.send('posting to shelters')
})

router.get('/:id', (req, res) => {
    res.send('viewing shelters message')
})


module.exports = router;