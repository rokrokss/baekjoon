function mergesort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  let mid = parseInt(arr.length / 2);
  let a1 = mergesort(arr.slice(0, mid));
  let a2 = mergesort(arr.slice(mid));
  let i1 = 0;
  let i2 = 0;
  let ia = 0;
  while (i1 < a1.length && i2 < a2.length) {
    if (a1[i1] < a2[i2]) {
      arr[ia] = a1[i1];
      i1++;
    } else {
      arr[ia] = a2[i2];
      i2++;
    }
    ia++;
  }
  while (i1 < a1.length) {
    arr[ia] = a1[i1];
    i1++;
    ia++;
  }
  while (i2 < a2.length) {
    arr[ia] = a2[i2];
    i2++;
    ia++;
  }
  return arr;
}


let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')[1].split(' ').map(x => {return Number(x);});
input = mergesort(input);
let ans = 0;
for (let i = 0; i < input.length; i++) {
  ans += input[i] * (i - (input.length - 1 - i));
}
console.log(ans + ans);

