#!/usr/bin/env node
const arg = process.argv.slice(2)[0];

if (isNaN(Number(arg))) {
  console.error('Missing number of occurrences');
} else {
  Array.from({ length: Number(arg) }, () => console.log('C is fun'));
}
