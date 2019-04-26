import sys


class Heap():
    def __init__(self):
        self.heap = []

    def _compare(self, i, j):
        return self.heap[i][0] < self.heap[j][0]

    def _heapify(self, parent_idx):
        heap = self.heap
        length = len(heap)
        if length == 1:
            return
        parent = parent_idx
        child = 2 * parent + 1
        while child < length:
            if child + 1 < length and self._compare(child + 1, child):
                child += 1
            if self._compare(parent, child):
                return
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = 2 * parent + 1

    def _inv_heapify(self, child_idx):
        heap = self.heap
        child = child_idx
        while child > 0:
            parent = (child - 1) // 2
            if self._compare(parent, child):
                return
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent

    def add(self, item):
        self.heap.append(item)
        self._inv_heapify(len(self.heap) - 1)

    def min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def del_min(self):
        heap = self.heap
        last_element = heap.pop()
        if not heap:
            return last_element
        item = heap[0]
        heap[0] = last_element
        self._heapify(0)
        return item

    def is_empty(self):
        return not self.heap


def dijkstra(s, adj_list):
    global v, inf
    visited = [False for _ in range(v)]
    d = [inf for _ in range(v)]
    d[s] = 0
    q = Heap()
    q.add((d[s], s))
    while not q.is_empty():
        value, cur = q.del_min()
        if value > d[cur]: continue
        visited[cur] = True
        for dest, weight in adj_list[cur]:
            new_w = weight + d[cur]
            if (not visited[dest]) and new_w < d[dest]:
                d[dest] = new_w
                q.add((d[dest], dest))
    return d


inf = 10**7
read = sys.stdin.readline
v, e = map(int, read().split())
adj_list = [[] for _ in range(v)]
s = int(read()) - 1
for i in range(e):
    src, dest, w = map(int, read().split())
    adj_list[src - 1].append((dest - 1, w))
d = dijkstra(s, adj_list)
for item in d:
    if item == inf:
        print("INF")
    else:
        print(item)

