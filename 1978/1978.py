import math
N = int(input())
cnt = 0
arr = input().split()
for i in range(N):
    n = int(arr[i])
    if n%2 == 0:
        if n == 2:
            cnt += 1
    else:
        j=3
        root = math.sqrt(n)
        f = 0
        while True:
            if n == 1:
                f = 1
                break
            if j > root:
                break
            if n%j==0:
                f = 1
                break
            else:
                j += 2
        if f == 0:
            cnt += 1
print(cnt)
