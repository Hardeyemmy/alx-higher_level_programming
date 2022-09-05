#!/usr/bin/node
// Prints a specified string only if the first argument can be converted to an integer

const integer = parseInt(process.argv[2]);
if (integer) {
  console.log('My number: ' + integer);
} else {
  console.log('Not a number');
}
