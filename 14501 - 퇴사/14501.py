import sys


def get_money(day, money):
    global ts, ps, n
    if day == n:
        return money
    elif day + ts[day] > n:
        return get_money(day + 1, money)
    else:
        return max(get_money(day + 1, money), get_money(day + ts[day], money + ps[day]))


read = sys.stdin.readline
ts, ps = [], []
n = int(read())
money = 0
for _ in range(n):
    t, p = map(int, read().split())
    ts.append(t)
    ps.append(p)
score = get_money(0, 0)
print(score)

