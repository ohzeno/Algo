# https://www.acmicpc.net/problem/1865
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
n개 노드. m개 도로와 w개 웜홀.
도로는 양방향, 웜홀은 단방향.
웜홀을 지나면 시간이 되돌아감.
출발점으로 돌아왔을 때, 출발 시각보다 이전인 경우가 있는지 구하라.
1 <= n <= 500
1 <= m <= 2500
1 <= w <= 200
0 <= t <= 10_000
"""


def bellman_ford(n, graph):
    dist = [0] * (n + 1)
    for i in range(n):
        for mid in graph:
            for ed, me_cost in graph[mid]:
                if (new_cost := dist[mid] + me_cost) < dist[ed]:
                    if i == n - 1:
                        return True
                    dist[ed] = new_cost
    return False


def solution():
    n, m, w = map(int, input().split())
    graph = {}
    for i in range(m):
        s, e, t = map(int, input().split())
        graph.setdefault(s, []).append((e, t))
        graph.setdefault(e, []).append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.setdefault(s, []).append((e, -t))
    if bellman_ford(n, graph):
        return "YES"
    return "NO"


for _ in range(int(input())):
    print(solution())


"""
현 시점 골드 3. 제출 50347. 정답률 21.485 %
벨만 포드 알고리즘 변형.

넷상의 풀이글들은 죄다 코드를 이해하지 못해서 설명이 없거나 잘못됐다.
그리고 대부분의 풀이는 벨만포드 알고리즘을 잘못 구현한 것이다.

모든 점에서 출발하는 로직을 사용하는데, 그게 왜 작동하는지에 대한 증명을 못찾았다.
국내는 물론이고 USACO 2006 December 해설에서도 
'증명할 수 있지만 연습으로 남겨둠'같은 말만 있다.
국내 마스터 유저의 해설에는 아예 그 부분 증명의 필요성조차 언급이 없고,
그냥 그렇게 하면 풀린다는 식으로 적어놨다.

이해를 위해 벨만포드 알고리즘 자체를 공부했고,
위키백과(https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)의 증명을 읽어봤다.

증명에 논리적 결함이 있어서 출처인 스탠포드 교육자료 pdf의 증명파트를 읽어봤다.
거기에도 같은 설명이 적혀있어서 pdf 전체를 다시 읽어봤다.
pdf의 증명은 옳지만, 증명한 로직이 위키의 수도코드와 달랐다.

변형 관련 내용은 md파일에 적어뒀다.
"""
