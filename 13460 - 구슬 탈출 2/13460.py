import sys

world = []
class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def empty(self):
        return not self.items


class Status():
    def __init__(self, depth, rx, ry, bx, by):
        self.depth = depth
        self.rx, self.ry, self.bx, self.by = rx, ry, bx, by


def move(x, y, direction):
    global world
    while True:
        x += direction[0]
        y += direction[1]
        if world[y][x] == "O":
            break
        if world[y][x] == "#":
            x -= direction[0]
            y -= direction[1]
            break
    return (x, y)


read = sys.stdin.readline
nm = read().strip().split()
h = int(nm[0].rstrip())
w = int(nm[1].lstrip())
visit = [[[[False for _ in range(h)] for _ in range(w)] for _ in range(h)] for _ in range(w)]
rx, ry, bx, by, ox, oy = 0, 0, 0, 0, 0, 0
for i in range(h):
    line = read().rstrip()
    for j in range(w):
        if line[j] == "R":
            rx, ry = j, i
        elif line[j] == "B":
            bx, by = j, i
        elif line[j] == "O":
            ox, oy = j, i
    world.append(line.replace("R", ".").replace("B", "."))
q = Queue()
initial_status = Status(0, rx, ry, bx, by)
q.enqueue(initial_status)
ans = -1
directions = [(1,0), (-1,0), (0,1), (0,-1)]
found = False
while not (q.empty() or found):
    cur = q.dequeue()
    cur_rx, cur_ry, cur_bx, cur_by = cur.rx, cur.ry, cur.bx, cur.by
    visit[cur_rx][cur_ry][cur_bx][cur_by] = True
    for direction in directions:
        next_rx, next_ry = move(cur_rx, cur_ry, direction)
        next_bx, next_by = move(cur_bx, cur_by, direction)
        next_depth = cur.depth + 1
        if next_bx == ox and next_by == oy:
            continue
        if next_rx == ox and next_ry == oy:
            ans = next_depth
            found = True
            break
        if next_bx == next_rx and next_by == next_ry:
            if direction == (1, 0):
                if cur.rx < cur.bx:
                    next_rx -= 1
                else:
                    next_bx -= 1
            elif direction == (-1, 0):
                if cur.rx > cur.bx:
                    next_rx += 1
                else:
                    next_bx += 1
            elif direction == (0, 1):
                if cur.ry < cur.by:
                    next_ry -= 1
                else:
                    next_by -= 1
            else:
                if cur.ry > cur.by:
                    next_ry += 1
                else:
                    next_by += 1
        if next_depth < 10 and not visit[next_rx][next_ry][next_bx][next_by]:
            q.enqueue(Status(next_depth, next_rx, next_ry, next_bx, next_by))
print(ans)
