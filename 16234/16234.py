import sys


class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        return not self.items


def is_family(x, y, x2, y2):
    global l, r, grid
    diff = abs(grid[x][y] - grid[x2][y2])
    if diff >= l and diff <= r:
        return True
    return False


def open_gates(countries):
    global visited, n
    q = Queue()
    q.enqueue(countries.pop())
    while not q.is_empty():
        x, y = q.dequeue()
        countries.append([x, y])
        if x > 0 and not visited[x-1][y]:
            if is_family(x, y, x-1, y):
                visited[x-1][y] = 1
                q.enqueue([x-1, y])
        if y > 0 and not visited[x][y-1]:
            if is_family(x, y, x, y-1):
                visited[x][y-1] = 1
                q.enqueue([x, y-1])
        if x < n-1 and not visited[x+1][y]:
            if is_family(x, y, x+1, y):
                visited[x+1][y] = 1
                q.enqueue([x+1, y])
        if y < n-1 and not visited[x][y+1]:
            if is_family(x, y, x, y+1):
                visited[x][y+1] = 1
                q.enqueue([x, y+1])
    return countries


def check():
    global grid, ans, n, visited
    visited = [[0 for _ in range(n)] for _ in range(n)]
    changed = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                countries = open_gates([[i, j]])
                if len(countries) > 1:
                    people_sum = 0
                    for c in countries:
                        people_sum += grid[c[0]][c[1]]
                    people = people_sum // len(countries)
                    for c in countries:
                        grid[c[0]][c[1]] = people
                    changed = True
    if not changed:
        return False
    else:
        ans += 1
        return True


read = sys.stdin.readline
n, l, r = map(int, read().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, read().split())))
visited = []
ans = 0
aaa = True
while aaa:
    aaa = check()
print(ans)

