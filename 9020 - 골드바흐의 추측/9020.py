import math
import sys
read = sys.stdin.readline
root = math.sqrt(10000)
arr = list(range(0, 10001))
arr[0] = 0
arr[1] = 0
arr[2] = 2
i = 2
while i <= root:
    if arr[i] == 0:
        i += 1
        continue
    for j in range(i+i, 10001, i):
        arr[j] = 0
    i += 1
t = int(read())
for _ in range(t):
    a = 0
    b = 0
    n = int(read())
    i = 0
    while i <= n/2:
        if arr[i] != 0 and arr[n - i] != 0:
            a = i
            b = n - i
        i += 1
    print(str(a) + ' ' + str(b))
