from sys import stdin


def pow(base, idx, mod):
    if idx == 1: return base
    if idx % 2 == 0:
        r = pow(base, idx / 2, mod)
        return (r * r) % mod
    else:
        return (base * pow(base, idx - 1, mod)) % mod


read = stdin.readline
t = int(read())
for _ in range(t):
    a, b = map(int, read().split())
    ans = pow(a, b, 10)
    if ans == 0: ans = 10
    print(ans)


