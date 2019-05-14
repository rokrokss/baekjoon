class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}


class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
  }
  
  isEmpty() {
    return !this.head;
  }

  enqueue(data) {
    let tmp = this.tail;
    this.tail = new Node(data);
    if (this.isEmpty()) {
      this.head = this.tail;
    } else {
      tmp.next = this.tail;
    }
  }

  dequeue() {
    let tmp = this.head;
    this.head = tmp.next;
    return tmp;
  }
}


let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let N = input[0].trim();
let NLen = N.length;
N = parseInt(N);
let M = parseInt(input[1]);
let btns = Array(10);
for (let i = 0; i < 10; i++)
  btns[i] = 1;
if (M) {
  let broken = input[2].toString().split(' ');
  for (let i = 0; i < broken.length; i++)
    btns[broken[i]] = 0;
}
let ans = Math.min(Math.abs(100 - N));
let q = new Queue();
if (btns[0])
  ans = Math.min(ans, N + 1);
for (let i = 1; i < btns.length; i++) {
  if (btns[i]) {
    if (btns[0])
      ans = Math.min(ans, i * (10 ** NLen) - N + NLen + 1);
    else {
      let tmp = 0;
      for (let j = 0; j <= NLen; j++) {
        tmp += i * (10 ** j);
      }
      ans = Math.min(ans, tmp - N + NLen + 1);
    }
    break;
  }
}
if (NLen > 1) {
  for (let i = btns.length - 1; i > 0; i--) {
    if (btns[i]) {
      let tmp = 0;
      for (let j = 0; j < NLen - 1; j++) {
        tmp += i * (10 ** j);
      }
      ans = Math.min(ans, Math.abs(tmp - N) + NLen - 1);
      break;
    }
  }
}
for (let i = 1; i < btns.length; i++)
  if (btns[i])
    q.enqueue(i.toString());
while (!q.isEmpty()) {
  let data = q.dequeue().data;
  if (data.length == NLen) {
    ans = Math.min(ans, Math.abs(parseInt(data) - N) + parseInt(data).toString().length);
    continue;
  }
  for (let i = 0; i < btns.length; i++)
    if (btns[i])
      q.enqueue(data + i.toString());
}
console.log(ans);

