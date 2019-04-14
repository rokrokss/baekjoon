import math
import sys
read = sys.stdin.readline
mn = read().split()
m = int(mn[0])
n = int(mn[1])
for i in range(m, n+1):
    if i%2 == 0:
        if i == 2:
            print(i)
    else:
        j = 3
        root = math.sqrt(i)
        f = 0
        while True:
            if i == 1:
                f = 1
                break
            if j > root:
                break
            if i%j==0:
                f = 1
                break
            else:
                j += 2
        if f == 0:
            print(i)
