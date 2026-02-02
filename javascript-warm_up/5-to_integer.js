#!/usr/bin/node
const args = process.argv.slice(2);
if (Number.isInteger(Number(args[0]))) {
  console.log('My number: ' + args[0]);
} else {
    console.log('Not a number');
}
