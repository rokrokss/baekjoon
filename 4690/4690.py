def aaa(a):
    return a*a*a


for i in range(2, 101):
    for j in range(2, 101):
        for k in range(j, 101):
            for l in range(k, 101):
                if aaa(i) == aaa(j) + aaa(k) + aaa(l):
                    print("Cube = {}, Triple = ({},{},{})".format(i, j, k, l))

