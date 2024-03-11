#!/usr/bin/node
const computeFactorial = num => {
  if (num < 0) return -1;
  if (num === 0 || isNaN(num)) return 1;
  return num * computeFactorial(num - 1);
};

const numberToCalculate = Number(process.argv[2]);
console.log(computeFactorial(numberToCalculate));
