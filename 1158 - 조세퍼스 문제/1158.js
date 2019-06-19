function solution(N, K) {
  let answer = '';
  const circleArray = Array(N);
  let head = 0;
  for (let i = 0; i < N; i++) {
    circleArray[i] = (i + 1);
  }
  while (circleArray.length > 0) {
    head += K - 1;
    head %= circleArray.length;
    if (answer)
      answer += ', ';
    answer += circleArray[head];
    circleArray.splice(head, 1);
  }
  return '<' + answer + '>';
}

const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
console.log(solution(parseInt(input[0]), parseInt(input[1])));

