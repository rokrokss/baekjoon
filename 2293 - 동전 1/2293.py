import sys

read = sys.stdin.readline
n, k = map(int, read().split())
dp = [0] * (k + 1)
dp[0] = 1
for _ in range(n):
    coin = int(read())
    for j in range(1, k + 1):
        if coin <= j:
            dp[j] += dp[j - coin]
print(dp[k])

