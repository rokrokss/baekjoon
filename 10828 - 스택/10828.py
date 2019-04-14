import sys
read = sys.stdin.readline
t = int(read())
s = []
size = 0
for _ in range(t):
    command = read().split()
    if command[0] == 'push':
        n = int(command[1])
        s.append(n)
        size += 1
    elif command[0] == 'top':
        if size == 0:
            print(-1)
        else:
            print(s[-1])
    elif command[0] == 'size':
        print(size)
    elif command[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(s.pop())
            size -= 1
    elif command[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
