const unknown1 = 'foo';
console.log(typeof unknown1); // Output: string

// variables
// let, const for declaring. let only needed during declaration, not reassigment
let myVar = 1;
// bools are lowercase e.g. true, false
// str slicing still exists e.g myStr[0]
// get len with myStr.length
// str methods (go to MDN for full list), e.g. like myStr.toUpperCase()
// .trim() is like .strip()
// .indexOf(subStr) like index() but also if/in, returns -1 if arg not in str
// slicing through .splice() method e.g. myStr.splice(0,5). one num e.g. myStr.splice(5) like [5:]
// .replace() exists,
// .indexOf('str') -> returns -1 if not present

// template literals use `` and ${foo} (like f formatting)
// need `` not ''
// Math object has values (Math.pi) and methods (Math.round())
// Math.pow(2, 3) -> 8

// == vs ===
// == doesn't care if same type, e.g. 1 == '1' -> true (? wow)
// === is probably what i'll want to use, also !==
// alert() and prompt () create browser alerts or prompts
let input = prompt('enter your prompt');
alert('alert!');

// parseInt() like int()

// if/elses
if (myVar === 3) {
    console.log('here');
} else if (myVar === 4) {
    console.log('there');
} else {
    console.log('finally');
}

// && is and, || is or, ! is not
// switch
switch (myVar) {
    case 1:
        console.log(`myVar is 1`);
    case 2:
        console.log(`myVar is 2`)
    default:
        console.log(`this is like the "else"`);
}

// arrays
let a = [1, 2, 3]
a.length
// push/pop add/remove at end, unshift/shift add/remove at start
a.push(4);
a.push(5, 6); // also works
a.pop() // returns & removes 6
a.unshift(0);
let b = [7, 8]
combo = a.concat(b);
a.includes(1) // returns true
// also have .indexOf(), which again returns -1 if not present
// a.reverse() works in place
a.slice(1, 3); // works like python slicing
// splice: second arg is "delete count", i.e. how many curr items to delete @ idx
a.splice(2, 0, 'new'); // adds 'new' str add index 2, doesn't delete anything
a.splice(5, 1); // removes & returns the 5th list element
a.sort(); // defaults by converting everything into strings (? annoying)

// object literals. all keys are converted to strs
const d = { var1: 'first', var2: 'second' } // etc
d['var1'] // -> 'first'. Note how var1 didn't have quotes above but has quotes here?
d.var1 // also -> 'first

// try/catch like try/except
try { a } catch { console.log('a not defined!') }

// destructing objects
const [firstEl, secondEl, allElse] = a; // firstEl = 1, secondEl = 2, allElse = [3]
const { var1 } = d; // creates a new variable called var1 from d.var1

// belowcreates new variables named newVarName, newVarName2 from d.var1 & d.var2
const { var1: newVarName, var2: newVarName2 = 'defaultVal' } = d
// works for func parameters when obj is passed in (i.e., this works with myFuncObjDestruct(d))
const myFuncObjDestruct = ({ var1, var2 }) => (var1, var2)
