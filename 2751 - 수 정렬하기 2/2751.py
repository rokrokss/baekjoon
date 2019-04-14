from sys import stdin
read = stdin.readline
t = int(read())
input_list = []
for _ in range(t):
    n = int(read())
    input_list.append(n)
print(*sorted(input_list), sep='\n')
