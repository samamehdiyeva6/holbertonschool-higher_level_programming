#!/usr/bin/node
const list = process.argv.slice(2).map(Number);
list((a,b) => b - a);
console.log(list[1]);
