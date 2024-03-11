#!/usr/bin/node

// Define an object with a value and a method to increment it
class IncrementableObject {
  constructor() {
    this.type = 'object';
    this.value = 12;
  }

  incr() {
    this.value += 1;
  }
}

// Create an instance of the object and perform operations
const myObject = new IncrementableObject();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
