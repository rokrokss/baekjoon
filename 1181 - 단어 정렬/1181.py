import sys

N = int(sys.stdin.readline())
arr = [set() for _ in range(51)]
for i in range(N):
    w = sys.stdin.readline().rstrip()
    l = len(w)
    arr[l].add(w)
for s in arr:
    if s:
        for w in sorted(s):
            print(w)
