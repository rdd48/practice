// diff ways to define a function
function addFunc(x, y) { return x + y }

const addFunc = function (x, y) { return x + y }

// arrow funcs, but no internet explorer support
const addFunc2 = (x, y) => { return x + y }
const oneParamFuncSquare = x => { return x ** 2 }
const noReturnNeeded = x => x ** 2 // use () after => for multiline funcs

// default params
const addFuncDefaults = (x = 1, y = 2) => x + y

// pass funcs as args
function callTwice(func) {
    for (let i = 0; i < 2; i++) { func() }
}
callTwice(addFunc);

// methods
const myObj = {
    x = 1,
    y = 2,
    addFunc: function (x, y) { return x + y },
    addFuncThis() { return this.x + this.y },
    // if you use arrow functions, stay consistent (? something about where it refers)
    // this keyword behaves differently in arrow functions
}

myObj.addFunc(0, 2) // returns 2
myObj.addFuncThis() // returns 3

// forEach, kind of like a for/of loop
a = [0, 1, 2, 3, 4]
a.forEach(function (el) { console.log(el + 1) })

// map generates new array like python
const aPlusOne = a.map(function (el) { return el + 1 })
const aPlusOne = a.map(el => el + 1)

// filter generates new array from logic
const odds = a.filter(n => n % 2 === 1)

// some() checks if some elements pass test, every() if all elements pass test
a.some(el => el >= 3) // returns true
a.every(el => el >= 3) // returns false

// reduce() takes a func with two params that are an accumulator and a curr value
a.reduce((sum, curr) => sum + curr) // gets sum
a.reduce((min, curr) => {
    if (curr < min) { return curr } else { return min }
})

// setTimeout() takes a function and time (ms) as arg
setTimeout(addFunc(1, 1), 3000) // prints 2 after 3 sec
// setInterval() does the same thing constantly after given intervals
const id = setInterval(() => console.log(Math.random()), 2000) // prints random vals every 2 s
clearInterval(id) // stops setInterval

// spread char "..." unpacks arrays
console.log(...a) // prints all values separately
aCopy = [...a] // copies into new array
aOddsDup = [...a, ...odds]
myObjDup = { ...myObj } // if combining two obj with same key, will just keep last val

// arguments object available in all funcs but not an array
// so we need rest (...) operator, kinda like *args
const sumAll = (...nums) => nums.reduce((sum, curr) => sum + curr)