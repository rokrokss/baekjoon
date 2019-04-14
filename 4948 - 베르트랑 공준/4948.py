import math
import sys
read = sys.stdin.readline
n = 0
cnt = 0
root = math.sqrt(246913)
arr = list(range(0, 246915))
arr[0] = 0
arr[1] = 0
arr[2] = 2
i = 2
while i <= root:
    if arr[i] == 0:
        i += 1
        continue
    for j in range(i+i, 246914, i):
        arr[j] = 0
    i += 1
while True:
    n = int(read())
    if n == 0:
        break
    for j in range(n+1, 2*n+1):
        if arr[j] != 0:
            cnt += 1
    print(cnt)
    cnt = 0
