import sys


for line in sys.stdin:
    ab = [int(x) for x in line.split()]
    print(ab[0] + ab[1])

