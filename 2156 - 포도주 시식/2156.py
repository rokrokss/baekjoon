import sys


read = sys.stdin.readline
n = int(read())
wines = [int(read()) for _ in range(n)]
memo = [0 for _ in range(n)]
try:
    memo[0] = wines[0]
    memo[1] = wines[0] + wines[1]
    memo[2] = max(memo[1], wines[1] + wines[2], wines[0] + wines[2])
except:
    pass
if n <= 3:
    print(memo[n-1])
else:
    for i in range(3, n):
        memo[i] = max(memo[i-3] + wines[i-1] + wines[i],
                      memo[i-2] + wines[i],
                      memo[i-1])
    print(memo[n-1])

