# https://www.acmicpc.net/problem/14929
import sys
from collections import deque
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
다익스트라 연습문제로 찾은 문제다. 다익스트라로 풀면 메모리 초과가 된다.
다익스트라로 풀었다고 주장하는 많은 풀이들이 있지만 내용을 보면 
다익스트라가 아니라 bfs 변형이다.
다익스트라는 방문하지 않은 노드 중 연결가중치가 가장 낮은 노드순으로 중계노드로 지정하여 
다음 노드까지의 가중치 갱신을 확인한다.
인터넷에 올라온 풀이들은 그런 과정이 없고 그냥 직접 연결된 노드들을 순서대로 탐색하며 
가중치 갱신이 이루어진 노드들을 중계노드로 큐에 넣어 bfs처럼 사용한다.
아니나 다를까 난이도 기여에 가보면 플레 ~ 루비 유저들이 하나같이 
다익스트라가 아니라 bfs 문제라고 의견을 냈다.

다익스트라로 풀면 메모리초과가 발생하기에 연결노드만을 기록하여 bfs를 변형하여 사용했다.
"""

# def dijkstra(st):
#     inf = 300000 ** 2
#     mat = [[inf] * (n_city + 1) for _ in range(n_city + 1)]
#     for _ in range(n_road):
#         a, b = map(int, input().split())
#         mat[a][b] = 1
#     visited = [0] * (n_city + 1)
#     visited[st] = 1
#     for _ in range(n_city - 1):
#         min_d = inf
#         min_idx = 0
#         # 방문한 적 없는 도시 중 가중치가 가장 낮은 도시 찾기
#         for j in range(1, n_city + 1):
#             if mat[st][j] < min_d and not visited[j]:
#                 min_d = mat[st][j]
#                 min_idx = j
#         visited[min_idx] = 1
#         # 해당 도시를 경유하여 가중치 갱신
#         for k in range(1, n_city + 1):
#             new_distance = mat[st][min_idx] + mat[min_idx][k]
#             if not visited[k] and new_distance < mat[st][k]:
#                 mat[st][k] = new_distance
#     return mat[st]  # 출발 도시의 가중치 목록 리턴
#
# n_city, n_road, distance, st = map(int, input().split())
# dis = dijkstra(st)
# end = 0
# for i in range(1, n_city + 1):
#     if dis[i] == distance:
#         print(i)
#         end = 1
# if not end:
#     print(-1)

def bfs(st):
    ans = []
    inf = 300000 ** 2
    mat = [[] for _ in range(n_city + 1)]
    for _ in range(n_road):
        a, b = map(int, input().split())
        mat[a].append(b)  # 0 쓰면 메모리 초과라 직접 연결된 도시만 사용.
    cost = [inf] * (n_city + 1)  # cost[i] = st에서 i도시까지의 최단거리
    cost[st] = 0
    q = deque([[0, st]])  # 현재 거리, 도시
    while q:
        count, node = q.popleft()
        for next_node in mat[node]:  # 현재 도시와 연결된 도시들에 대해
            # 방문한 적 없고 최단거리 갱신해야 할 도시면
            if not visited[next_node] and count + 1 < cost[next_node]:
                cost[next_node] = count + 1  # 최단거리 갱신
                visited[next_node] = 1  # 방문처리
                q.append([count + 1, next_node])
                # 최단거리가 바뀌었으므로 해당 노드와 연결된 다른 도시들도 갱신의 여지가 있음.
                # 그러므로 q에 추가해서 경유지로 사용. 유사 다익스트라
    for i in range(1, n_city + 1):
        if cost[i] == distance:
            ans.append(i)
    return ans

n_city, n_road, distance, st = map(int, input().split())
visited = [0] * (n_city + 1)
visited[st] = 1
dis = bfs(st)
if dis:
    for now in dis:
        print(now)
else:  # 최단거리가 distance인 도시가 없을 경우
    print(-1)

