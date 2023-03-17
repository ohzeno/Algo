# https://www.acmicpc.net/problem/9461
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
첫 삼각형은 한 변의 길이가 1인 정삼각형. 나선에서 가장 긴 변의 길이를 k라 할 때, 
그 변을 한 변으로 하는 정삼각형을 추가한다.
파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. 
P(1)부터 P(10)까지의 수는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.
N이 주어졌을 때, P(N)을 출력하라.
"""
for _ in range(int(input())):
    n = int(input())
    dp = [0] * (n+1)
    for i in range(1, min(4, n + 1)):
        dp[i] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])

"""
현 시점 실버3. 제출 82246, 정답률 42.711%
2×n 타일링처럼 값들을 나열해놓고 보며 규칙을 찾았다. 그나마 이 문제는 n = 10까지 값이 주어져있어 편했다.
"""