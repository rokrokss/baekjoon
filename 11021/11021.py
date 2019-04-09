import sys


read = sys.stdin.readline
t = int(read())
for i in range(t):
    ab = [int(x) for x in read().split()]
    print("Case #{}: {}".format(i+1, ab[0]+ab[1]))

