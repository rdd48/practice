// section 50. there's a whole demo app section, but since we're doing this in yelpCamp, not doing this myself but watching the vids
// later, in section 51, we use the passport library
// authentication: the user is the user
// authorization: what the user can do

// npm i bcrypt
// docs: https://www.npmjs.com/package/bcrypt
const bcrypt = require('bcrypt');

// generate a hash from password
// salting: add random chars to password to increase complexity
const hashPassword = async (pw) => {
    // generate salt separately
    // const salt = await bcrypt.genSalt(12);
    // const hash = await bcrypt.hash(pw, salt);

    // generate salt & hash in one go
    console.log(await bcrypt.hash(pw, 12))
}

const login = async (pw, hashedPw) => {
    console.log(await bcrypt.compare(pw, hashedPw))
}

// returns true, since hash was generated from hashPassword('password')
login('password', '$2b$12$TIgG2sXs/Q2E5q.p/EOSD.Fy8l7v3zp6X6/3EIRAEb287CDBdB5OW'
);

// false
login(
    'password!',
    '$2b$12$TIgG2sXs/Q2E5q.p/EOSD.Fy8l7v3zp6X6/3EIRAEb287CDBdB5OW'
);

// from demo
res.session.destroy() // destroys all session info
// also defined a findUserAndValidate static method to userSchema
