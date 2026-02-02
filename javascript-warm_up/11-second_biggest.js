#!/usr/bin/node
const list = process.argv.slice(2);
const sorted = list.sort();
console.log(Number(sorted[-2]));
