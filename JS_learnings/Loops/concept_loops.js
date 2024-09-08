/* 
For Loop: The for loop is used for iterating over a block of code a certain number of times
          or over the elements of an array. Here’s a basic example:

syntax: 
    for (initialExpression; condition; updateExpression) {
    // Loop body
}

*/
for (let i=0; i<5; i++) {
    console.log("Hello world!")
}
console.log("===================== loops ====================")

const fruits = ["Apple", "Banana", "Cherry", "Mango", "Guava"]
for (let i=0; i < fruits.length; i++){
    console.log(fruits[i])
}

console.log("===================== Nested loops ====================")
for (let i=0; i < 3; i++) {
    for (let j=0; j<2; j++) {
        console.log(`i = ${i}, j = ${j}`)
    }
}

console.log("===================== Sum of Natural Numbers using loops ====================")

let sum = 0;
const n = 100;
for (let i=1; i <= n; i++) {
    sum += i;
}

console.log(`Sum of ${n} Natural number: ${sum}`)

/* 
While Loop:
    while loop is a fundamental construct that repeatedly executes a block of code as long as
    a specified condition evaluates to true. Here’s how it works:

Syntax:
    while (condition) {
    // Code to execute while the condition is true
}
Explanation:
1. The condition is evaluated before each iteration.
2. If the condition is true, the code inside the loop runs.
3. The loop continues until the condition becomes false.
Be cautious: If the condition never becomes false, the loop will run indefinitely, 
potentially crashing your browser.
*/
console.log("================ While loops ====================================")
let i = 0;
while (i<10){
    console.log("The number is " + i);
    i++;
}

/*
Do While Loop:
    1. A variant of the while loop is the do... while loop. It executes the code block once before
    checking the condition.
    2. If the condition is true, it repeats the loop.

Syntax:
    do {
    // block of code before condition.
    }
    while (condition) {
        //body 
    }
*/
console.log("===================== Do While loop ==============================")

let j = 0;
do {
    console.log("The number is " + j);
    j++;
} while (j<10);




