/*
-----------------------------------------------------------------------------------------------
Data Type |	Description	                                       | Example                       | 
-----------------------------------------------------------------------------------------------
String	  | Textual data.	                                   | 'hello', "hello world!", etc. |
Number	  | An integer or a floating-point number.	           | 3, 3.234, 3e-2, etc.          |
BigInt	  | An integer with arbitrary precision.	           | 900719925124740999n, 1n, etc. |
Boolean	  | Any of two values: true or false.	               | true and false                |
undefined | A data type whose variable is not initialized.     |	let a;                     |
null	  | Denotes a null value.	                           | let a = null;                 |
Symbol	  | A data type whose instances are unique and immutable.|	let value = Symbol('hello');|
Object	  | Key-value pairs of collection of data.	             | let student = {name: "John"};|
------------------------------------------------------------------------------------------------

Note: JavaScript data types are divided into primitive and non-primitive types.

Primitive Data Types: They can hold a single simple value. String, Number, BigInt, Boolean, undefined, null,
    and Symbol are primitive data types.
Non-Primitive Data Types: They can hold multiple values. Objects are non-primitive data types.
*/
/*
JavaScript has several built-in data types that are essential for handling different kinds of data. 
Each data type comes with its own set of methods that make it easier to manipulate data. Below is a 
detailed list of JavaScript's built-in data types and their commonly used methods, along with examples.
*/
// JavaScript Built-in Data Types:

// 1. Number: The 'Number' type represents both integer and floating-point numbers.
/*
 Common Methods:
 --------------
 a. 'toFixed()' : Formats a number to a specified number of decimal places.
 b. 'toString()' : Coverts a number to a string.
 c. 'parseInt()' : Parses a string and returns an integer.
 d. 'parseFloat()' : Parses a string and returns a floating-point number.
 */
console.log("======================= Number Methods ========================")
let num = 1235.568269469;
console.log("Method toFixed(): " + num.toFixed(2));
console.log(`Method toString(): ${num.toString()} and type of object: ${typeof(num.toString())}`);
console.log("Number method parseInt(): ", Number.parseInt("120"), "and typeof of object: ", typeof(Number.parseInt("120")));
console.log("Number method parseFloat(): ", Number.parseFloat("120.25"), "and typeof of object: ", typeof(Number.parseFloat("120.25")));

// 2. String: Strings are used to represent text. They are immutable.
/*
Common Methods:
a. 'chartAt()' : Returns the character at a specified index.
b. 'concat()' : Joins two or more strings.
c. 'includes()' : Checks if a string contains a specified value.
d. 'indexOf()' : Returns the position of the first occurrence of a specified value.
e. 'slice()' : Extracts a part of a string and returns a new string.
f. 'toLowerCase()' : Converts a string to lowercase.
g. 'toUpperCase()' : Converts a string to Uppercase.
h. 'trim()' : Removes whitespace from both ends of string.
*/
console.log("======================= String Methods ========================");
let str = "Hello, World!";
console.log("Method 'charAt(1)': ", str.charAt(1));
console.log("Method 'concat()': ", str.concat(" How are you?"));
console.log("Method 'includes()': ", str.includes("World"));
console.log("Method 'indexOf()': ", str.indexOf("o"));
console.log("Method 'slice(7, 12)': ", str.slice(7, 12));
console.log("Method 'toLowerCase()': ", str.toLocaleLowerCase());
console.log("Method 'toUpperCase()': ", str.toUpperCase());
console.log("Method 'trim()': ", "   _Trim this _   ".trim());
// at() methods
let text = "Hello, World!";
let char = text.at(-4);
console.log(char);
let sq_char = text[-2];
console.log(sq_char);
console.log(text.charAt())

// 3. Boolean: Booleans represent logical values: 'true' or 'false'.
console.log("======================= Boolean ========================");
let isAvailable = true;

console.log(isAvailable);
console.log(typeof isAvailable);

// 4. Array: Arrays are used to store multiple values in a single variable. It is Mutable datatype in JS.
/*
push():      Adds new items to the end of an array.                py/ append()
pop():       Removes the last item of an array.
shift():     Removes the first item of an array.
unshift():   Adds new items to the beginning of an array.
concat():    Joins two or more arrays.                             py/ extend()
slice():     Selects a part of an array and returns a new array.   py/ []
splice():    Adds/removes items to/from an array.
forEach():   Calls a function for each array element.              py/ list iterable object.
map():       Creates a new array by performing a function on each array element.
filter():    Creates a new array with all elements that pass a test.
reduce():    Reduces the array to a single value.
*/

let arr = [1,2,3,4,5];
arr.push(6);
console.log(arr) // [1, 2, 3, 4, 5, 6]
arr.pop(); // [1, 2, 3, 4, 5]
arr.shift(); // [2, 3, 4, 5]
arr.unshift(1); // [1, 2, 3, 4, 5]
let newArr = arr.concat([6, 7]); // [1, 2, 3, 4, 5, 6, 7]
let slicedArr = arr.slice(1, 3); // [2, 3]
arr.splice(2, 1); // [1, 2, 4, 5]
// console.log("After splice method: arr.splice(2, 2)", arr.splice(2, 2)) // [1, 2, 5]

arr.forEach(function(item) {
    console.log(item*2); // Logs each item
});

let mappedArr = arr.map(item => item * 2); // [2, 4, 8, 10]
let filteredArr = arr.filter(item => item > 2); // [4, 5]
let reducedValue = arr.reduce((accumulator, currentValue) => accumulator + currentValue, 0); // 12
