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
    this.size = 0;
  }

  is_empty() {
    return !this.head;
  }

  enqueue(item) {
    let tmp = this.tail;
    this.tail = new Node(item);
    if (this.is_empty()) {
      this.head = this.tail;
    } else {
      tmp.next = this.tail;
    }
    this.size++;
  }

  dequeue() {
    let tmp = this.head;
    this.head = tmp.next;
    this.size--;
    return tmp;
  }

  get_size() {
    return this.size;
  }
}


const bfs = (miro, n, m) => {
  const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  let q = new Queue();
  let visited = Array(n);
  let result = 1;
  for (let i = 0; i < n; i++) {
    visited[i] = Array(m).fill(false);
  }
  q.enqueue([0, 0]);
  visited[0][0] = true;
  while(!q.is_empty()) {
    let size = q.get_size();
    for (let _ = 0; _ < size; _++) {
      let cur = q.dequeue();
      if (cur.data[0] === n - 1 && cur.data[1] === m - 1) {
        return result;
      }
      for (let i = 0; i < directions.length; i++) {
        let next = [cur.data[0] + directions[i][0], cur.data[1] + directions[i][1]];
        if (next[0] < 0 || next[0] >= n || next[1] < 0 || next[1] >= m) {
          continue;
        }
        if (visited[next[0]][next[1]]) {
          continue;
        }
        if (miro[next[0]][next[1]] === 0) {
          continue;
        }
        q.enqueue(next);
        visited[next[0]][next[1]] = true;
      }
    }
    result++;
  }
};
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input[0].split(' ').map(x => {return Number(x)});
let miro = Array(n);
for (let i = 0; i < n; i++) {
  miro[i] = input[i + 1].split('').map(x => {return Number(x)});
}
console.log(bfs(miro, n, m));

