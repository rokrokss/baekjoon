import sys


def rotate_face(cube, side, direction):
    idx = 0
    if side == "D":
        idx += 9
    elif side == "F":
        idx += 18
    elif side == "B":
        idx += 27
    elif side == "L":
        idx += 36
    elif side == "R":
        idx += 45
    tmp = cube[idx:idx+9]
    if direction == "+":
        cube[idx:idx+9] = [tmp[6], tmp[3], tmp[0], tmp[7], tmp[4], tmp[1], tmp[8], tmp[5], tmp[2]]
    else:
        cube[idx:idx+9] = [tmp[2], tmp[5], tmp[8], tmp[1], tmp[4], tmp[7], tmp[0], tmp[3], tmp[6]]


def turn(cube, side, direction):
    rotate_face(cube, side, direction)
    tmp = cube[:]
    if side == "U":
        if direction == "+":
            cube[33], cube[34], cube[35] = tmp[38], tmp[37], tmp[36]
            cube[36], cube[37], cube[38] = tmp[18], tmp[19], tmp[20]
            cube[18], cube[19], cube[20] = tmp[45], tmp[46], tmp[47]
            cube[45], cube[46], cube[47] = tmp[35], tmp[34], tmp[33]
        else:
            cube[33], cube[34], cube[35] = tmp[47], tmp[46], tmp[45]
            cube[45], cube[46], cube[47] = tmp[18], tmp[19], tmp[20]
            cube[18], cube[19], cube[20] = tmp[36], tmp[37], tmp[38]
            cube[36], cube[37], cube[38] = tmp[35], tmp[34], tmp[33]
    elif side == "F":
        if direction == "+":
            cube[45], cube[48], cube[51] = tmp[6], tmp[7], tmp[8]
            cube[6], cube[7], cube[8] = tmp[44], tmp[41], tmp[38]
            cube[38], cube[41], cube[44] = tmp[9], tmp[10], tmp[11]
            cube[9], cube[10], cube[11] = tmp[51], tmp[48], tmp[45]
        else:
            cube[45], cube[48], cube[51] = tmp[11], tmp[10], tmp[9]
            cube[6], cube[7], cube[8] = tmp[45], tmp[48], tmp[51]
            cube[38], cube[41], cube[44] = tmp[8], tmp[7], tmp[6]
            cube[9], cube[10], cube[11] = tmp[38], tmp[41], tmp[44]
    elif side == "D":
        if direction == "+":
            cube[24], cube[25], cube[26] = tmp[42], tmp[43], tmp[44]
            cube[42], cube[43], cube[44] = tmp[29], tmp[28], tmp[27]
            cube[27], cube[28], cube[29] = tmp[53], tmp[52], tmp[51]
            cube[51], cube[52], cube[53] = tmp[24], tmp[25], tmp[26]
        else:
            cube[24], cube[25], cube[26] = tmp[51], tmp[52], tmp[53]
            cube[51], cube[52], cube[53] = tmp[29], tmp[28], tmp[27]
            cube[27], cube[28], cube[29] = tmp[44], tmp[43], tmp[42]
            cube[42], cube[43], cube[44] = tmp[24], tmp[25], tmp[26]
    elif side == "B":
        if direction == "+":
            cube[0], cube[1], cube[2] = tmp[47], tmp[50], tmp[53]
            cube[47], cube[50], cube[53] = tmp[17], tmp[16], tmp[15]
            cube[15], cube[16], cube[17] = tmp[36], tmp[39], tmp[42]
            cube[36], cube[39], cube[42] = tmp[2], tmp[1], tmp[0]
        else:
            cube[0], cube[1], cube[2] = tmp[42], tmp[39], tmp[36]
            cube[36], cube[39], cube[42] = tmp[15], tmp[16], tmp[17]
            cube[15], cube[16], cube[17] = tmp[53], tmp[50], tmp[47]
            cube[47], cube[50], cube[53] = tmp[0], tmp[1], tmp[2]
    elif side == "L":
        if direction == "+":
            cube[0], cube[3], cube[6] = tmp[27], tmp[30], tmp[33]
            cube[27], cube[30], cube[33] = tmp[9], tmp[12], tmp[15]
            cube[9], cube[12], cube[15] = tmp[18], tmp[21], tmp[24]
            cube[18], cube[21], cube[24] = tmp[0], tmp[3], tmp[6]
        else:
            cube[0], cube[3], cube[6] = tmp[18], tmp[21], tmp[24]
            cube[18], cube[21], cube[24] = tmp[9], tmp[12], tmp[15]
            cube[9], cube[12], cube[15] = tmp[27], tmp[30], tmp[33]
            cube[27], cube[30], cube[33] = tmp[0], tmp[3], tmp[6]
    else:   #R
        if direction == "+":
            cube[2], cube[5], cube[8] = tmp[20], tmp[23], tmp[26]
            cube[20], cube[23], cube[26] = tmp[11], tmp[14], tmp[17]
            cube[11], cube[14], cube[17] = tmp[29], tmp[32], tmp[35]
            cube[29], cube[32], cube[35] = tmp[2], tmp[5], tmp[8]
        else:
            cube[2], cube[5], cube[8] = tmp[29], tmp[32], tmp[35]
            cube[29], cube[32], cube[35] = tmp[11], tmp[14], tmp[17]
            cube[11], cube[14], cube[17] = tmp[20], tmp[23], tmp[26]
            cube[20], cube[23], cube[26] = tmp[2], tmp[5], tmp[8]


read = sys.stdin.readline
t = int(read())
ans = []
for _ in range(t):
    cube = list("wwwwwwwwwyyyyyyyyyrrrrrrrrrooooooooogggggggggbbbbbbbbb")
    read()
    operations = read().split()
    for op in operations:
        turn(cube, op[0], op[1])
    print(*cube[0:3], sep="")
    print(*cube[3:6], sep="")
    print(*cube[6:9], sep="")
