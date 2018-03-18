import sys
from collections import Counter

N = int(sys.stdin.readline())
sum = 0
arr = []
for i in range(N):
    n = int(sys.stdin.readline())
    sum += n
    arr.append(n)
arr.sort()
N = len(arr)
min = arr[0]
max = arr[N-1]
median = 0
mode = 0
if N % 2 == 1:
    median = arr[(N-1)//2]
else:
    median = (arr[N//2] + arr[N//2-1]) / 2
cntArr = Counter(arr).most_common()
if N == 1:
    mode = cntArr[0][0]
else:
    if cntArr[0][1] == cntArr[1][1]:
        mode = cntArr[1][0]
    else:
        mode = cntArr[0][0]

print(round(sum/N))
print(median)
print(mode)
print(max-min)
