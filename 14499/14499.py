import sys


def move_dice(dice, cmd):
    if cmd == 1:      # E
        dice = [dice[0], dice[5], dice[1], dice[2], dice[4], dice[3]]
    elif cmd == 2:    # W
        dice = [dice[0], dice[2], dice[3], dice[5], dice[4], dice[1]]
    elif cmd == 3:    # N
        dice = [dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]]
    else:   # S
        dice = [dice[5], dice[1], dice[0], dice[3], dice[2], dice[4]]
    return dice


read = sys.stdin.readline
n, m, x, y, k = [int(x) for x in read().split()]
grid = []
for i in range(n):
    grid.append([int(x) for x in read().split()])
cmds = [int(x) for x in read().split()]
dice = [0, 0, 0, 0, 0, 0]
for cmd in cmds:
    if (cmd==4 and x==n-1) or (cmd==3 and x==0) or (cmd==2 and y==0) or (cmd==1 and y==m-1):
        continue
    if cmd==4: x+=1
    elif cmd==3: x-=1
    elif cmd==2: y-=1
    else: y+=1
    dice = move_dice(dice, cmd)
    print(dice[2])
    if grid[x][y]==0:
        grid[x][y] = dice[5]
    else:
        dice[5] = grid[x][y]
        grid[x][y] = 0

