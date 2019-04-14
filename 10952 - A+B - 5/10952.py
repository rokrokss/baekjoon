import sys


read = sys.stdin.readline
while True:
    ab = [int(x) for x in read().split()]
    if ab[0]==0 and ab[1]==0: break
    print(ab[0] + ab[1])

