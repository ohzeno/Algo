# https://www.acmicpc.net/problem/9095
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
"""
# from itertools import product
# for _ in range(int(input())):
#     n = int(input())
#     dataset = [1, 2, 3]
#     tmps = []
#     for i in range(1, n + 1):
#         tmps.extend(product(dataset, repeat=i))
#     cnt = 0
#     for tmp in tmps:
#         if sum(tmp) == n:
#             cnt += 1
#     print(cnt)
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for _ in range(int(input())):
    n = int(input())
    print(dp[n])

"""
현 시점 실버3. 제출 184584, 정답률 32.216%
일반항 규칙을 구하려고 손으로 경우의 수를 찾았는데, 한참 헤맸다.
그냥 itertools를 이용해 직접 경우의 수를 구하고(이것도 통과됐다...) 
그 후에 dp규칙을 찾아서 적용했다.
"""