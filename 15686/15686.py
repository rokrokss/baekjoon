import sys


def check_chicken_distance(chickens):
    global houses, n
    chicken_distance = 0
    for house in houses:
        min_distance = 2*n
        for chicken in chickens:
            distance = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
            min_distance = min(min_distance, distance)
        chicken_distance += min_distance
    return chicken_distance


def dfs(left, idx, picked_chickens):
    global grid, houses, chickens, ans
    if not left:
        chicken_d = check_chicken_distance(picked_chickens)
        ans = min(ans, chicken_d)
        return
    while left != 0 and idx < len(chickens):
        pc = picked_chickens[:]
        pc.append(chickens[idx])
        idx += 1
        dfs(left-1, idx, pc)


read = sys.stdin.readline
n, m = map(int, read().split())
grid = []
houses = []
chickens = []
for _ in range(n):
    grid.append(list(map(int, read().split())))
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            houses.append([i, j])
        elif grid[i][j] == 2:
            chickens.append([i, j])
ans = 2*n*len(houses)
dfs(m, 0, [])
print(ans)

