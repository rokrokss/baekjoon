import sys


def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    a1 = merge_sort(a[:mid])
    a2 = merge_sort(a[mid:])
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] < a2[i2]:
            a[ia] = a1[i1]
            i1 += 1
        else:
            a[ia] = a2[i2]
            i2 += 1
        ia += 1
    while i1 < len(a1):
        a[ia] = a1[i1]
        i1 += 1
        ia += 1
    while i2 < len(a2):
        a[ia] = a2[i2]
        i2 += 1
        ia += 1
    return a


read = sys.stdin.readline
n = int(read())
a = merge_sort(list(map(int, read().split())))
print(a)

