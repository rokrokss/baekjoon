import sys


def check_destinations(cnt):
    global grid, ans, h, n
    for i in range(n):
        dest = i
        for j in range(h):
            if dest > 0 and grid[j][dest-1]:
                dest -= 1
            elif dest < n-1 and grid[j][dest]:
                dest += 1
        if dest != i:
            return False
    return True


def check(cnt, idx):
    global ans, grid, unconnected, n
    if cnt > 3 or cnt >= ans:
        return
    if check_destinations(cnt):
        ans = min(ans, cnt)
        return
    if cnt >= ans - 1:
        return
    while idx != len(unconnected):
        if unconnected[idx][1] > 0 and grid[unconnected[idx][0]][unconnected[idx][1]-1]:
            idx += 1
            continue
        if unconnected[idx][1] < n-2 and grid[unconnected[idx][0]][unconnected[idx][1]+1]:
            idx += 1
            continue
        grid[unconnected[idx][0]][unconnected[idx][1]] = True
        idx += 1
        check(cnt+1, idx)
        grid[unconnected[idx-1][0]][unconnected[idx-1][1]] = False


read = sys.stdin.readline
n, m, h = map(int, read().split())
grid = [[False for _ in range(n-1)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, read().split())
    grid[a-1][b-1] = True
unconnected = []
for i in range(h):
    for j in range(n-1):
        if not grid[i][j]:
            unconnected.append([i, j])
ans = 4
check(0, 0)
if ans < 4: print(ans)
else: print(-1)

