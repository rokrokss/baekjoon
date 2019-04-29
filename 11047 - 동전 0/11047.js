class Stack {
  constructor() {
    this.items = [];
  }

  isEmpty() {
    return !this.items;
  }

  enqueue(item) {
    this.items.push(item);
  }

  dequeue() {
    return this.items.pop();
  }

  top() {
    return this.items[-1];
  }
}


const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [n, k] = input[0].split(' ').map(x => {return Number(x);});
let s = new Stack();
for (let i = 1; i <= n; i++) {
  let coin = Number(input[i]);
  if (coin <= k) {
    s.enqueue(coin);
  }
}
let ans = 0;
while (k) {
  let coin = s.dequeue();
  let a = parseInt(k / coin);
  k -= a * coin;
  ans += a;
}
console.log(ans);

