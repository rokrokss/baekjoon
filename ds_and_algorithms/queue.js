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
  var tmp = this.tail;
  this.tail = new Node(data);
  if (this.is_empty()) {
    this.head = this.tail;
  } else {
    tmp.next = this.tail;
  }
};

Queue.prototype.dequeue = function() {
  if (this.is_empty()) {
    console.log("Queue is empty!");
    return null;
  } else {
    var tmp = this.head;
    this.head = tmp.next;
    return tmp
  }
  return tmp;
};

var q = new Queue();
q.enqueue(10);
q.enqueue(2);
q.enqueue(12);
q.enqueue(1324);
q.dequeue();
q.dequeue();
q.enqueue(111);
var curr = q.head;
while (curr) {
  console.log(curr.data);
  curr = curr.next;
}

