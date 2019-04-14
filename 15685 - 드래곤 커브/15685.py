import sys


class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return not self.items


def curve_from_zero(g):
    global memo
    if not memo[g]:
        curve = curve_from_zero(g-1)[:]
        s = Stack()
        for c in curve:
            s.push(c)
        while not s.is_empty():
            curve.append(s.pop()+1)
        memo[g] = curve
    return memo[g]


def get_curve(x, y, d, g):
    global memo
    curve = curve_from_zero(g)
    curve_cords = [[x, y]]
    for c in curve:
        c = (c + d) % 4
        if c == 0:
            x += 1
            curve_cords.append([x, y])
        elif c == 1:
            y -= 1
            curve_cords.append([x, y])
        elif c == 2:
            x -= 1
            curve_cords.append([x, y])
        else:
            y += 1
            curve_cords.append([x, y])
    return curve_cords


read = sys.stdin.readline
n = int(read())
grid = [[0 for _ in range(101)] for _ in range(101)]
memo = [[] for _ in range(11)]
memo[0] = [0]
for _ in range(n):
    x, y, d, g = map(int, read().split())
    curve_cords = get_curve(x, y, d, g)
    for curve_x, curve_y in curve_cords:
        grid[curve_x][curve_y] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
            ans += 1
print(ans)

