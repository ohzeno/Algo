# https://codeforces.com/problemset/problem/2041/E
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

def solve(a, b):
    if a == b:
        return [1, [a]]
    # 평균이 중앙값보다 큰 경우: [b, b, b, ..., large]
    # 평균이 중앙값보다 작은 경우: [small, b, b, b, ...]
    # n*a = trg + (n-1)*b
    # trg = n*a - (n-1)*b
    n = 3  # 2개면 b,b가 성립 안될 확률이 높아서 trg맞추다가 중앙값 조건 벗어남.
    trg = n * a - (n - 1) * b
    boundary = 1e6
    while (a > b and trg > boundary) or (a <= b and trg < -boundary):
        n += 1
        trg = n * a - (n - 1) * b
    if a > b:
        return [n, [b] * (n - 1) + [trg]]
    return [n, [trg] + [b] * (n - 1)]


a, b = map(int, input().split())
leng, arr = solve(a, b)
print(leng)
print(*arr)

"""
현 시점 Difficulty 1200. 완료 1918
"""
