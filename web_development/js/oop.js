// this seems easier, and is what VS recommends
class Color {
    constructor(r, g, b) {
        this.r = r;
        this.g = g;
        this.b = b;
    }
    // define methods here to automatically put them in prototype
    rgb = () => `rgb(${this.r}, ${this.g}, ${this.b})`
}

const myColor = new Color(0, 0, 0) // need new for each instance

// extends, like inheritance
class extendedColor extends Color {
    // super keyword used to reference the parent class's constructor
    // useful for adding new attrs to the parent constructor
    // const newColor = new extendsColor(0, 0, 0, 'newAttr')
    constructor(newAttr) {
        super(r, g, b);
        this.newAttr = newAttr;
    }
    myMethod() { console.log('here') };
}



// everything below this will probably be used infrequently
// constructor functions & new keyword
function Color(r, g, b) {
    this.r = r;
    this.g = g;
    this.b = b;
}

// define methods to prototype object outside of function def?
Color.prototype.rgb = function () {
    const { r, g, b } = this;
    return `rgb(${r}, ${g}, ${b})`;
}

// use new keyword to sort of like instantiate it like an __init__ ?
const newColor = new Color(0, 0, 0);


// factory function, less common
function makeClass(p1, p2) {
    const myObj = {
        para1: p1,
        para2: p2,
    };
    myObj.myMethod = () => {
        console.log(this.myObj.para1);
    }
    return myObj;
}


// prototype property in object, reference to a "blueprint object"
// typically contains methods for every instance of that object

String.prototype.yell = () => {
    return this.toUpperCase()
} // this will now add yell() method to all strings