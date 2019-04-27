var Queue = function() {
  this.head = null;
  this.tail = null;
};

var Node = function(data) {
  this.data = data;
  this.next = null;
};

Queue.prototype.is_empty = function() {
  return !this.head;
};

Queue.prototype.enqueue = function(data) {
  var tmp = this.tail
  this.tail = new Node(data);
  if (this.is_empty()) {
    this.head = this.tail;
  } else {
    tmp.next = this.tail;
  }
};

Queue.prototype.dequeue = function() {
  var tmp = this.head;
  this.head = tmp.next;
  return tmp;
};

var PriorityQueue = function() {};
PriorityQueue.prototype = Object.create(Queue.prototype);
PriorityQueue.prototype.enqueue = function(data) {
  var node = new Node(data);
  if (this.is_empty()) {
    this.head = node;
  } else {
    if (data < this.head.data) {
      node.next = this.head;
      this.head = node;
      return;
    }
    var cur = this.head;
    while (cur.next) {
      if (cur.data < data && data < cur.next.data) {
        node.next = cur.next;
        break;
      }
      cur = cur.next;
    }
    cur.next = node;
  }
};

var dfs = function(v, adj, visited) {
  process.stdout.write((v + 1).toString() + ' ');
  visited[v] = true;
  var cur = adj[v].head;
  while (cur) {
    if (!visited[cur.data]) {
      dfs(cur.data, adj, visited);
    }
    cur = cur.next;
  }
};

var bfs = function (v, adj, visited) {
  var q = new Queue();
  q.enqueue(v);
  visited[v] = true;
  while (!q.is_empty()) {
    var u = q.dequeue().data;
    process.stdout.write((u + 1).toString() + ' ');
    var cur = adj[u].head;
    while (cur) {
      if (!visited[cur.data]) {
        q.enqueue(cur.data);
        visited[cur.data] = true;
      }
      cur = cur.next;
    }
  }
};

var input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
var nmv = input[0].split(' ').map(function(x) {return Number(x)});
var n = nmv[0], m = nmv[1], v = nmv[2] - 1;
var adj = [];
var visited = [];
for (var i = 0; i < n; i++) {
  adj.push(new PriorityQueue());
  visited[i] = false;
}
for (var i = 1; i <= m; i++) {
  var ab = input[i].split(' ').map(function(x) {return Number(x) - 1});
  adj[ab[0]].enqueue(ab[1]);
  adj[ab[1]].enqueue(ab[0]);
}
dfs(v, adj, visited);
process.stdout.write('\n');
for (var i = 0; i < n; i++) {
  visited[i] = false;
}
bfs(v, adj, visited);
process.stdout.write('\n');

