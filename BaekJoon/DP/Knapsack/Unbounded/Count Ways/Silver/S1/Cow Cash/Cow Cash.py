# https://www.acmicpc.net/problem/6126
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
V(1~25)개 동전으로 N원(1~10,000)원 만드는 방법 수?
"""

V, N = map(int, input().split())
coins = [int(input()) for _ in range(V)]
# dp[i]: i원 만드는 방법 수
dp = [0] * (1 + N)
dp[0] = 1
for c in coins:
    for i in range(c, N+1):
        dp[i] += dp[i - c]
print(dp[N])


"""
현 시점 Silver I. 제출 239. 정답률 60.204 %
무한 배낭 연습하려고 했는데 또 분류가 달랐다.
Count Ways.
"""
