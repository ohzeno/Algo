# https://www.acmicpc.net/problem/1238
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
n개 마을 각각에 한 명의 학생이 살고 있다.
전원이 x번 마을에 모여 파티를 벌이려 함.
1 <= x <= n
이 마을 사이에는 총 m개의 단방향 도로들이 있고 i번째 길을 지나는 데 Ti(1 <= Ti <= 100) 시간이 걸림.
각 학생들은 파티에 참석 후 다시 돌아가야 함.
오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하라.
1 <= n <= 1_000, 1 <= m <= 10_000
"""
n, m, x = map(int, input().split())
mat = [[float("inf")] * (n + 1) for _ in range(n + 1)]
rev = [[float("inf")] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    mat[a][b] = t
    rev[b][a] = t  # 역방향 그래프

def dijkstra(st, mat):
    visited = [0] * (n + 1)
    visited[st] = 1
    for _ in range(n - 1):
        min_value = float("inf")
        min_idx = 0
        for mid in range(1, n + 1):
            if not visited[mid] and mat[st][mid] < min_value:
                min_value = mat[st][mid]
                min_idx = mid
        visited[min_idx] = 1
        for ed in range(1, n + 1):
            new_dist = mat[st][min_idx] + mat[min_idx][ed]
            if not visited[ed] and new_dist < mat[st][ed]:
                mat[st][ed] = new_dist

dijkstra(x, mat)
dijkstra(x, rev)  # 각 노드에서 x로 가는 최단거리
max_time = 0
for i in range(1, n + 1):
    if i == x:  # 파티 장소에 사는 사람은 제외
        continue
    go, back = rev[x][i], mat[x][i]
    max_time = max(max_time, go + back)
print(max_time)


"""
현 시점 골드 3. 제출 46144. 정답률 48.539 %
처음에는 모든 정점 사이를 구해야하니 플로이드-워셜이 아닌가 했다.
그러면 시간초과.
다익스트라를 양방향으로 돌리면 된다.
정방향의 경우 x를 출발점으로 하면 x에서 돌아오는 거리를 구할 수 있다.
파티 장소로 가는 경우는 역방향 그래프에서 x에서 출발하면 된다.

증명이 궁금했지만 아니나 다를까 내가 찾아본 모든 블로그, 질문 게시판 답변자는
'뒤집으면 된다'라고만 답변한다. 아무도 그 사실을 증명하거나 구체적으로 설명하지 않았다.

제일 먼저, 역방향으로 기록하고 다익스트라를 돌리면 
'정방향'에서 가능한 경로단축이 불가능해지지 않을까 의문이 생겼다. 반대도 마찬가지.
대부분의 단방향 논리는 역이 성립하지 않기 때문에 든 의문.
그렇게되면 정방향 i->x가 역방향 x->i와 다를 수 있다.

정방향 그래프에서, i->x로 가는 모든 경로는 연속적이다. 불연속 그래프가 아니라는 뜻.
그리고 각 경로는 역방향 그래프에서도 성립한다. 각 노드 사이의 길을 전부 뒤집었기에 성립.
각 경로는 구성 노드가 같고, 순서만 역순이 되고, 가중치도 같다.
그러므로 정방향 그래프에서 각 노드에서 x로 가는 최단경로는 
역방향 그래프에서 x에서 각 노드로 가는 최단경로와 같다.

그러므로 단 두번의 다익스트라로 해결 가능하다.
"""
