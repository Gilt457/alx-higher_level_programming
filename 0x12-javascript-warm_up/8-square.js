#!/usr/bin/node
const size = process.argv[2];
const squareChar = 'X';

function printSquare(dimension) {
  if (!parseInt(dimension)) {
    console.log('Missing size');
    return;
  }
  const line = squareChar.repeat(dimension);
  for (let i = 0; i < dimension; i++) {
    console.log(line);
  }
}

printSquare(size);
