#!/usr/bin/node
let n = parseInt(process.argv[2]);
for (n; n > 0; n--) {
  console.log('C is fun');
}
if (Number.isNaN(n)) {
  console.log('Missing number of occurences');
}
