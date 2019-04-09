import sys


def dfs(pos, count):
    global visited, directions, grid, n, m
    score = 0
    if count >= 5:
        return score
    for direction in directions:
        nx = pos[0] + direction[0]
        ny = pos[1] + direction[1]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                score = max(score, grid[pos[0]][pos[1]] + dfs([nx, ny], count + 1))
                visited[nx][ny] = False
    return score


def potato(pos):
    global grid
    score = 0
    x, y = pos[0], pos[1]
    if x < n-1 and y < m-2: # ㅗㅜ
        score = max(score, grid[x][y+1] + grid[x+1][y] + grid[x+1][y+1] + grid[x+1][y+2])
        score = max(score, grid[x][y] + grid[x][y+1] + grid[x][y+2] + grid[x+1][y+1])
    if x < n-2 and y < m-1: # ㅏㅓ
        score = max(score, grid[x][y] + grid[x+1][y] + grid[x+2][y] + grid[x+1][y+1])
        score = max(score, grid[x][y+1] + grid[x+1][y+1] + grid[x+2][y+1] + grid[x+1][y])
    return score


read = sys.stdin.readline
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n, m = map(int, read().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, read().split())))
visited = [[False for _ in range(m)]for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        ans = max(ans, dfs([i, j], 1))
        ans = max(ans, potato([i, j]))
        visited[i][j] = False
print(ans)

