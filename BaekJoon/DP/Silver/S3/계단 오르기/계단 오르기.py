# https://www.acmicpc.net/problem/2579
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
계단 오르기 게임. 시작점부터 꼭대기 계단까지 가는 게임.
각 계단에는 해당 계단을 밟으면 얻을 수 있는 점수가 적혀있다.
1. 한 번에 1~2계단을 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. (시작점은 제외)
3. 마지막 계단은 반드시 밟아야 한다.
계단을 오를 때 얻을 수 있는 점수의 최댓값을 구하라.
"""
def solution():
    if n < 3:
        return sum(scores)
    dp = [0] * (n+1)
    dp[1] = scores[1]
    dp[2] = dp[1] + scores[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + scores[i-1], dp[i-2]) + scores[i]
    return dp[n]
n = int(input())
scores = [0] + [int(input()) for _ in range(n)]
print(solution())


"""
현 시점 실버 3. 제출 179249. 정답률 33.887%
간단한 dp문제.
"""