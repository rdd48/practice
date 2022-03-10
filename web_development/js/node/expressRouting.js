// section 47

const express = require('express');
const app = express();

const shelterRoutes = require('./routes/shelters')


// this appends '/shelters' to front of paths in shelterRoutes
app.use('/shelters', shelterRoutes);

app.listen(3000, () => {
    console.log('listening')
})