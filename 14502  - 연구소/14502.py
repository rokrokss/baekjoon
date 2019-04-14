import sys
import itertools


def infection(grid):
    new_infection = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==2:
                if i < n-1 and grid[i+1][j]==0: new_infection.append([i+1, j])
                if j < m-1 and grid[i][j+1]==0: new_infection.append([i, j+1])
                if i > 0 and grid[i-1][j]==0: new_infection.append([i-1, j])
                if j > 0 and grid[i][j-1]==0: new_infection.append([i, j-1])
    if not new_infection:
        return grid
    else:
        for pos in new_infection:
            grid[pos[0]][pos[1]] = 2
        return infection(grid)


def findsubsets(arr, n):
    return list(itertools.combinations(arr, n))


read = sys.stdin.readline
n, m = map(int, read().split())
grid = []
spaces = []
ans = 0
for _ in range(n):
    grid.append(list(map(int, read().split())))
for i in range(n):
    for j in range(m):
        if grid[i][j]==0:
            spaces.append([i, j])
for walls in findsubsets(spaces, 3):
    tmp_grid = [grid[i][:] for i in range(n)]
    for wall in walls:
        tmp_grid[wall[0]][wall[1]] = 1
    tmp_grid = infection(tmp_grid)
    tmp_spaces = 0
    for line in tmp_grid:
        for item in line:
            if item == 0:
                tmp_spaces += 1
    if tmp_spaces > ans:
        ans = tmp_spaces
print(ans)

