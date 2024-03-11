#!/usr/bin/node
const main = () => {
  const numbers = getNumbersFromArgs();
  if (numbers.length < 2) {
    console.log(0);
    return;
  }
  const secondLargest = findSecondLargest(numbers);
  console.log(secondLargest);
};

const getNumbersFromArgs = () => {
  return process.argv.slice(2).map(Number).filter(n => !isNaN(n));
};

const findSecondLargest = (numbers) => {
  numbers.sort((x, y) => x - y);
  return numbers[numbers.length - 2];
};

main();
