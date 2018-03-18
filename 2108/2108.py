def quicksort(data):
    if len(data) < 1:
        return data
    pivot = data[0]
    left = []
    right = []
    for x in range(1, len(data)):
        if data[x][0] <= pivot[0]:
            left.append(data[x])
        else:
            right.append(data[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right


N = int(input())
sum = 0
arr = []
for i in range(N):
    n = int(input())
    sum += n
    check = 0
    for (num, cnt) in arr:
        if num == n:
            cnt += 1
            check = 1
    if check == 0:
        arr.append((n, 1))
arr = quicksort(arr)
min = arr[0][0]
N = len(arr)
max = arr[N-1][0]
median = 0
modeArr = []
mode = 0

if N%2 == 1:
    median = arr[(N-1)//2][0]
else:
    median = (arr[N//2][0] + arr[N//2-1][0]) / 2

cntmax = 0
for (num, cnt) in arr:
    if cnt > cntmax:
        modeArr = [(num, 0)]
        cntmax = cnt
    elif cnt == cntmax:
        modeArr.append((num, 0))
modeArr = quicksort(modeArr)
if len(modeArr) > 1:
    mode = modeArr[1][0]
else:
    mode = modeArr[0][0]
print(round(sum/N))
print(median)
print(mode)
print(max-min)
