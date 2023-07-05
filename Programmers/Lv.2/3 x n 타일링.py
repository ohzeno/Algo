# https://school.programmers.co.kr/learn/courses/30/lessons/12902
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
"""

def solution(n):
    if n % 2:
        return 0
    dp = [0] * (n+1)
    dp[0], dp[2] = 1, 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 4 - dp[i-4]
    return dp[n] % 1000000007

inputdatas = [
    4
]

"""
현 시점 Lv.2. 완료한 사람 2878명. 정답률 32%
Tri Tiling과 같은 문제. 백준의 타일 채우기와 거의 같은 코드다.
"""

for t in inputdatas:
    print(solution(t))