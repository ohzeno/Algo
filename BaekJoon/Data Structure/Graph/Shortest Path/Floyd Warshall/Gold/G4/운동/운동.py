# https://www.acmicpc.net/problem/1956
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
V개 마을, E개 도로. 도로는 일방 통행.
마을은 1~V번.
시작점으로 돌아오는 사이클. 사이클 도로 길이 합 최소.
두 마을 왕복하는 경우도 사이클.
"""

v, e = map(int, input().split())
mat = [[float('inf')] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    mat[a][b] = c  # 중복 없음
for mid in range(1, v + 1):
    for st in range(1, v + 1):
        for ed in range(1, v + 1):
            # st != ed는 사용하지 않았다. 자신에게 돌아오는 사이클 비용을 구해야 하기 때문.
            if st != mid != ed:
                mat[st][ed] = min(mat[st][ed], mat[st][mid] + mat[mid][ed])
ans = float('inf')
for i in range(1, v + 1):
    ans = min(ans, mat[i][i])  # 각 노드에서 자신에게 돌아오는 사이클 비용 비교
print(ans if ans != float('inf') else -1)  # 없으면 -1

"""
현 시점 골드4. 제출 17014, 정답률 40.296 %
플로이드 워셜로 풀었고, python3로는 시간초과 발생.
python3로 통과한 풀이를 상당수 살펴봤는데, 전부 heqpq와 다익스트라를 이용한 풀이였다.
플로이드 워셜로는 pypy로 제출해야 할 듯.
다익스트라 풀이도 시도해볼 예정.
다익스트라 이용한 풀이도 작성해 올려뒀다.
순수 다익스트라 풀이는 시간초과가 발생한다. 다익스트라와 bfs를 응용하여 풀었다.
python3로 통과한 기존 풀이들도 다시 살펴보니 다익스트라와 bfs를 응용하였다.
"""