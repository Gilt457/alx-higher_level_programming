#!/usr/bin/node
const size = process.argv[2];

if (!Number.isInteger(Number(size))) {
  console.log('Missing size');
} else {
  Array.from({ length: size }, () => 'X'.repeat(size)).forEach(line => console.log(line));
}
