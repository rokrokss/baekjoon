import sys


def solution(n, m):
    global memo
    if memo[n][m]: return memo[n][m]
    ans = 0
    for i in range(n-1, m):
        ans += solution(n-1, i)
    memo[n][m] = ans
    return ans


read = sys.stdin.readline
memo = [[0 for _ in range(30)] for _ in range(30)]
for i in range(30):
    memo[0][i] = i+1
t = int(read())
for _ in range(t):
    n, m = map(int, read().split())
    n -= 1
    m -= 1
    print(solution(n, m))
