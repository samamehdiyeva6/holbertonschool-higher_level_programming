#!/usr/bin/node
let myObject1 = {
  type: 'object',
  value: 12
};
let myObject2 = {
  type: 'object',
  value: 12
  };
myObject2.value = 89;
console.log(myObject1);
console.log(myObject2);
