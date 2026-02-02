#!/usr/bin/node
const size = process.argv.slice(2);
const num = Number(size) || 'Missing size';
for (let i = 0; i < size; i++) {
    for (let j = 0; j < size;j++) {
      console.log('X');
    }
    console.log('\n')
}
