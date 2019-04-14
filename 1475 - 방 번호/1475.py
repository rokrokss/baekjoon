N = input()
N = int(N)
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
if int((arr[6] + arr[9] + 1)/2) > num:
    num = int((arr[6] + arr[9] + 1)/2)
print(num)