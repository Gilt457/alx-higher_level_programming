#!/usr/bin/node
const num1 = process.argv[2];
const num2 = process.argv[3];

const sum = (x, y) => parseInt(x) + parseInt(y);

console.log(`The sum is: ${sum(num1, num2)}`);
