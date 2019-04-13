import operator


class Heap():
    def __init__(self, compare = operator.lt):
        self.heap = []
        self.compare = compare

    def _heapify(self, parent_index):
        heap, compare = self.heap, self.compare
        length = len(heap)
        if length == 1:
            return
        parent = parent_index
        while 2 * parent < length:
            child = 2 * parent
            if child + 1 < length and compare(heap[child + 1], heap[child]):
                child += 1
            if compare(heap[parent], heap[child]):
                return
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child

    def _inv_heapify(self, child_index):
        heap, compare = self.heap, self.compare
        child = child_index
        while child > 0:
            parent = child // 2
            if compare(heap[parent], heap[child]):
                return
            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent

    def add(self, item):
        self.heap.append(item)
        self._inv_heapify(len(self.heap) - 1)

    def del_min(self):
        heap = self.heap
        last_element = heap.pop()
        if not heap:
            return last_element
        item = heap[0]
        heap[0] = last_element
        self._heapify(0)
        return item

