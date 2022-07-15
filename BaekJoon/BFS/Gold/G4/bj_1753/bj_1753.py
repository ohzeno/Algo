# https://www.acmicpc.net/problem/1753
import sys
import heapq
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def bfs(st):
    q = []
    # 가중치, 노드. heapq가 우선 첫 원소 오름차순으로 정렬시키므로 가중치 우선.
    # 다익스트라에선 확인하지 않은 노드 중 가중치가 작은 것부터 확인함.
    # 다익스트라라고 인터넷에 올라온 이와 비슷한 풀이가 많은데 효과는 비슷해도 과정이 다르다.
    # 다익스트라를 참고한 bfs라고 보는게 맞을 듯 하다.
    heapq.heappush(q, (0, st))
    while q:
        cost, now = heapq.heappop(q)
        if not dist[now] < cost:  # 직접 연결 비용보다 낮으면 이미 갱신된거임. 유사 visited 효과
            for node in mat[now]:  # 현재 노드와 연결된 노드만 확인
                new_cost = cost + node[1]  # 현재 노드와 연결노드를 잇는 가중치 + 이전까지의 경로에서 쌓인 가중치
                if new_cost < dist[node[0]]:  # 누적 가중치가 st - 목적지 직접 연결보다 낮으면 갱신
                    dist[node[0]] = new_cost
                    heapq.heappush(q, (new_cost, node[0]))  # 연결노드를 누적 가중치와 함께 현재노드로 넣는다.
                    # 다음 순회에 연결노드를 거쳐가는 가중치를 계산하게 됨.

n_node, n_road = map(int, input().split())
st = int(input())
mat = [[] for _ in range(n_node + 1)]  # 메모리초과로 연결노드만
inf = float('inf')
dist = [inf] * (n_node + 1)
dist[st] = 0  # 자신에게 가는 비용 0
for i in range(n_road):
    a, b, c = map(int, input().split())
    mat[a].append((b, c))  # a>b 가중치 c
bfs(st)
for i in range(1, n_node + 1):
    if dist[i] == inf:
        print('INF')
    else:
        print(dist[i])

