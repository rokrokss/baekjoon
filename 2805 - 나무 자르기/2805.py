import sys


read = sys.stdin.readline
n, m = map(int, read().split())
trees = list(map(int, read().split()))
max_h = max(trees)
left, right = 0, max_h - 1
ans = 0
while left <= right:
    mid = (left + right) // 2
    total = sum(t - mid for t in trees if t > mid)
    if total >= m:
        if mid > ans: ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)

