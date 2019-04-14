import sys


def turn_left(d):
    if d == [1, 0]: return [0, 1]
    elif d == [-1, 0]: return [0, -1]
    elif d == [0, 1]: return [-1, 0]
    else: return [1, 0]


def clean(pos, d):
    global grid
    first_d = d
    for _ in range(4):
        d = turn_left(d)
        next_pos = [pos[0] + d[0], pos[1] + d[1]]
        if grid[next_pos[0]][next_pos[1]] == 0:
            grid[next_pos[0]][next_pos[1]] = 2
            clean([next_pos[0], next_pos[1]], d)
            return
    back_pos = [pos[0] - d[0], pos[1] - d[1]]
    if grid[back_pos[0]][back_pos[1]] != 1:
        grid[back_pos[0]][back_pos[1]] = 2
        clean(back_pos, d)


directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
read = sys.stdin.readline
n, m = map(int, read().split())
r, c, d = map(int, read().split())
d = directions[d]
grid = []
for _ in range(n):
    grid.append(list(map(int, read().split())))
grid[r][c] = 2
clean([r, c], d)
ans = 0
for line in grid:
    for x in line:
        if x == 2: ans += 1
print(ans)

