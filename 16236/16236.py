import sys
from collections import deque


class Queue():
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return not self.items


class Shark():
    def __init__(self, pos=None):
        self.size = 2
        self.stomach = 0
        self.pos = pos

    def eat(self):
        self.stomach += 1
        if self.stomach == self.size:
            self.size += 1
            self.stomach = 0


def next_pos(pos):
    x, y = pos[0], pos[1]
    return [[x, y-1], [x+1, y], [x-1, y], [x, y+1]]


read = sys.stdin.readline
n = int(read())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
food = []
s = Shark()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            s.pos = [i, j]
            grid[i][j] = 0
ans = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = Queue()
    pos = s.pos
    q.enqueue((pos, 0))
    visited[pos[0]][pos[1]] = True
    found = []
    while not q.is_empty():
        curr, steps = q.dequeue()
        value = grid[curr[0]][curr[1]]
        if 0 < value < s.size:
            found.append((curr, steps))
        elif value <= s.size and not found:
            for pos in next_pos(curr):
                if 0 <= pos[0] <= n-1 and 0 <= pos[1] <= n-1 and not visited[pos[0]][pos[1]]:
                    visited[pos[0]][pos[1]] = True
                    q.enqueue((pos, steps+1))
    if not found:
        break
    else:
        found.sort(key=lambda pos: pos[1]*n*n + pos[0][0]*n + pos[0][1])
        s.eat()
        grid[found[0][0][0]][found[0][0][1]] = 0
        ans += found[0][1]
        grid[s.pos[0]][s.pos[1]] = 0
        s.pos = found[0][0]
print(ans)

