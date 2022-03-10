for (let i = 0; i < 10; i++) {
    console.log(i);
}

for (let i = 30; i >= 0; i -= 5) {
    console.log(i);
}

let a = [0, 1, 2];
for (let i = 0; i < a.length; i++) {
    console.log(a[i]);
}

// for of loop
for (let sub of a) {
    console.log(a);
}

// for in loop for objects
let o = { one: 1, two: 2 }
for (i in o) {
    console.log(i, o[i]);
}

// can also get Objects.keys(o), Object.values(o), Object.entries(o) (like .items())
// oh but this is weird, it's actually Object.keys(myObj)
// then loop through those

// while loops
let i = 0;
while (i < a.length) {
    console.log(i); // break also exists
    i++;
}