import sys


read = sys.stdin.readline
n, l = map(int, read().split())
lines = []
for _ in range(n):
    lines.append(list(map(int, read().split())))
lines = lines + [list(col) for col in zip(*lines)]
ans = 0
for line in lines:
    i = 0
    ladders = [0 for _ in line]
    no = False
    while i < len(line)-1:
        gap = line[i+1] - line[i]
        if abs(gap) > 1:
            no = True
            break
        elif gap == 1:
            if i-l+1 < 0:
                no = True
                break
            for j in range(l):
                if line[i-j] != line[i] or ladders[i-j]==2:
                    no = True
                    break
                ladders[i-j] = 1
            if no: break
        elif gap == -1:
            if i+l >= n:
                no = True
                break
            for j in range(l):
                if line[i+j+1] != line[i+1] or ladders[i+j+1]==1:
                    no = True
                    break
                ladders[i+j+1] = 2
            if no: break
        i += 1
    if not no: ans += 1
print(ans)

