/*
Scope in JavaScript refers to the current context of execution, which determines the accessibility of 
variables, objects, and functions. In other words, scope controls where variables and functions are available 
for use in your code.

Types of Scope:

1. Global Scope: Variable declared outside of any function or block have global scope.
Global variables can be accessed from anywhere in the code.

2. Function Scope: Variable declared within a function are in function scope.
These variables are accessible only within that function and not outside.

3. Block Scope: Introduced in ES6, block scope applies to variable declared with 'let' and 'const'.
Variables declared inside a block (between '{}') are accessible only within that block.

4. Lexical Scope: Lexical scope means that a function's scope is detemined by where it is written in the code,
not where it is called. Inner function have access to the variables of their outer functions.

Closures:
Closures occur when a function is able to remember and access its lexical scope even when it is executed outside
of that scope.
A closure is created whenever a function is created within another function, and the inner function accesses the
variables of the outer function.
----------------------------------------------------------------------------------------------------------------------------
function outerFunction() {
    var outerVar = "I'm an outer variable";

    function innerFunction() {
        console.log(outerVar);
    }

    return innerFunction;
}

const myClosure = outerFunction();
myClosure(); // Output: I'm an outer variable
-----------------------------------------------------------------------------------------------------------------------------
In this example:

a. outerFunction creates a variable outerVar and an innerFunction.
b. The innerFunction has access to outerVar because of lexical scoping.
c. When outerFunction is called, it returns innerFunction, and the variable myClosure holds 
   the reference to innerFunction.
d. Even though outerFunction has finished execution, myClosure still has access to outerVar 
   because of the closure created by innerFunction.


Practical Use of Closures:
Closures are often used in situations where you need to maintain state between function calls,
  create private variables, or implement currying.
*/

// 1. Global Scope:

console.log('================== Global scope ====================')
var globalVar = "I'm a global variable";

function showGlobalVar() {
  console.log(globalVar);
}

showGlobalVar();

// 2. Function Scope:
console.log('================== Function scope ==================')
function myFunc() {
  var localVar = 'I am a local variable';
  console.log(localVar);
}

myFunc();
// console.log("Access the variable defined in the function: " + localVar); // ReferenceError: localVar is not defined

// 3. Block Scope:

if (true) {
  let blockVar = "I'm a block-scoped variable";
  console.log(blockVar); // Accessible here
}

// ReferenceError: blockVar is not defined
// console.log(blockVar); // Error: blockVar is not defined

// 4. Lexical scope:

function outerFunction() {
  var outerVar = "I'm an outer variable";

  function innerFunction() {
      console.log(outerVar); // Accessible here
  }

  innerFunction(); // Output: I'm an outer variable
}

outerFunction();

// ========================================================================================
// Closures:

/*
Practical Use of Closures:
Closures are often used in situations where you need to maintain state between function calls, create private variables, or implement currying.
*/
function counter() {
  let count = 0;

  return function() {
      count++;
      return count;
  };
}

const increment = counter();
console.log(increment()); // Output: 1
console.log(increment()); // Output: 2
console.log(increment()); // Output: 3
