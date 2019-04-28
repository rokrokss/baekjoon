function arrayMax(arr) {
  let len = arr.length;
  let max = -Infinity;
  while (--len) {
    if (arr[len] > max) {
      max = arr[len];
    }
  }
  return max;
}


function solution(n, memo) {
  if (memo[n]) {
    return memo[n];
  }
  let ans = solution(n - 1, memo) + solution(n - 2, memo) + solution(n - 3, memo);
  memo[n] = ans;
  return ans;
}


const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const t = Number(input[0]);
const ns = Array(t)
for (let i = 0; i < t; i++) {
  ns[i] = Number(input[i + 1]);
}
let memo = Array(arrayMax(ns) + 1).fill(0);
memo[1] = 1;
memo[2] = 2;
memo[3] = 4;
for (let i = 0; i < t; i++) {
  console.log(solution(ns[i], memo));
}

