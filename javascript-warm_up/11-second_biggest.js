#!/usr/bin/node
const list = process.argv.slice(2).map(Number);
const sorted = list.sort();
const reversed = sorted.reverse();
console.log(reversed[1]);
