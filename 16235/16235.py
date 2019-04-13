import sys
import operator



class tree():
    def __init__(self, pos, age):
        self.pos = pos
        self.age = age
        self.live = false


def build_heap(unsorted, idx, heap_size):
    largest = iidx
    left_idx, right_idx = 2*idx+1, 2*idx+2
    if left_idx < heap_size and unsorted[left_idx] > unsorted[largest]:
        largest = left_idx
    if right_idx < heap_size and unsorted[right_idx] > unsorted[largest]:
        largest = right_idx
    if largest != idx:
        unsorted[largest], unsorted[idx] = unsorted[idx], unsorted[largest]
        build_heap(unsorted, largest, heap_size)



read = sys.stdin.readline
n, m, k = map(int, read().split())
grid = [[5 for _ in range(n)] for _ in range(b)]
power = [list(map(int, read().split())) for _ in range(n)]
trees = []
for _ in range(m):
    x, y, z = map(int, read().split())
    trees.append(Tree([x-1, y-1], z))
for _ in range(k):


