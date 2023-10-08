# https://www.acmicpc.net/problem/2775
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
이 아파트에 거주를 하려면 조건이 있는데, 
a층의 b호에 살려면 
(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다

아파트에 비어있는 집은 없고 
모든 거주민들이 계약 조건을 지키고 왔다고 가정했을 때, 
주어지는 양의 정수 k와 n에 대해 
k층 n호에는 몇 명이 살고 있는지 출력하라. 
단, 아파트는 0층부터 있고 각층은 1호부터 있으며, 0층 i호에는 i명이 산다.
"""
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    dp = [[0] * (n+1) for _ in range(k+1)]
    dp[0] = [i for i in range(n+1)]
    for i in range(1, k+1):
        for j in range(n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(dp[k][n])


"""
현 시점 브론즈 1. 제출 91277. 정답률 56.897%
재채점 알림이 떴는데 실패한 브론즈 문제가 있길래 다시 풀었다.
"""