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


n, e = map(int, input().split())
if not e:
    print(-1)
    exit()
INF = 200_000 * 1_000 * 2 + 10
mat = [[INF if r != c else 0 for c in range(n+1)] for r in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    mat[a][b] = mat[b][a] = c
v1, v2 = map(int, input().split())
for mid in range(1, n + 1):
    for st in range(1, n + 1):
        for ed in range(1, n + 1):
            if mat[st][mid] + mat[mid][ed] < mat[st][ed]:
                mat[st][ed] = mat[st][mid] + mat[mid][ed]
p1 = mat[1][v1] + mat[v1][v2] + mat[v2][n]
p2 = mat[1][v2] + mat[v2][v1] + mat[v1][n]
ans = min(p1, p2)
print(ans if ans < INF else -1)

"""
현 시점 골드 4. 제출 82021. 정답률 	24.976 %
다익스트라 응용 문제. 플로이드 워셜 풀이.
맞힌 사람, 숏코딩 Python 부문 1위.
v1, v2를 필수적으로 거쳐야 한다.
처음에는 경로 기록하는 bfs나 dfs가 생각났으나,
그러면 시간초과가 날 게 뻔하다.
경로단축 후 1-v1-v2-n, 1-v2-v1-n 중 최소값을 출력하면 된다.
왜 이 두 경로만 고려하냐면, 결국 1에서 출발하고 종점은 n이어야 하므로
v1, v2는 항상 그 사이에 존재할 수 밖에 없다.

플로이드 워셜은 다익스트라와 달리 모든 정점간의 최단거리를 구해야 하므로 시간복잡도가 높다.
우스운 점은, 
이 풀이에서 INF값으로 정수 대신 INF = float('inf')를 사용하면 시간초과 된다.
혹은 해당 로직을 그대로 solution함수에 넣고, print(solution())으로 출력해도 시간초과.
로직 변경 없이 
함수호출 단 한번, 혹은 float('inf') 호출만으로 시간초과가 나는 것은
명백히 사이트가 시간 제한 설정을 잘못한 것이다.
"""
