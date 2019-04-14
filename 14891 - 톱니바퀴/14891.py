import sys


def rotate(saw_idx, direction):
    global saws, rotated
    rotated[saw_idx] = True
    right = saws[saw_idx][2]
    left = saws[saw_idx][6]
    if direction == 1:
        saws[saw_idx].insert(0, saws[saw_idx].pop())
    else:
        saws[saw_idx].append(saws[saw_idx].pop(0))
    if saw_idx < 3:
        if saws[saw_idx+1][6] + right == 1 and not rotated[saw_idx+1]:
            rotate(saw_idx+1, direction*(-1))
    if saw_idx > 0:
        if saws[saw_idx-1][2] + left == 1 and not rotated[saw_idx-1]:
            rotate(saw_idx-1, direction*(-1))


read = sys.stdin.readline
saws = []
rotated = []
for _ in range(4):
    saws.append(list(map(int, list(read().strip()))))
k = int(read())
turned, directions = [], []
for _ in range(k):
    i, j = map(int, read().split())
    turned.append(i)
    directions.append(j)
for i in range(k):
    turned_idx = turned[i] - 1
    direction = directions[i]
    rotated = [False for _ in range(4)]
    rotate(turned_idx, direction)
ans = 0
if saws[0][0] == 1: ans += 1
if saws[1][0] == 1: ans += 2
if saws[2][0] == 1: ans += 4
if saws[3][0] == 1: ans += 8
print(ans)

