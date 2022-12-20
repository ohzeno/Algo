# https://www.acmicpc.net/problem/13549
import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    q = []
    heappush(q, (0, st))
    while q:
        cost, target = heappop(q)
        if not dist[target] < cost:  # 현재 위치 비용이 이미 작으면 의미없음.
            for node in [target - 1, target + 1, target * 2]:  # 이동 가능 위치
                if 0 <= node <= ed * 2:  # 범위를 벗어나지 않는 선에서
                    if dist[node] > cost:  # 가중치 갱신이 필요하면
                        if node == target * 2:  # 순간이동이면 추가비용 없음
                            dist[node] = cost
                        else:  # 걸어가면 1 추가비용
                            dist[node] = cost + 1
                        heappush(q, (dist[node], node))  # 다음 노드 경유하는 경로 체크

st, ed = map(int, input().split())
"""
다른 사람들은 10만 개의 원소를 만들어두었던데 어차피 목적지 * 2 초과는 체크할 일이 없다.
"""
dist = [i for i in range(ed * 2 + 1)]
if st >= ed:  # 수빈이 위치가 동생과 같거나 크면 차이만큼 걸어갈 수 밖에 없다.
    print(st - ed)
else:
    bfs()
    print(dist[ed])


