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

  is_empty() {
    return !this.head;
  }

  enqueue(data) {
    let tmp = this.tail
    this.tail = new Node(data);
    if (this.is_empty()) {
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


class PriorityQueue extends Queue {
  enqueue(data) {
    let node = new Node(data);
    if (this.is_empty()) {
      this.head = node;
    } else {
      if (data < this.head.data) {
        node.next = this.head;
        this.head = node;
        return;
      }
      let cur = this.head;
      while (cur.next) {
        if (cur.data < data && data < cur.next.data) {
          node.next = cur.next;
          break;
        }
        cur = cur.next;
      }
      cur.next = node;
    }
  }
}


let dfs = (v, adj, visited) => {
  process.stdout.write((v + 1).toString() + ' ');
  visited[v] = true;
  let cur = adj[v].head;
  while (cur) {
    if (!visited[cur.data]) {
      dfs(cur.data, adj, visited);
    }
    cur = cur.next;
  }
};
let bfs = (v, adj, visited) => {
  let q = new Queue();
  q.enqueue(v);
  visited[v] = true;
  while (!q.is_empty()) {
    let u = q.dequeue().data;
    process.stdout.write((u + 1).toString() + ' ');
    let cur = adj[u].head;
    while (cur) {
      if (!visited[cur.data]) {
        q.enqueue(cur.data);
        visited[cur.data] = true;
      }
      cur = cur.next;
    }
  }
};
let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [n, m, v] = input[0].split(' ').map(x => {return Number(x)}); v--;
let adj = Array(n);
let visited = Array(n);
for (var i = 0; i < n; i++) {
  adj[i] = new PriorityQueue();
  visited[i] = false;
}
for (let i = 1; i <= m; i++) {
  let [a, b] = input[i].split(' ').map(x => {return Number(x) - 1});
  adj[a].enqueue(b);
  adj[b].enqueue(a);
}
dfs(v, adj, visited);
process.stdout.write('\n');
for (var i = 0; i < n; i++) {
  visited[i] = false;
}
bfs(v, adj, visited);
process.stdout.write('\n');

