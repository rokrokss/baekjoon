import sys
from collections import deque


class Queue():
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)


def bfs(miro, n, m):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = 1
    q = Queue()
    q.enqueue((0, 0))
    visited[0][0] = True
    while not q.is_empty():
        size = q.size()
        for _ in range(size):
            cur = q.dequeue()
            if cur[0] == n - 1 and cur[1] == m - 1:
                return result
            for d in directions:
                next = (cur[0] + d[0], cur[1] + d[1])
                if next[0] == -1 or next[0] == n or next[1] == -1 or next[1] == m:
                    continue
                if not miro[next[0]][next[1]]:
                    continue
                if visited[next[0]][next[1]]:
                    continue
                q.enqueue(next)
                visited[next[0]][next[1]] = True
        result += 1


read = sys.stdin.readline
n, m = map(int, read().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, read().strip())))
print(bfs(miro, n, m))

