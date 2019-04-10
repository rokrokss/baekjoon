import sys


def dfs_calculate(ans, idx, a_s, s_s, m_s, d_s):
    global max_ans, min_ans, numbers
    #print((ans, idx, a_s, s_s, m_s, d_s))
    if idx == len(numbers):
        max_ans = max(ans, max_ans)
        min_ans = min(ans, min_ans)
    if a_s > 0:
        dfs_calculate(ans + numbers[idx], idx + 1, a_s - 1, s_s, m_s, d_s)
    if s_s > 0:
        dfs_calculate(ans - numbers[idx], idx + 1, a_s, s_s - 1, m_s, d_s)
    if m_s > 0:
        dfs_calculate(ans * numbers[idx], idx + 1, a_s, s_s, m_s - 1, d_s)
    if d_s > 0:
        if ans >= 0: dfs_calculate(ans // numbers[idx], idx + 1, a_s, s_s, m_s, d_s - 1)
        else: dfs_calculate(-1*ans//numbers[idx] * (-1), idx + 1, a_s, s_s, m_s, d_s - 1)

max_ans, min_ans = -1000000000, 1000000000
read = sys.stdin.readline
n = int(read())
numbers = list(map(int, read().split()))
a, s, m, d = map(int, read().split())
dfs_calculate(numbers[0], 1, a, s, m, d)
print(max_ans)
print(min_ans)

