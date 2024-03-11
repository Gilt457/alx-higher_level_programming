#!/usr/bin/node
// Store the number of command-line arguments
const argumentCount = process.argv.length;

// Check if there are any additional arguments provided
const hasArguments = argumentCount > 2;
const message = hasArguments
  ? `Argument${argumentCount > 3 ? 's' : ''} found`
  : 'No argument';

// Output the appropriate message
console.log(message);
