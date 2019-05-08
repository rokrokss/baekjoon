import sys


def solution(n):
    arr = [0] * (n + 3)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n):
        arr[i] = (arr[i - 1] + arr[i - 3]) % 1000000009
    return arr[n - 1]


n = int(sys.stdin.readline())
print(solution(n) % 1000000009)

