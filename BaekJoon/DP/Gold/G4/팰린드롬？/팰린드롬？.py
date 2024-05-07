# https://www.acmicpc.net/problem/10942
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
먼저, 홍준이는 자연수 N개를 칠판에 적는다. 그 다음, 명우에게 질문을 총 M번 한다.
각 질문은 두 정수 S와 E(1 ≤ S ≤ E ≤ N)로 나타낼 수 있으며, 
S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지를 물어보며, 
명우는 각 질문에 대해 팰린드롬이다 또는 아니다를 말해야 한다.
예를 들어, 홍준이가 칠판에 적은 수가 1, 2, 1, 3, 1, 2, 1라고 하자.
S = 1, E = 3인 경우 1, 2, 1은 팰린드롬이다.
S = 2, E = 5인 경우 2, 1, 3, 1은 팰린드롬이 아니다.
S = 3, E = 3인 경우 1은 팰린드롬이다.
S = 5, E = 7인 경우 1, 2, 1은 팰린드롬이다.
자연수 N개와 질문 M개가 모두 주어졌을 때, 명우의 대답을 구하는 프로그램을 작성하시오.
"""

n = int(input())
nums = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1
for l in range(2, n):
    for i in range(n-l):
        if nums[i] == nums[i+l] and dp[i+1][i+l-1]:
            dp[i][i+l] = 1
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])


"""
현 시점 골드 4. 제출 57397. 정답률 29.897 %
팰린드롬을 판단할 때 매번 순회하면 시간초과가 난다.
dp를 이용해 베이스 케이스부터 순회해야 한다.
1자리, 2자리를 따로 처리해주고 3자리를 순회하면서 팰린드롬 여부를 판단한다.
처음엔 세번째 루프에서 i를 밖에 두고 l을 순회했는데,
그러면 3, 5가 True인데 2, 6이 펠린드롬으로 판정되지 않는다.
짧은 길이를 참조하여 상위 길이의 팰린드롬 여부를 판단하므로,
짧은 길이를 먼저 순회해야 한다.
"""