import sys


read = sys.stdin.readline
n = int(read())
candidates = [int(x) for x in read().split()]
b, c = [int(x) for x in read().split()]
result = 0
for cnt in candidates:
    cnt -= b
    result += 1
    if cnt > 0:
        result += -(-cnt // c)
print(result)
