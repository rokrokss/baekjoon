import sys

N = int(sys.stdin.readline())
arr = [None] * 51
for i in range(N):
    w = sys.stdin.readline().rstrip()
    l = len(w)
    if arr[l]:
        arr[l].add(w)
    else:
        arr[l] = set()
        arr[l].add(w)
for s in arr:
    if s:
        for w in sorted(s):
            print(w)
