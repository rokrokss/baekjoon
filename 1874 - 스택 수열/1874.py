import sys


class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop()

    def size(self):
        return self.size

    def top(self):
        return self.items[-1]


read = sys.stdin.readline
t = int(read())
s = Stack()
s.push(0)
result = []
flag = 0
item = 1
for _ in range(t):
    n = int(read())
    top = s.top()
    if n >= item:
        for i in range(n-item+1):
            s.push(item)
            item += 1
            result.append('+')
    elif top != n:
        flag = 1
    _ = s.pop()
    result.append('-')
if flag == 1:
    print("NO")
else:
    for i in range(len(result)):
        print(result[i])
