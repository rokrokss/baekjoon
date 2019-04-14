import sys


def power_gap(team_a, team_b):
    global ans, grid, n
    if len(team_a) == n//2:
        gap = 0
        for i in range(n//2):
            for j in range(n//2):
                gap += grid[team_a[i]][team_a[j]] - grid[team_b[i]][team_b[j]]
        gap = abs(gap)
        if ans > gap: ans = gap
    else:
        for i in range(len(team_b)):
            if team_b[i] > team_a[-1]:
                tmp_team_b = team_b[:]
                to_a = tmp_team_b.pop(i)
                power_gap(team_a + [to_a], tmp_team_b)


read = sys.stdin.readline
n = int(read())
ans = 100 * n
grid = []
for _ in range(n):
    grid.append(list(map(int, read().split())))
gap = power_gap([0], list(range(n))[1:])
print(ans)

