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
    if (a1[i1][1] < a2[i2][1] || (a1[i1][1] === a2[i2][1] && a1[i1][0] < a2[i2][0])) {
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


let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input.shift());
let arr = mergesort(input.map(x => {return x.split(' ').map(y => {return Number(y)})}));
arr = mergesort(arr);
let ans = 0;
let taken = 0;
for (let i = 0; i < n; i++) {
  let [start, end] = arr[i];
  if (start < taken) {
    continue;
  }
  taken = end;
  ans++;
}
console.log(ans);

