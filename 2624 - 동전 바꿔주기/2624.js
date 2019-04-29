function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}


function _solution(coins, t, idx, memo) {
  if (t === 0) {
    return 1;
  }
  if (idx >= coins.length) {
    return 0;
  }
  if (memo[t][idx] != -1) {
    return memo[t][idx];
  }
  let result = 0;
  let tt = t;
  for (let i = 0; i <= coins[idx][1] && t >= 0; i++) {
    result += _solution(coins, t, idx + 1, memo);
    t -= coins[idx][0];
  }
  memo[tt][idx] = result;
  return result;
}


function solution(coins, t, k) {
  let memo = Array(t + 1);
  for (let i = 0; i < t + 1; i++) {
    memo[i] = Array(k);
    for (let j = 0; j < k; j++) {
      memo[i][j] = -1;
    }
  }
  return _solution(coins, t, 0, memo);
}


const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let t = Number(input[0]);
let k = Number(input[1]);
let coins = Array(k);
for (let i = 0; i < k; i++) {
  coins[i] = input[i + 2].split(' ').map(x => {return Number(x);});
}
console.log(solution(coins, t, k));

