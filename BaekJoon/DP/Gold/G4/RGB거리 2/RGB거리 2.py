# https://www.acmicpc.net/problem/17404
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
RGB거리에는 집이 N개 있다. 
거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

2 ≤ N ≤ 1,000, 비용은 1,000보다 작거나 같은 자연수이다.
"""

def calc(st):
    dp = [[INF, INF, INF] for _ in range(2)]
    dp[0][st] = costs[0][st]
    for i in range(1, n):
        dp[1][0] = min(dp[0][1], dp[0][2]) + costs[i][0]
        dp[1][1] = min(dp[0][0], dp[0][2]) + costs[i][1]
        dp[1][2] = min(dp[0][0], dp[0][1]) + costs[i][2]
        dp[0] = dp[1][:]
    return min(dp[1][st-1], dp[1][st-2])  # 마지막 집은 st와 다른 색

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
INF = 1000**2 + 1
print(min(calc(0), calc(1), calc(2)))


"""
현 시점 골드 4. 제출 15719. 정답률 59.467 %
규칙이 복잡해 보이지만 그냥 원형으로 이으면 i-1, i+1과 다른 색이라는 조건이다.
(처음과 끝을 이으면 1번과 N번이 i-1, i+1관계에 포함되기 때문에)
처음엔 dp배열 하나를 사용하면 첫 집의 색을 고정하지 못하지 않나 싶었다.
그래서 dp를 3번 따로 만들어서 풀었다.
이건 너무 초보적이고 무식한 방법이라 생각해서 다른 풀이들도 확인해봤는데
결국 전부 나와 비슷하게 dp배열을 3번 만드는 방법이었다.
"""
