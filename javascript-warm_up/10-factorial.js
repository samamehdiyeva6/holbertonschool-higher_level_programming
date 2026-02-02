#!/usr/bin/node
function factorial(a) {
  if (a === 0) {
    return 1;
  } else if (a === 1) {
    return 1;
  } else {
    return factorial(a) * factorial(a-1);
  }
}
const a = Number(process.argv.slice(2));
console.log(factorial(a));
