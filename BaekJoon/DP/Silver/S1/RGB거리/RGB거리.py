# https://www.acmicpc.net/problem/1149
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

- 1번 집의 색은 2번 집의 색과 달라야 한다.
- N번 집의 색은 N-1번 집의 색과 달라야 한다.
- i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 달라야 한다.
"""
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]  # costs[i] = [r, g, b]
dp = [[0] * 3 for _ in range(n)]
dp[0] = costs[0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]  # i번째 집을 r로 칠하는 비용
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
print(min(dp[-1]))

"""
현 시점 실버1. 제출 93964, 정답률 53.137%
bfs로 풀기에는 시간제한이 0.5초로 빡빡해서 dp를 생각했는데,
dp에서 1번집의 r g b 3가지 케이스가 있는데 dp테이블을 셋을 만들어야 하나 생각했다.
그냥 dp테이블을 2차원으로 만들면 해결되는 문제였다.
dp 생성 과정에서 min을 사용하면 하나의 경우를 제외하는 것인데
당장 비용이 높은 쪽을 선택하는게 나중에 전체적인 비용이 적을 수 있지 않나 하는 생각을 할 수 있다.
하지만 이 경우 dp[i][0]은 i번째 집은 r을 칠하는 것으로 고정이다. 
그럼 앞쪽에서는 작은 비용 큰 비용 어느 쪽을 선택하더라도 이후 비용에 영향을 미치지 않는다.
그래서 최소 비용을 선택해도 문제가 없다.
"""