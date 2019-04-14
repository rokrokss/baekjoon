import sys


class Camera():
    def __init__(self, pos, num):
        self.pos = pos
        self.num = num


def copy_grid(grid):
    return [xgrid[:] for xgrid in grid]


def check_cam(pos, direction, grid):
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= n or pos[1] >= m:
        return
    num = grid[pos[0]][pos[1]]
    if num == 0:
        grid[pos[0]][pos[1]] = 9
    elif num == 6: return
    check_cam([pos[0]+direction[0], pos[1]+direction[1]], direction, grid)


def check(pos, direction_set, grid, idx):
    for directions in direction_set:
        tmp_grid = copy_grid(grid)
        for direction in directions:
            check_cam(pos, direction, tmp_grid)
        change_camera(idx+1, tmp_grid)


def change_camera(idx, grid):
    global ans, cameras, n, m
    if idx == len(cameras):
        spaces = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    spaces += 1
        ans = min(ans, spaces)
        return
    tmp_grid = copy_grid(grid)
    cam = cameras[idx]
    if cam.num == 1:
        check(cam.pos, [[[1, 0]], [[-1, 0]], [[0, 1]], [[0, -1]]], grid, idx)
    elif cam.num == 2:
        check(cam.pos, [[[1, 0], [-1, 0]], [[0, 1], [0, -1]]], grid, idx)
    elif cam.num == 3:
        check(cam.pos, [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]]], grid, idx)
    elif cam.num == 4:
        check(cam.pos, [[[-1, 0], [0, 1], [0, -1]], [[1, 0], [0, 1], [0, -1]], [[1, 0], [-1, 0], [0, -1]], [[1, 0], [-1, 0], [0, 1]]], grid, idx)
    elif cam.num == 5:
        check(cam.pos, [[[1, 0], [-1, 0], [0, -1], [0, 1]]], grid, idx)


read = sys.stdin.readline
n, m = map(int, read().split())
ans = n * m
grid = []
cameras = []
for _ in range(n):
    grid.append(list(map(int, read().split())))
for i in range(n):
    for j in range(m):
        if grid[i][j] != 0 and grid[i][j] != 6:
            cameras.append(Camera([i, j], grid[i][j]))
change_camera(0, grid)
print(ans)

