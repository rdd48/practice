// rest = representational state transfer
// rest is a set of guidelines for how clinets + servers should communicate
// crud: create retrieve update delete

// pattern to follow (ONE option for RESTful routing):
// base url is /comments
// GET /comments => list all comments
// GET /comments/:id => get one comment (using id)
// POST /comments => create a new comment
// PATCH /comments/:id => Update one comment
// DELETE /comments/:id => Destroy one comment

const express = require('express');
const app = express();
const path = require('path');
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));
// app.use(express.static(path.join(__dirname, 'public')))
app.use(express.urlencoded({ extended: true }))

// npm i uuid: for creating unique identifiers
const { v4: uuid } = require('uuid')

// method-override: for doing requests besides get/post
const methodOverride = require('method-override');
app.use(methodOverride('_method'))


let comments = [{
    id: uuid(),
    username: 'Teddy',
    comment: 'hungry'
},
{
    id: uuid(),
    username: 'Teddy',
    comment: 'still hungry'
},
{
    id: uuid(),
    username: 'Teddy',
    comment: 'thanks for feeding me, I love dad'
}]

// render the first form
app.get('/comments', (req, res) => {
    res.render('comments/index', { comments })
})

// render new comment submission form
app.get('/comments/new', (req, res) => {
    res.render('comments/new')
})

// listen for posts that go to (not originate from!) index form
app.post('/comments', (req, res) => {
    const { username, comment } = req.body;
    const id = uuid();
    comments.push({ id, username, comment })
    res.redirect('/comments'); // redirects to a get request
    // res.render('comments/index', { comments })
})

// show comments by id
app.get('/comments/:id', (req, res) => {
    const { id } = req.params;
    const comment = comments.find(c => c.id === id);
    res.render('comments/show', { comment })
})

// update post via patch request
app.get('/comments/:id/edit', (req, res) => {
    const { id } = req.params;
    const comment = comments.find(c => c.id === id);
    res.render('comments/edit', { comment })
})

app.patch('/comments/:id', (req, res) => {
    const { id } = req.params;
    const newCommentText = req.body.comment;
    const foundComment = comments.find(c => c.id === id);
    foundComment.comment = newCommentText; // edits the object in the list in place?
    res.redirect('/comments')
})

// delete post
app.delete('/comments/:id', (req, res) => {
    const { id } = req.params;
    // const foundComment = comments.find(c => c.id === id);
    comments = comments.filter(c => c.id !== id);
    res.redirect('/comments');
})

app.listen(3000, () => {
    console.log('listening on 3000')
})