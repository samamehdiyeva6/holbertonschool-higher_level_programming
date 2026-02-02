#!/usr/bin/node
const x = process.argv.slice(2);
const num = Number(x) || 'Missing number of occurrences';
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
