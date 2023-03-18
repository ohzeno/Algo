# https://www.acmicpc.net/problem/11726
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
2xn 크기 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하고
10007로 나눈 나머지를 출력하라.
"""

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
if n > 1:
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n] % 10007)

"""
현 시점 실버3. 제출 136569, 정답률 36.092%
처음엔 규칙을 찾으려고 애썼다. dp를 이용하여, 큰 직사각형을 범위별로 나눠서 계산해보려 했지만 실패했다.
범위별 경우의 수는 구할 수 있지만, 구간 자체의 배치에서 가로 길이가 홀, 짝일 경우 계산이 달라진다.
그냥 n = 1 ~ 6일 경우를 수동으로 경우의 수를 찾아보니 피보나치 수열을 2항부터 나열한 것이었다.
규칙을 찾으려다 헤맨 케이스. 그냥 몇 케이스를 직접 구하고 규칙을 발견하는 게 편하다.
"""