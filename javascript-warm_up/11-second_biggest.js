#!/usr/bin/node
const list = process.argv.slice(2);
const sorted = list.reverse();
console.log(Number(sorted[1]));
