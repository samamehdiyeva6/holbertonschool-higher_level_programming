#!/usr/bin/node
const list = process.argv.slice(2);
let max = Number(list[0]);
for (let i = 1; i < list.length; i++) {
  if (max < Number(list[i])) {
    max = Number(list[i]);
  }
}
console.log(max);
