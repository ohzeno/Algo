# https://www.acmicpc.net/problem/1277
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
최소 전선 길이 추가하여 1번 n번 발전소를 연결하라.
안정성 문제로 어떠한 두 발전소 사이 전선 길이가 m을 초과할 수는 없다.
연결에 필요한 최소 전설 길이 * 1000, 버림 후 출력
"""
from heapq import heappush as hpush, heappop as hpop


def get_dist(p1, p2):
    return (abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2) ** 0.5


# n: 발전소 수,  w: 남아있는 전선 수
n, w = map(int, input().split())
m = float(input())  # m: 제한 길이
pos = {}  # 발전소 위치
connects = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    x, y = map(int, input().split())
    pos[i] = (x, y)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):  # 1부터 하면 중복됨. 그냥 dist 한번 구하고 대칭 저장.
        dist = get_dist(pos[i], pos[j])
        if dist <= m:  # 제한길이 넘지 않으면 기록
            connects[i].append((j, dist))
            connects[j].append((i, dist))
for _ in range(w):  # 추가 길이만 구하면 되므로, 이미 연결된 전선은 가중치 0으로 둔다.
    a, b = map(int, input().split())
    connects[a].append((b, 0))
    connects[b].append((a, 0))
dists = [float("inf")] * (n + 1)  # 1번에서 각 발전소까지의 최단 거리
q = [(0, 1)]  # cost, st
while q:  # 유사 다익스트라
    # 빠른 가지치기를 위해 누적 cost가 제일 작은 경우를 뽑음
    sm_cost, mid = hpop(q)
    if dists[mid] < sm_cost:  # 이미 더 작은 값이 있으면 넘어감
        continue
    # 현재 노드 경유하여 비용 갱신
    for ed, me_cost in connects[mid]:
        new_cost = sm_cost + me_cost
        if new_cost < dists[ed]:
            dists[ed] = new_cost
            hpush(q, (new_cost, ed))
print(int(dists[n] * 1000))

"""
현 시점 골드4. 제출 838, 정답률 29.383%
문제 설명에 문제가 있어 이해에 시간이 좀 걸렸다.
전선의 길이를 구하는 문제인데, 전선 길이를 어떻게 구하는지 나와있지 않다.
2차원 격자 좌표 상에서 전선을 잇는데, 직선 거리 한 칸이 거리 몇인지,
대각선 한 칸은 거리 몇인지 나와있지 않다.
미국 올림피아드 문제라는데 설명이 지나치게 부족하기에 좋은 문제는 아니다.
제한길이가 float인 점을 고려해 피타고라스 정리로 거리를 구했다.

오랜만에 다익스트라를 사용했는데, 알고리즘을 거의 잊고 있었다.

오랜만에 공부하는 김에 더 자주 사용되는 우선순위 큐 다익스트라로 변형해봤다.
방문행렬을 사용하지 않고 연결그래프를 사용한다.
기존 다익스트라는 하나의 경유노드씩 검토하는 bfs에 가깝지만 
이 경우는 매번 연결 노드 중 비용 감소가 이루어진 곳을 
다 때려박고 최소 코스트 노드를 뽑아서 사용한다.
dfs도 아니고 bfs도 아닌 형태. 
어쨋든 뽑혀나온 노드는 누적 코스트를 품고 있다.
"""
