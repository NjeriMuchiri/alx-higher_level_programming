#!/usr/bin/node
const square = parseInt(process.argv[2]);
if (Number.isNaN(square)) {
  console.log('Missing size');
} else {
  let i = 0;
  let s;
  while (i < square) {
    i++;
    s = '';
    let j = 0;
    while (j < square) {
      j++;
      s += 'X';
    }
    console.log(s);
  }
}
