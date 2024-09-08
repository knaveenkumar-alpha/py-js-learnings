/*
Exception handling in JavaScript is done using the try...catch statement, which allows you to handle errors gracefully without breaking the execution of your code.
This is especially useful for catching runtime errors and handling them in a controlled manner.

Syntax:
======
try {
    // Code that may throw an error
} catch (error) {
    // Code to handle the error
} finally {
    // Code that will run regardless of whether an error occurred or not
}

1. try block: Contains the code that may throw an exception.
2. catch block: Contains the code that will be executed if an exception occurs in the try block.
3. finally block: (Optional) Contains the code that will always be executed after the try and catch blocks,
   regardless of whether an exception was thrown or not.


*/

console.log("====================== Basic Exception handling ========================================")
try {
    let res = 10/0;
    console.log("result: ", res);
    console.log(a)
} catch (err) {
    console.error("An Error occurred: ", err.message);
} finally {
    console.log("This will always execute.");
}
// ===========================================================================================

console.log("====================== Handling Specific Error ========================================")

try {
    let jsonString = '{"name": "navin", "age":29}';
    let user = JSON.parse(jsonString);
    console.log(user.name);

    let badJsonString = '{"name": "navin", "age":}';
    let badUser = JSON.parse(badJsonString);
} catch (err) {
    if (err instanceof SyntaxError) {
        console.error("Json Parsing Error: ", err.message)
    } else {
        console.error("An Unexpected error occurred:", err.message)
    }
} finally {
    console.log("this code will execute always.")
}

console.log("====================== Custom Error Throwing ========================================")

function divide(a,b) {
    if (b == 0) {
        throw new Error("Division by zero is not allowed.");
    }
    return a/b;
}

try {
    let res = divide(18, 0);
    console.log("Result: ", res);
} catch (err) {
    // console.log("Error: ", err.message)
    console.error("Error occurred: ", err.message)
} finally {
    console.log("This will execute always.")
}

console.log("====================== Nested try catch exception handling ========================================")

try {
    try {
        let res = someUndefinedFunc();
    } catch (error) {
        console.error("Inner catch: ", error.message)
        throw new Error("Re-throwing the error.")
    }
} catch (err) {
    console.error("Outer catch: ", err.message)
}
/* 
Explanation:
===========
An error occurs in the inner try block because someUndefinedFunction is not defined.
The inner catch block catches the error, logs it, and then re-throws a new error.
The outer catch block catches this new error and handles it.

Summary:
=======
1. try...catch: Basic structure for handling exceptions.
2. finally: Used for code that should run regardless of whether an exception occurred or not.
3. Custom errors: You can throw custom errors using throw.
4. Error types: Use instanceof to handle specific types of errors differently.

*/

