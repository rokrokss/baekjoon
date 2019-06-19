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

  enqueue(node) {
    let tmp = this.tail;
    this.tail = node;
    if (this.isEmpty())
      this.head = this.tail;
    else
      tmp.next = this.tail;
  }

  dequeue() {
    let tmp = this.head;
    this.head = tmp.next;
    tmp.next = null;
    return tmp;
  }
}


let input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
const [N, K] = input.map(x => { return parseInt(x); });
const Q = new Queue();
for (let i = 1; i <= N; i++)
  Q.enqueue(new Node(i));
let answer = '';
while (!Q.isEmpty()) {
   for (let i = 0; i < K - 1; i++)
     Q.enqueue(Q.dequeue());
  if (answer)
    answer += ', ';
   answer += Q.dequeue().data;
}
console.log('<' + answer + '>');

