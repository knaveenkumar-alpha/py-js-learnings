/*
JavaScript though originally a prototype-based language, supports OOP concepts, including classes, Objects, Inheritance, Encapsulation, Polymorphism, and Abstraction.
1. Class: A Class is a blueprint for creating objects. It defines properties and methods that the objects created from the class will have.
   Object: An Object is an instance of a class. It can have properties (data) and Methods (functions) that operates on the data.
2. Inheritance:
    Inheritance allows one class to inherit properties and methods from another class, enabling code reuse and the creation of a class hierarchy.
3. Encapsulation: 
    Encapsulation is the bundling of data and methods that operate on the data within one unit, typically a class, restricting access to some
    of the objects components.
4. Polymorphism:
    Polymorphism allows objects of different classes to be treated as object of a common superclass. It enables the same method to behave 
    differently based on the object it is called on.
5. Abstraction:
    Abstraction hides the complex implementation details and exposes only the essential features of an object.
6. Prototype-based Inheritance:
    Java Script also supports prototype-based inheritance, where objects inherit properties and methods directly from other objects.
*/

console.log("======================== Class and Object ==============================")

class Car{
    constructor(brand, model){
        this.brand = brand;
        this.model = model;
    }

    start() {
        return (`${this.brand} model ${this.model} is starting.`)
    }
}

// Creating an object (instance) of the car class
const myCar = new Car("Toyota", "Corolla");
console.log(myCar.start());


class Bike {
	constructor(name, maker, engine) {
		this.name = name;
		this.maker = maker;
		this.engine = engine;
	}
	getDetails() {
		return (`The name of the bike is ${this.name}.`)
	}
}
// Making object with the help of the constructor
let bike1 = new Bike('Hayabusa', 'Suzuki', '1340cc');
let bike2 = new Bike('Ninja', 'Kawasaki', '998cc');

console.log(bike1.name); // Hayabusa
console.log(bike2.maker); // Kawasaki
console.log(bike1.getDetails());

// ===================================================================================== //
// Inheritance:
console.log("======================== Inheritance ==============================")

class Vehicle {
    constructor(type){
        this.type = type;
    }

    start(){
        console.log(`${this.type} is starting.`)
    }
}

class Car1 extends Vehicle {
    constructor(brand, model){
        super('Car');
        this.brand = brand;
        this.model = model;
    }

    displayInfo(){
        console.log(`This is a ${this.brand} ${this.model}.`)
    }
}

const myyCar = new Car1('Honda', 'Civic');
myyCar.start();         // Output: Car is starting.
myyCar.displayInfo();   // Output: This is a Honda Civic.

// ==================================================================================
//Encapsulation:
console.log("======================== Encapsulation ==============================")


class Person {
    constructor(name, age){
        this._name = name;
        this._age = age;
    }

    get name() {
        return this._name;
    }

    set age(newAge){
        if (newAge > 0) {
            this._age = newAge;
        } else {
            console.log('Age must be positive.');
        }
    }
}

const person = new Person("John", 30);
console.log(person.name);
person.age = -3;
// =====================================================================================
// Polymorphism:
console.log("======================== Polymorphism ==============================")

class Animal {
    speak() {
        console.log('Animal makes a sound.');
    }
}

class Dog extends Animal {
    speak(){
        console.log('Dog barks');
    }
}


class Cat extends Animal {
    speak() {
        console.log('Cat meows');
    }
}

const animals = [new Dog(), new Cat()];
animals.forEach(animal => {
    animal.speak();
})

// =====================================================================================
// Abstraction:
console.log("======================== Abstraction ==============================")


class CoffeeMachine {
    brewCoffee(type){
        this._boilwater();
            console.log(`Brewing ${type} coffee.`)
        }
    
    _boilwater() { // Private method conventionally marked with an underscore
        console.log('Boiling water....');
    }
    }


const machine = new CoffeeMachine();
machine.brewCoffee('Espresso');

// ======================================================================================
// Prototype-base inheritance:
console.log("======================== Prototype-based Inheritance ==============================")

const carr = {
    brand: "Ford",
    start() {
        console.log(`${this.brand} car is starting.`);
    }
};

const electricar = Object.create(carr);
electricar.start()
electricar.brand = "Tesla";
electricar.start();


