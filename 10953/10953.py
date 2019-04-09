import sys


read = sys.stdin.readline
t = int(read())
for _ in range(t):
    ab = [int(x) for x in read().split(',')]
    print(ab[0] + ab[1])

