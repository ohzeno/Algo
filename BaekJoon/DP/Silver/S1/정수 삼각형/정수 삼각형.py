# https://www.acmicpc.net/problem/1932
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽/오른쪽에 있는 것만 선택할 수 있다.
삼각형의 크기는 1 이상 500 이하이다. 
삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
"""

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = tri[0][0]
for r in range(1, n):
    for c in range(r + 1):
        if c == 0:  # 왼쪽 끝은 우상단에서만 내려옴
            dp[r][c] = dp[r - 1][c] + tri[r][c]
        elif c == r:  # 오른쪽 끝은 좌상단에서만 내려옴
            dp[r][c] = dp[r - 1][c - 1] + tri[r][c]
        else:  # 좌, 우 상단 중 큰 값에 현재 값 더함
            dp[r][c] = max(dp[r - 1][c - 1], dp[r - 1][c]) + tri[r][c]
print(max(dp[-1]))

"""
현 시점 실버1. 제출 76656, 정답률 59.061%
삼각형이라 인덱싱이 좀 귀찮은 dp문제.
"""
