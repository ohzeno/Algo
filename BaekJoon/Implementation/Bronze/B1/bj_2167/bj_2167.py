# https://www.acmicpc.net/problem/2167
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
"""
pypy 쓰면 시간초과는 안난다. 브론즈라 그냥 일일이 더했다. 
시간제한이 더 빡빡하다면 각 좌표에 그 좌표까지의 합을 넣어놓으면 계산이 중복되지 않아 빠르다.
"""
for _ in range(k):
    i, j, x, y = map(int, input().split())
    ans = 0
    for r in range(i - 1, x):
        for c in range(j - 1, y):
            ans += mat[r][c]
    print(ans)

