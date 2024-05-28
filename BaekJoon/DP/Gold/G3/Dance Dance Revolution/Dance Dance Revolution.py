# https://www.acmicpc.net/problem/2342
import sys


sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
ddr게임.
상 좌 하 우: 1~4
가운데는 0. 처음에 게이머는 두 발 모두 중앙에 있다.
한 번에 하나의 발만 움직인다. 
처음을 제외하고 두 발이 같은 지점에 있는 것은 허락되지 않는다.
중앙에서 다른 지점으로 움직일 때 2의 힘이 든다.
다른 지점에서 인접한 지점(예를 들면 1에서 2나 4로)으로 움직일 때 3의 힘이 든다.
반대편으로 움직일 때 4의 힘이 든다(1에서 3이나 2에서 4로 등등).
같은 지점을 다시 밟을 때 1의 힘이 든다.

입력은 지시 사항으로 이루어진다. 마지막에는 0이 들어온다.
입력 수열 길이는 10만을 넘지 않는다.
모든 지시 사항을 만족하는 데 사용되는 최소의 힘을 출력하라.
"""


def cost(st, ed):
    if st == ed:
        return 1
    if st == 0:
        return 2
    if abs(st - ed) == 2:
        return 4
    return 3

def update(dp, orders, i):
    nxt = orders[i]
    cur_dp, nxt_dp = dp[i], dp[i+1]
    for ll in range(5):
        for rr in range(5):
            cur_cost = cur_dp[ll][rr]
            if cur_cost == INF:
                continue
            if nxt != rr:  # 왼발 움직이는 경우
                nxt_dp[nxt][rr] = min(
                    nxt_dp[nxt][rr],
                    cur_cost + cost(ll, nxt),
                )
            if nxt != ll:  # 오른발 움직이는 경우
                nxt_dp[ll][nxt] = min(
                    nxt_dp[ll][nxt],
                    cur_cost + cost(rr, nxt),
                )

def ddr_game(orders):
    n = len(orders)
    # dp[i][a][b]는 i-1번 명령 수행 후 왼발이 a, 오른발이 b에 있을 때의 최소 힘
    dp = [[[INF] * 5 for _ in range(5)] for _ in range(n + 1)]
    dp[0][0][0] = 0  # 초기 상태: 양 발이 중앙에 있음
    for i in range(n):
        update(dp, orders, i)
    return min(map(min, dp[n]))

INF = float("inf")
orders = list(map(int, input().split()))[:-1]
print(ddr_game(orders))

"""
현 시점 골드 3. 제출 13823. 정답률 38.309 %

3차원 배열을 사용하는게 더럽다고 생각해서 다른 풀이들을 좀 찾아봤는데
무려 1차원 배열 둘로 푸는 사람들이 있었다.
발이 아니라 위치에 도달하는 최소 비용을 저장하는 듯 한데,
직관적이지 않아서 그냥 넘겼다.

내 풀이도 dp배열을 n개 유지하지 않고 2개만 유지하면서 풀 수 있는데,
최적화에는 좋지만 이해하기엔 이게 편하고, 그렇게 느린 상태도 아니라 그냥 냅뒀다.
"""
