var input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
var e = Number(input[0]), s = Number(input[1]), m = Number(input[2]);
var a = b = c = i = 0;
while (true) {
  i++; a++; b++; c++;
  if (a > 15) a -= 15;
  if (b > 28) b -= 28;
  if (c > 19) c -= 19;
  if (a === e && b === s && c === m) {
    console.log(i);
    break;
  }
}

