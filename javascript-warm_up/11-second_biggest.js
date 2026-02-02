#!/usr/bin/node
const list = Number(process.argv.slice(2));
let max = list[0];
for (let i = 1; i < list.length; i++) {
  if (max < list[i]) {
    max = list[i];
  }
}
console.log(max);
