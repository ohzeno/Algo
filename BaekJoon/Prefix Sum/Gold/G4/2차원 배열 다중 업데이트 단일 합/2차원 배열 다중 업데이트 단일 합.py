# https://www.acmicpc.net/problem/25826
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
질의1: 1 i1 j1 i2 j2 k i1<=i<=i2, j1<=j<j2인 A[i][j]에 k를 더한다.
질의2: 2 i1 j1 i2 j2 i1<=i<=i2, j1<=j<j2인 A[i][j]의 합을 출력한다.
질의2는 B 마지막에 1개만 있다.
"""

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
acc = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m - 1):
    _, r1, c1, r2, c2, k = list(map(int, input().split()))
    acc[r1][c1] += k
    acc[r2 + 1][c1] -= k
    acc[r1][c2 + 1] -= k
    acc[r2 + 1][c2 + 1] += k
# 가로 누적 먼저
for c in range(1, n + 1):
    for r in range(n+1):
        acc[r][c] += acc[r][c - 1]
# 세로 누적
for r in range(1, n + 1):
    for c in range(n+1):
        acc[r][c] += acc[r - 1][c]
_, r1, c1, r2, c2 = list(map(int, input().split()))
ans = 0
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        ans += mat[i][j] + acc[i][j]
print(ans)


"""
현 시점 Gold IV. 제출 369. 정답률 52.347 %
2차원 imos 연습해보려고 푼 문제.
"""
