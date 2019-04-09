import sys


class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)


def change_direction(direction, c):
    if c == "L":
        if direction == [1, 0]: return[0, 1]
        elif direction == [-1, 0]: return [0, -1]
        elif direction == [0, 1]: return [-1, 0]
        else: return [1, 0]
    else:
        if direction == [1, 0]: return [0, -1]
        elif direction == [-1, 0]: return [0, 1]
        elif direction == [0, 1]: return [1, 0]
        else: return [-1, 0]


read = sys.stdin.readline
n = int(read())
grid = [[0 for _ in range(n)] for _ in range(n)]
k = int(read())
for _ in range(k):
    apple_pos = [int(x) for x in read().split()]
    grid[apple_pos[0]-1][apple_pos[1]-1] = 2
l = int(read())
dir_changes = []
for _ in range(l):
    xc = read().split()
    dir_changes.append((int(xc[0]), xc[1]))
t = 0
direction = [0, 1]
grid[0][0] = 1
snake_head = [0, 0]
q = Queue()
q.enqueue(snake_head)
while True:
    head_next = [snake_head[0] + direction[0], snake_head[1] + direction[1]]
    t += 1
    if head_next[0] >= n or head_next[1] >= n or head_next[0] < 0 or head_next[1] < 0:
        break
    head_item = grid[head_next[0]][head_next[1]]
    if head_item == 1:
        break
    q.enqueue(head_next)
    if head_item == 2:
        grid[head_next[0]][head_next[1]] = 1
    else:
        grid[head_next[0]][head_next[1]] = 1
        snake_tail = q.dequeue()
        grid[snake_tail[0]][snake_tail[1]] = 0
    if dir_changes and dir_changes[0][0] == t:
        direction = change_direction(direction, dir_changes[0][1])
        dir_changes.pop(0)
    snake_head = head_next
print(t)

