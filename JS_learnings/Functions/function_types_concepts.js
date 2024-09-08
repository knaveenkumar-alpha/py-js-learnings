/*
JavaScript functions can be categorized in various ways based on how they are defined, how they behave, and
how they are used. Here are some of the main types of functions in JavaScript with examples:
1. Function Declaration: A function declaration defines a named function that can be called anywhere in the 
scope where it is defined.
2. Function Expression: A function expression defines a function as part of an expression. It can be named or anonymous.
3. Arrow Function: Arrow functions provides a shorter syntax for writing functions. They are always anonymous and don't
have their own 'this' context.
4. Immediately Invoked Function Expression (IIFE): An IIFE is a function that is executed immediately after it is defined.
It's commonly used to create a new scope and avoid polluting the global namespace.
5. Higher-Order Function: A higher-order function is a function that takes another function as an argument, or returns
a function as a result.
6. Callback Function: A Callback function is a function passed into another function as an argument, which is then invoked
inside the outer function to complete some action.
7. Recursive Function: A Recursive function is a function that calls itself until it reaches a base condition.
8. Generator Function: A generator function is a special type of function that can be paused and resumed, using the 'yield'
keyword. It's denoted by an asterisk('*') after the 'function' keyword.
9. Asynchronous Function (Async/Await): An Async function is a function that returns a 'promise', and 'await' is used to
wait for the promise to resolve.
10. Constructor Function: A constructor function is used to create objects. When called with the 'new' keyword, it creates
a new object and assigns 'this' to the newly created object.

These are some of the primary types of functions in JavaScript, each with its own use cases and characteristics. 
Understanding these will help you write more flexible and powerful JavaScript code.
*/

// 1. Function Declaration:
function greet(name){
    return "Hello, " + name + "!";
};

console.log(greet("Naveen")); // output: Hello, Naveen!

// 2. Function Expression:
const greet1 = function(name){
    return "Hello, " + name + "!";
};

console.log(greet1("Bob")); // output: Hello, Bob!

// 3. Arrow Function:
const greet2 = (name) => `Hello, ${name}!`;
console.log(greet2("Dave"));
// Arrow fucntion with multiple parameters and a block body
const add = (a, b) => {
    return a+b;
};
console.log(add(2,4));

// 4. IIFE (Immediately Invoked Function Expression)
(function() {
    console.log("This is an IIFE");
}) ();
// IIFE with parameters
(function(name) {
    console.log("Hello, " + name + "!");
}) ("Eve");

// 5. Higher Order function:
function higherOrderFunc(callback) {
    return callback();
};

function sayHello() {
    return "Hello world!";
};
console.log(higherOrderFunc(sayHello));

// 6. Callback Functions:
function fetchData(callback) {
    setTimeout(() => {
        callback("Data Fetched");
    }, 1000);
}

function handleData(data) {
    console.log(data);
}
fetchData(handleData); // Output after 1 second: Data fetched

// 7. Recursive Function:
function factorial(n) {
    if (n==0) {
        return 1;
    } else {
        return n * factorial(n-1);
    }
}

console.log(factorial(5));

// 8. Generator Function:
function* generatorSequence() {
    yield 1;
    yield 2;
    yield 3;
};

const gene = generatorSequence();
console.log(gene.next().value);
console.log(gene.next().value);
console.log(gene.next().value);
// second version:

function* generatorSeq() {
    const arr = [1,2,3,4,5,6]
    for(let i=0; i<arr.length; i++) {
        yield i;
    }
};

const gen = generatorSeq();
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);

// 9. Asynchronous Function (Async/Await):
// async function fetchData1() {
//     const resp = await fetch("https://api.example.com/data");
//     const data = await resp.json();
//     return data;
// };

// fetchData1().then(data => console.log(data));

// 10. Constructor Function:
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    };

    displayInfo() {
        console.log("Person: " + this.name + " and age: " + this.age)
    };
};
const navn = new Person("Naveen", 30);
navn.displayInfo();

// second way:
function Person1(name, age) {
    this.name = name;
    this.age = age;
}

const person = new Person("Frank", 32);
console.log(person.name);