# https://www.acmicpc.net/problem/16493
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
남은 일 수 1<=N<=200
챕터 수 1<=M<=20
"""

N, M = map(int, input().split())
datas = []
# dp[i]: i일동안 읽을 수 있는 최대 페이지 수
dp = [0] * (N + 1)
for _ in range(M):
    d, p = map(int, input().split())
    datas.append((d, p))
for d, p in datas:
    for i in range(N, d-1, -1):
        dp[i] =max(dp[i], dp[i-d] + p)
print(max(dp))

"""
현 시점 Silver II. 제출 2795. 정답률 64.680 %
배낭 문제 연습용. 0/1 유형을 방금 전에 풀었기에 쉬웠다.
"""
