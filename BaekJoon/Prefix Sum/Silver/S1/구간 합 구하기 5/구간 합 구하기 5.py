# https://www.acmicpc.net/problem/11660
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
nxn 표의 칸마다 수가 들어있다.
(x1, y1)부터 (x2, y2)까지 합을 구하라.
표의 크기 n, 합을 구할 횟수 m, 표의 정보가 주어진다.
1 <= n <= 1024, 1 <= m <= 10_0000
x1 <= x2, y1 <= y2
"""

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n+1) for _ in range(n+1)]
# dp[i][j] = mat[0][0] ~ mat[i-1][j-1]까지의 누적합
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = mat[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])



"""
현 시점 실버 1. 제출 61831. 정답률 44.146 %
처음에는 그냥 for문으로 푸는건가? 그런데 왜 실1인지 의문을 가졌다가 
m이 10만인 것을 보고 누적합으로 선회했다.
집합 그림으로 생각하면 쉽다.
"""