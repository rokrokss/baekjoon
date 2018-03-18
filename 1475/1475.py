N = int(input())
arr = []
for i in range(0, 10):
    arr.append(0)
while True:
    arr[N % 10] += 1
    if N < 10:
        break
    N = int(N/10)
num = 0
for idx, n in enumerate(arr):
    if idx != 9 and idx != 6:
        if n > num:
            num = n
numSixNine = int((arr[6] + arr[9] + 1)/2)
if numSixNine > num:
    num = numSixNine
print(num)
