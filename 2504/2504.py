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

    def top2(self):
        return self.items[-2]


read = sys.stdin.readline
str = read().rstrip()
s = Stack()
l = len(str)
s.push(str[0])
for i in range(l-1):
    idx = i+1
    cur = str[idx]
    flag = 0
    if s.size == 0:
        s.push(cur)
    else:
        prev = s.top()
        if prev == '(' and cur == ')':
            s.pop()
            s.push(2)
            flag = 1
        elif prev == '[' and cur == ']':
            s.pop()
            s.push(3)
            flag = 1
        elif s.size > 1:
            if prev != '(' and prev != ')' and prev != '[' and prev != ']':
                if s.top2() == '(' and cur == ')':
                    x = prev * 2
                    s.pop()
                    s.pop()
                    s.push(x)
                    flag = 1
                elif s.top2() == '[' and cur == ']':
                    x = prev * 3
                    s.pop()
                    s.pop()
                    s.push(x)
                    flag = 1
        if flag == 0:
            s.push(cur)
        if s.size > 1:
            if s.top() != '(' and s.top() != ')' and s.top() != '[' and s.top() != ']' and s.top2() != '(' and s.top2() != ')' and s.top2() != '[' and s.top2() != ']':
                a = s.pop()
                b = s.pop()
                s.push(a+b)
if s.size == 1 and s.top() != '(' and s.top() != ')' and s.top() != '[' and s.top() != ']':
    print(s.top())
else:
    print(0)
