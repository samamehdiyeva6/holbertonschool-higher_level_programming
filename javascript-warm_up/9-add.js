#!/usr/bin/node
function add(a, b){
    return a + b;
}
const a = Number(process.argv.slice(2)[0]);
const b = Number(process.argv.slice(2)[1]);
console.log(add(a, b));
