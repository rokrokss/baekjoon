class Node {
  constructor(priority, target) {
    this.priority = priority;
    this.target = target;
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

  enqueue(p, t) {
    let tmp = this.tail;
    this.tail = new Node(p, t);
    if (this.isEmpty()) {
      this.head = this.tail;
    } else {
      tmp.next = this.tail;
    }
  }

  dequeue() {
    let tmp = this.head;
    let tmptmp = tmp.next;
    while(tmptmp) {
      if (tmptmp.priority > tmp.priority) {
        this.head = this.head.next;
        this.enqueue(tmp.priority, tmp.target);
        tmp = this.head;
        tmptmp = tmp.next;
      } else {
        tmptmp = tmptmp.next;
      }
    }
    this.head = tmp.next;
    return tmp;
  }
}


let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let T = parseInt(input[0]);
for (let i = 0; i < T; i++) {
  let [N, M] = input[2*i + 1].split(' ').map(x => {return parseInt(x);});
  let arr = input[2*i + 2].split(' ').map(x => {return parseInt(x);});
  let Q = new Queue();
  for (let j = 0; j < arr.length; j++) {
    Q.enqueue(arr[j], (j === M) ? true : false);
  }
  for (let j = 1; j <= arr.length; j++) {
    if (Q.dequeue().target)
      console.log(j);
  }
}

