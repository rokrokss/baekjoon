n = int(input())
arr = sorted(list(map(int, input().split(' '))))
print(2*sum([arr[i] * (2*i - n + 1) for i in range(n)]))

