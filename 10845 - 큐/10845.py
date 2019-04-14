import sys


class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.items.pop()

    def size(self):
        return self.size

    def front(self):
        return self.items[-1]

    def back(self):
        return self.items[0]


read = sys.stdin.readline
t = int(read())
q = Queue()
for _ in range(t):
    str = read().rstrip()
    strArr = str.split()
    command = strArr[0]
    if command == 'push':
        q.enqueue(int(strArr[1]))
    elif command == 'pop':
        if q.isEmpty():
            print(-1)
        else:
            print(q.dequeue())
    elif command == 'size':
        print(q.size)
    elif command == 'empty':
        if q.isEmpty():
            print(1)
        else:
            print(0)
    elif command == 'front':
        if q.isEmpty():
            print(-1)
        else:
            print(q.front())
    else:
        if q.isEmpty():
            print(-1)
        else:
            print(q.back())

