#!/usr/bin/node
const argumentCount = process.argv.length;

const argumentMessage = argumentCount > 2 ? `Argument${argumentCount > 3 ? 's' : ''} found` : 'No argument';
console.log(argumentMessage);
