# https://www.acmicpc.net/problem/1504
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
무방향 그래프. 1번에서 n번으로 최단거리로 이동하려 함.
임의의 두 정점 v1, v2는 반드시 통과해야 한다.
v1 ≠ v2, v1 ≠ N, v2 ≠ 1
n: 정점 개수 2~800
e: 간선 개수 0~200_000
코스트 c: 1~1000
임의의 두 정점 사이에는 간선이 최대 1개 존재.
1에서 n까지 v1, v2를 거치는 최대 거리를 출력하라. 불가능하면 -1 출력. 
"""

def solution():
    n, e = map(int, input().split())
    if not e:
        return -1
    connects = [[] for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        connects[a].append((b, c))
        connects[b].append((a, c))
    v1, v2 = map(int, input().split())
    mat = {}
    for st in (v1, v2):
        dists = [float("inf")] * (n + 1)
        dists[st] = 0
        visited = [0] * (n + 1)
        visited[st] = 1
        for ed, cost in connects[st]:
            dists[ed] = cost
        for _ in range(n-1):
            min_value = float('inf')
            min_idx = 0
            for mid in range(1, n + 1):
                if not visited[mid] and dists[mid] < min_value:
                    min_value = dists[mid]
                    min_idx = mid
            visited[min_idx] = 1
            for ed, me_cost in connects[min_idx]:
                new_cost = dists[min_idx] + me_cost
                if not visited[ed] and new_cost < dists[ed]:
                    dists[ed] = new_cost
        mat[st] = dists
    p1 = mat[v1][1] + mat[v1][v2] + mat[v2][n]
    p2 = mat[v2][1] + mat[v2][v1] + mat[v1][n]
    ans = min(p1, p2)
    return ans if ans < float("inf") else -1


print(solution())

"""
현 시점 골드 4. 제출 82021. 정답률 	24.976 %
다익스트라 응용 문제. 정석 다익스트라 풀이
맞힌 사람, 숏코딩 Python 부문 1위.
v1, v2를 필수적으로 거쳐야 한다.
처음에는 경로 기록하는 bfs나 dfs가 생각났으나,
그러면 시간초과가 날 게 뻔하다.
경로단축 후 1-v1-v2-n, 1-v2-v1-n 중 최소값을 출력하면 된다.
왜 이 두 경로만 고려하냐면, 결국 1에서 출발하고 종점은 n이어야 하므로
v1, v2는 항상 그 사이에 존재할 수 밖에 없다.
v1, v2에서 출발하는 다익스트라만 구한다.
양방향 그래프이므로 1에서 v1, v2로 가는 비용은 v1, v2에서 1로 가는 비용과 같다.
"""
