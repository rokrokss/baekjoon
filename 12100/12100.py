import sys


class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return not self.items


def move_line(line, direction):
    combined = False
    nums = [x for x in line if x > 0]
    if direction == 1:
        line = [0 for _ in range(len(line) - len(nums))] + nums
        for i in reversed(range(len(line))):
            if i==0: break
            if line[i] == 0: break
            if line[i] == line[i-1]:
                line[i] *= 2
                line[:i] = [0] + line[:i-1]
    else:
        line = nums + [0 for _ in range(len(line) - len(nums))]
        for i in range(len(line)-1):
            if line[i] == 0: break
            if line[i] == line[i+1]:
                line[i] *= 2
                line[i+1:] = line[i+2:] + [0]
    return line


def move(grid, direction):
    new_grid = []
    for xgrid in grid:
        new_grid.append(xgrid[:])
    if direction[1] == 0:
        for i in range(len(new_grid)):
            new_grid[i] = move_line(new_grid[i], direction[0])
    else:
        for i in range(len(new_grid[0])):
            ygrid = move_line([xgrid[i] for xgrid in new_grid], direction[1])
            for j in range(len(ygrid)):
                new_grid[j][i] = ygrid[j]
    return new_grid


def biggest_in_grid(grid):
    biggest = 0
    for xgrid in grid:
        for x in xgrid:
            if x > biggest:
                biggest = x
    return biggest


grid = []
read = sys.stdin.readline
n = int(read())
for i in range(n):
    grid.append([int(x) for x in read().split()])
if n == 1:
    print(grid[0][0])
else:
    ans = 0
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    q = Queue()
    q.enqueue((0, grid))
    while not q.isEmpty():
        depth, cur = q.dequeue()
        for direction in directions:
            new_grid = move(cur, direction)
            new_biggest = biggest_in_grid(new_grid)
            if new_biggest > ans:
                ans = new_biggest
            if depth < 4:
                q.enqueue((depth+1, new_grid))
    print(ans)
