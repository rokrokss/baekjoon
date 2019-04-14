import sys

N = int(sys.stdin.readline())
for i in range(N):
    line = sys.stdin.readline().rstrip()
    lines = line.split()
    num1 = int(lines[0])
    num2 = int(lines[1])
    print(num1+num2)
