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
for _ in range(t):
    str = read()
    s = Stack()
    l = len(str)
    s.push(str[0])
    for i in range(l-2):
        idx = i+1
        cur = str[idx]
        if s.isEmpty():
            prev = '0'
        else:
            prev = s.top()
        if prev == '(' and cur == ')':
            s.pop()
        else:
            s.push(cur)
    if s.isEmpty():
        print('YES')
    else:
        print('NO')
