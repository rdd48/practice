// JS document object model
// html elements are objects under special document object

// view document as js object
console.dir(document)

// get element
let id = document.getElementById('my_id')
// get elements
// this returns an HTMLCollection object, which you can still loop thru or grab elements via [idx], but can't map
let imgCollection = document.getElementsByTagName('img');
let squareClass = document.getElementsByClassName('square');
for (let img of imgCollection) { console.log(img.source) }
// querySelector finds first element using css-type syntax
document.querySelector('h1')
document.querySelector('#my_id')
document.querySelector('.my_class')
//querySelectorAll is same idea but a collection
document.querySelectorAll('p a')

// innerText, innerHTML, textContent
let h1Text = document.querySelector('h1').innerText // content between open/close tag
let h1TextFull = document.querySelector('h1').textContent // content between open/close tag but shows display: none objects
let h1TextMarkup = document.querySelector('h1').innerHTML // get tags with text

// querySelector attributes/methods
document.querySelector('img').id = 'new_id' // sets id for all img elements
// src, href, title, etc all can be accessed or changed
document.querySelector('img').getAttribute('href') // gets exact link listed on html
document.querySelector('img').setAttribute('href', 'new/href/here') // resets href

// style attribute, (but unclear if current style is overwritten (?))
// camelCase not dash-case (like typical css)
h1Color = document.querySelector('h1').style.color
h1BackgroundColor = document.querySelector('h1').style.backgroundColor
// to deal with unclear styles, use:
h1BackgroundColorWindow = window.getComputedStyle(document.querySelector('h1').backgroundColor)

// classList is all classes of an element. use to apply multiple stlyes to an html element
document.querySelector('div').classList.add('newClass')
document.querySelector('div').classList.remove('newClass')
document.querySelector('div').classList.toggle('newClass') // turns on or off based on current state

// move between parent/child elements with .parentElement and .children (since there can be multiple children)
// move between siblings with .nextSibling/.previousSibling (gives us next node (?))
// better: also move between sublings with .nextSiblingElement/.previousSiblingElement

// create & position elements
let newImg = document.createElement('img')
newImg.src = 'my/source/file.png'
document.body.appendChild(newImg) // appends as last child of body

// append can add text or add element?
document.querySelector('p').append('appended text to paragraph', 'im also appended')
document.querySelector('p').prepend('appended text to paragraph', 'im also appended')

// insertAdjacentElement(). check the mozilla docs for this.
const h2 = document.createElement('h2')
h2.append('h2 text here')
document.querySelector('h1').insertAdjacentElement('afterend', h2)

// .removeChild() and .remove() work too
document.querySelector('b').remove()