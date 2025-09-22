# https://www.acmicpc.net/problem/1106
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
1 <= c <= 1000, 1 <= N <= 20
"""

C, N = map(int, input().split())
INF = float('inf')
# dp[i] = i명의 고객을 늘리기 위한 최소 비용
# '적어도 C명'. 비용당 고객 최대 100이니 여유분 둬야함.
C_ext = C + 101
dp = [INF] * C_ext
dp[0] = 0  # 0명을 늘리는 데 드는 비용은 0

cities = []
for _ in range(N):
    cost, customer = map(int, input().split())
    cities.append((cost, customer))

# 무한 배낭 문제 해법
for cost, customer in cities:
    # customer만큼 더해야하니 customer부터 순회.
    for i in range(customer, C_ext):
        if dp[i - customer] != INF:
            dp[i] = min(dp[i], dp[i - customer] + cost)

# C명 이상을 달성하는 최소 비용 찾기
# dp[C]가 INF일 수 있고, 더 많은 고객 수에서 비용이 더 작을 수 있어서 모두 확인해야함
print(min(dp[C:]))

"""
현 시점 Gold IV. 제출 19721. 정답률 39.301 %
배낭 문제를 이때까지 2문제밖에 안풀어봤다는 것을 알게됐다.
분명 dp 관련해서 많이 들어본 것 같은데...

dp라는건 이해했지만 처음에는 2차원 배열을 생각했다.
2차원 배열로 풀려고 하니 고객 수가 무한히 클 수 있다는 것 때문에 
dp배열 정의를 어떻게 해야할지 감이 잡히지 않았다.
골드 4에서 막히니 오랜만에 멍청해진 기분이었다.
결국 문제 카테고리를 확인하고 공부했다.

이전에 푼 문제들도 보니 
무한 배낭 문제는 포기하고 풀이를 찾아봤었고 0/1은 고생해서 푼 듯 하다.
dp는 항상 까다롭다.
"""
