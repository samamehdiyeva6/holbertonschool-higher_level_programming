#!/usr/bin/node
const list = process.argv.slice(2);
const sorted = list.sort();
const reversed = sorted.reverse();
console.log(Number(reversed[1]));
