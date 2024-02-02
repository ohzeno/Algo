# https://www.acmicpc.net/problem/9251
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 
두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK다.
두 문자열이 주어지면 LCS의 길이를 출력하라.
"""
s1 = input()
s2 = input()
l_s1, l_s2 = len(s1), len(s2)
dp = [[0] * (l_s2 + 1) for _ in range(l_s1 + 1)]
for r in range(1, l_s1 + 1):
    for c in range(1, l_s2 + 1):
        if s1[r-1] == s2[c-1]:  # 같은 문자면 양쪽 포인터 뒤로 가서 +1
            dp[r][c] = dp[r-1][c-1] + 1
        else:  # 다른 문자면 이전 값 중 최대값
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])
print(dp[-1][-1])
# 메모리 최적화 버전
# dp = [[0] * (l_s2 + 1) for _ in range(2)]
# for r in range(1, l_s1 + 1):
#     for c in range(1, l_s2 + 1):
#         if s1[r-1] == s2[c-1]:
#             dp[1][c] = dp[0][c-1] + 1
#         else:
#             dp[1][c] = max(dp[0][c], dp[1][c-1])
#     dp[0] = dp[1]
#     dp[1] = [0] * (l_s2 + 1)
# print(dp[0][-1])


"""
현 시점 골드 5. 제출 82447. 정답률 40.597 %
lcs라 최장 공통 문자열인 줄 알고 풀다가 애먹었다.
같은 분야에서 다른 개념을 같은 약어로 사용하는게 좀 어이없다.

최장 공통 문자열이 아니라 부분 수열이라 중간에 끊겨도 된다.
dp풀이가 제일 속편함.
왠지 메모리 최적화하면 몇십 ms 빨라진다.
정답 순위에 더 빠른 버전이 있는데, 덜 직관적이다.
"""