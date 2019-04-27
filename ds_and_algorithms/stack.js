var Stack = function() {
  this.top = null;
};

var Node = function(data) {
  this.data = data;
  this.previous = null;
};

Stack.prototype.is_empty = function() {
  return !this.top;
};

Stack.prototype.push = function(data) {
  var node = new Node(data);
  node.previous = this.top;
  this.top = node;
};

Stack.prototype.pop = function() {
  if (this.is_empty()) {
    console.log("Stack is Empty!");
    return null;
  } else {
    tmp = this.top;
    this.top = this.top.previous;
    return tmp;
  }
};

var s = new Stack();
s.push(3);
s.push(12);
s.push(123);
s.pop();
s.push(111);
var cur = s.top;
while (cur) {
  console.log(cur.data);
  cur = cur.previous;
}

