// in-line comment 
console.log("Hello World!");
console.log("Hello from JavaScript");
/* this is a multiple line 
comments
here*/

// Date Types and Variables
// undefined, null, boolean, string, symbol, number, and object.
var myName = "Naveen";
myName = 56;
let ourCollegeName = "FreeCodeCamp";
const pi = 3.14;
console.log(pi)

// Storing Values with Assigment Operators
var a;
var b = 2;
console.log(a)
a = 4;
b = a
console.log(a)

// Initializing Variables assignment Operator
var a = 9;

// Uninitialized variables
var a = 5;
var b = 10;
var c = "I'm a "

a = a+1;
b = b+5;
c = c+"string!"

// Case sensitivity in Variables
var StUdLyCapVaR;
var properCamelCase;
var TitleCaseOver;

/*STUDLYCAPVAR = 10;
ProperCAmelCAse = "A string"
tITLEcASEoVER = 1000;
*/

// Arthimatic Operations
var a = 10;
console.log(a)
a = a + 2
console.log(a)

var diff = 8 - 5;
console.log(diff)

var prod = 8*9;

var div = 89/5;

var increment = 85;
increment = increment + 1;
increment++;

var decr = 89;
decr--;

var rem;
rem = 45%2;

// Compounding assigment 
var q = 2;
var p = 4;
console.log(p, q)
q += 3;
p += 6;
console.log(p, q)

var a = 3;
var b = 4;
console.log(a, b)
a -= 1;
b -= 3;
console.log(a, b)

var s = 3;
console.log(s);
s *= 3;
console.log(s);

var x = 7;
console.log(x);
x /= 3;
console.log(x)

// Declare string Variables
var firstName = "Naveen";
var lastName = "Kumar";

var myFirstName = "Kuruva"

// Escaping Literal Quotes in string.
var myStr = "I am a \"double quoted\" string inside \"double quotes"
console.log(myStr)

// Quoting solutions with single quotes.
var adjection = "asesome"

console.log(myStr.length)

// slicing of array and string:
// string indexing starts with 0
var firstName = "Naveen Kumar"
console.log(firstName[1])
console.log(firstName[-1])

// String are Immutable
var mySt = "Jello World";
mySt[0] = "H"
console.log(mySt)

// functions
function wordBlanks(Noun, adj, verb, adverb){
  var result = "";
  result = "The " + adj + " " + Noun + " " + verb + " to the store " + adverb + "." 
  return result;
}

console.log(wordBlanks("dog", "big", "ran", "quickly"))

// Arrays is mutable object in JS
var arr = ["Naveen", 45]
console.log("Array: ", arr)
var myArr = [["string", 12, 25.5], [5,6]]
var array = [25,58,60];
console.log(array);
array[0] = 50;
console.log(array);
// multiple indexing in arrays
var a = [[1,2,3], [4,5,6], [7,8,9]];
console.log(a)
var data = a[0][2]
console.log(data)

// Manupulate Arrays with Push()
var arr = ["Naveen", "Kumar", "Lion"]
console.log(arr)
arr.push(["Happy", "Joy"])
console.log(arr)
var Arr = [2,4,6]
var rem = Arr.pop()
console.log(Arr, rem)
// shift() in array
var aa = [1,2,3]
var shf = aa.shift()
console.log(aa, shf)
console.log(aa.unshift(85));
// functions
function reuseFunc(){
  console.log("Hey! Naveen, How you doing?")
};
reuseFunc();
reuseFunc();

// Passing Values to Function with Arguments
function func(a=8, b=3){
  console.log(a-b);
};
func(78,5);
func();
// Global Scope and Functions
var myGlobal = 10;
function func1(){
  oopsGlobal = 5
}

function func2(){
  var output = "";
  if (typeof myGlobal != "undefined") {
    output += "myGlobal: " + myGlobal;
  }
  if (typeof oopGlobal != "undefined") {
    output += "oopGlobal: " + oopGlobal;
  }
  console.log(output);
}

func1();
func2();

//Local Scope and Functions
function myLocalFunc(){
  var myVar = 3; 
  console.log(myVar);
};
myLocalFunc();
// console.log(myVar);  ReferenceError: myVar is not defined 
//Global vs Local scope in functions
var outer = "T-shirt";
function myOutfit(){
  var outer = "Sweater"
  return outer;
}
console.log(myOutfit());
console.log(outer);
// Return a Value from a Function with Return
function func(num){
  return num-3;
};
console.log(func(78));
function timeFive(num){
  return num * 5
};
console.log(timeFive(52))
// Understanding Undefined Values Returned From a Function
var sum = 0;
function addThree(){
  sum += 3
};
console.log(addThree())
// Assignment with a Returned Value
var changed = 0;
function change(num){
  return (num + 5) / 3;
};
changed = change(10);
console.log(changed)
var processed = 0;
function processArg(num){
  return (num + 3)    / 5;
};
processed = processArg(22)
console.log(processed)

// Stand in line
function nextInLine(arr, item){
  arr.push(item);
  return arr.shift();
};

var arr = [1,2,3,4,5];
console.log("Before: " + JSON.stringify(arr));
console.log(nextInLine(arr, 6));
console.log("After: " + JSON.stringify(arr));

// Boolean Values
function welcomeToBoolean(){
  return false; // true
};

// Use conditional Logic with If Statement
function ourTrueOrFalse(isItTrue){
  if (isItTrue){
    return "Yes, it's true.";
  }
  return "No, it's false.";
}

function trueOrFalse(wasThatTrue){
  if (wasThatTrue){
    return "Yes, that was true."
  }
  return "No, that was false."
}

console.log(ourTrueOrFalse(true));
console.log(trueOrFalse(false));

// Comparison with the Equality Operator
function testEqual(val){
  if (val == 12){
    return "Equal to 12."
  }
  return "Not Equal to 12."
}

console.log(testEqual(10));

// Comparison with the Strict Equality Operator
/* 
2==2 equality operator
3===3 strict equality operator which give true.
3==='3' which will give false.
*/
function testStrict(val){
  if (val === 7){
    return "Strictly Equal."
  }
  return "Not Equal."
}

console.log(testStrict(7))
console.log(testStrict('7'))

// Practice Comparing Different Values
/*
== Equality operator 
=== strict equality operator
!= Not equality operator
!== Strictly not equality operator.
*/
// Comparison with the Logical and Operator
/*
> greater than 
< less than
>= greater equal than
<= less equal than
*/
function testLogical(val){
  if (val <= 50 && val >= 25){
    return "Yes, it's there in between 25 to 50";
  } else if (val > 10 && val < 20){
    return "Yes, it's there in between 10 to 20";
  }
  else{
    return "Yes,It's between 0 and 10"
  }
}

console.log(testLogical(26))
console.log(testLogical(15))
console.log(testLogical(4))
// Logical Order in If else statements
// we have to concentrated on order of conditions.
function orderMyLogic(val){
  if (val < 5){
    return "Less than 5";
  }
  else if (val<10){
    return "Less than 10";
  }
  else {
    return "Greater than or equal to 10";
  }
}

console.log(orderMyLogic(5));

//Chaining If else statements
// same as above

// Switch Statements
function caseInSwitch(val){
  var answer = "";
  switch(val){
    case 1:
      answer = "Alpha";
      break;
    case 2:
      answer = "Beta";
      break;
    case 3:
      answer = "Gamma";
      break;
    case 4:
      answer = "Delta";
      break;
  }
  return answer;
}

console.log(caseInSwitch(1));

// multiple Identical Options in Switch Statements

function caseInSwitchMul(val){
    var answer = "";
    switch(val){
      case 1:
      case 2:
        answer = "Alpha";
        break;
      case 3:
      case 4:
        answer = "Beta";
        break;
      case 5:
        answer = "Gamma";
        break;
      case 6:
        answer = "Delta";
        break;
    }
    return answer;
  }
  
  console.log(caseInSwitch(1));

// JS Objects
var dog = {
    "name": "Camper",
    "legs": 4,
    "tails": 1,
    "friends": ["everythings"]
};

console.log(dog.name)
console.log(dog['tails'])

