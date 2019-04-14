import math
import sys
read = sys.stdin.readline
m = int(read())
n = int(read())
min = 10000
sum = 0
p = 0
for i in range(m, n+1):
    if i%2 == 0:
        if i == 2:
            p = 1
            sum += 2
            if min > i:
                min = i
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
            p = 1
            sum += i
            if min > i:
                min = i
if p==1:
    print(sum)
    print(min)
else:
    print(-1)