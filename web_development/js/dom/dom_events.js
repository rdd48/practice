// addEventListener()
// events listed on MDN: https://developer.mozilla.org/en-US/docs/Web/Events
const btn1 = document.querySelector('#button_id_1');
// first param is a type of event, second is a function (without parens if defined earlier)
btn1.addEventListener('click', () => alert('clicked!'));
btn1.addEventListener('clicked once only', () => console.log('only once!'), { once: true })
// btn1.addEventListener('mouseup', () => alert('clicked!'));

// random color generator exercise
const randomizeColor = () => {
    let rColor = Math.floor(Math.random() * 255);
    let gColor = Math.floor(Math.random() * 255);
    let bColor = Math.floor(Math.random() * 255);
    return `rgb(${rColor},${gColor},${bColor})`

}

// use a this statement if you want
function colorize() {
    this.style.backgroundColor = randomizeColor();
}

const btnColorR = document.querySelector('#randomize_color');
btnColorR.addEventListener('click', colorize);

// event parameter
document.querySelector('button').addEventListener('click', function (evt) {
    // adding a parameter gives us access to info about the event
    console.log(evt.clientX) // tells us the X-coord
})

document.querySelector('input').addEventListener('keydown', (evt) => {
    console.log(evt.code); // shows code on computer
})

// form event listeners
const form = document.querySelector('#my_form');
const newItem = document.querySelector('#new_item');
form.addEventListener('submit', function (e) {
    e.preventDefault(); // prevents default behavior, e.g. form going to new page
    const newLi = document.createElement('li');
    newLi.innerText = newItem.value;
    document.querySelector('ul').appendChild(newLi); // could use .append(newLi) here too
    //console.log(new_item.value);
})

// do something when input is changed using 'input' argument
// can also try 'change' which is when you click out
const changedForm = document.querySelector('#changed');
changedForm.addEventListener('input', () => { console.log(changedForm.value) })

const btn2 = document.querySelector('#button_id_2');
// btn.onclick = function () { console.log('i was clicked!') }
btn2.onclick = () => { console.log('i was clicked!') }
btn2.onmouseenter = () => { console.log('i was moused over') }

// event propagation: when you click execute a child element, this can execute the parents
// use evt.stopPropagation() in your addEventListener function arg.
// evt.target can tell us the child of the parent that is clicked on (or interacted with in other ways)