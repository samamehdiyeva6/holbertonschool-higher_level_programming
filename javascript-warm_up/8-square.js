#!/usr/bin/node
const size = process.argv.slice(2);
const num = Number(size);
let res = '';
if (Number.isInteger(num)) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
        res += 'X';
    }
    console.log(res);
    res = '';
  }
} else {
    console.log('Missing size');
}
