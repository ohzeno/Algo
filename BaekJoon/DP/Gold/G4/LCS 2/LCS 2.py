# https://www.acmicpc.net/problem/9252
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
LCS(Longest Common Subsequence, 최장 공통 부분 수열)
첫 줄에 입력으로 주어진 두 문자열의 LCS의 길이, 둘째 줄에 LCS를 출력하라.
"""

s1, s2 = input(), input()
l1, l2 = len(s1), len(s2)
dp = [[''] * (l2+1) for _ in range(l1+1)]
for i in range(1, l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + s1[i-1]
        else:
            dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
print(len(dp[-1][-1]))
print(dp[-1][-1])


"""
현 시점 골드 4. 제출 42240. 정답률 37.956 %
dp배열에 문자열을 저장하니 편했다.
"""