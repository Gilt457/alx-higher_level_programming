#!/usr/bin/node
const arg = process.argv[2];
const num = Number(arg);

if (Number.isNaN(num)) {
  console.error('Missing number of occurrences');
} else {
  Array.from({ length: num }, () => console.log('C is fun'));
}
