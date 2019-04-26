import sys


def turn(d, lr):
    x, y = d
    if x == 1:
        if lr == "L":
            return [0, 1]
        else:
            return [0, -1]
    elif x == -1:
        if lr == "L":
            return [0, -1]
        else:
            return [0, 1]
    elif y == 1:
        if lr == "L":
            return [-1, 0]
        else:
            return [1, 0]
    else:
        if lr == "L":
            return [1, 0]
        else:
            return [-1, 0]


def move(s, d, t):
    return (s[0] + t * d[0], s[1] + t * d[1])


def update_answer(before, curr):
    if not before:
        result = curr
    else:
        result = min(before, curr)
    return result


def snake():
    read = sys.stdin.readline
    l = int(read())
    n = int(read())
    width = 2 * l + 1
    hor_lines = [
        (-1, -1, width),
        (width, -1, width)
    ]
    ver_lines = [
        (-1, -1, width),
        (width, -1, width)
    ]
    rotations = []
    for _ in range(n):
        line = read().split()
        rotations.append((int(line[0]), line[1]))
    rotations.append((2*10**11, None))
    d = [0, 1]
    s = (l, l)
    t = 0
    face_horizontal = True
    for t1, lr in rotations:
        dest = move(s, d, t1)
        ans = 0
        if face_horizontal:
            for line in hor_lines:
                if s[0] != line[0]: pass
                elif d[1] == 1:
                    if dest[1] < line[1]: pass
                    elif s[1] >= line[2]: pass
                    else: ans = update_answer(ans, t + line[1] - s[1])
                else:
                    if s[1] <= line[1]: pass
                    elif dest[1] > line[2]: pass
                    else: ans = update_answer(ans, t + s[1] - line[2])
            for line in ver_lines:
                if d[1] == 1:
                    if line[0] <= s[1] or line[0] > dest[1]: pass
                    elif line[2] < s[0] or line[1] > s[0]: pass
                    else: ans = update_answer(ans, t + line[0] - s[1])
                else:
                    if line[0] < dest[1] or line[0] >= s[1]: pass
                    elif line[2] < s[0] or line[1] > s[0]: pass
                    else: ans = update_answer(ans, t + s[1] - line[0])
            if d[1] == 1:
                hor_lines.append((s[0], s[1], dest[1]))
            else:
                hor_lines.append((s[0], dest[1], s[1]))
        else:
            for line in ver_lines:
                if s[1] != line[0]: pass
                elif d[0] == 1:
                    if dest[0] < line[1]: pass
                    elif s[0] >= line[2]: pass
                    else: ans = update_answer(ans, t + line[1] - s[0])
                else:
                    if s[0] <= line[1]: pass
                    if dest[0] > line[2]: pass
                    else: ans = update_answer(ans, t + s[0] - line[2])
            for line in hor_lines:
                if d[0] == 1:
                    if line[0] <= s[0] or line[0] > dest[0]: pass
                    elif line[2] < s[1] or line[1] > s[1]: pass
                    else: ans = update_answer(ans, t + line[0] - s[0])
                else:
                    if line[0] < dest[0] or line[0] >= s[0]: pass
                    elif line[2] < s[1] or line[1] > s[1]: pass
                    else: ans = update_answer(ans, t + s[0] - line[0])
            if d[0] == 1:
                ver_lines.append((s[1], s[0], dest[0]))
            else:
                ver_lines.append((s[1], dest[0], s[0]))
        if ans: return ans
        t += t1
        d = turn(d, lr)
        s = dest
        face_horizontal = not face_horizontal


print(snake())
