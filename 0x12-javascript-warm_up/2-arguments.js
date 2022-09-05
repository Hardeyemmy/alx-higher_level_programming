#!/usr/bin/node
// Prints a message depending on number of arguments passed
const argc = process.argv.length;
if (argc > 3) {
  console.log('Arguments found');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}

