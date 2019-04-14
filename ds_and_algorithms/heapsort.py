from sys import stdin


def build_heap(unsorted, index, heap_size):
    largest = index
    left_index, right_index = 2*index+1, 2*index+2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        build_heap(unsorted, largest, heap_size)


def heapsort(arr):
    n = len(arr)
    for i in range((n-1)//2, -1, -1):
        build_heap(arr, i, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        build_heap(arr, 0, i)


read = stdin.readline
t = int(read())
arr = []
for _ in range(t):
    arr.append(int(read()))
heapsort(arr)
print(*arr, sep=' ')

