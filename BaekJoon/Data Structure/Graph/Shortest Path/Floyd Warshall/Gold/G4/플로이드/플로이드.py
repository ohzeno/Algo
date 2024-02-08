# https://www.acmicpc.net/problem/11404
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n개 도시, m개 버스.
모든 도시 쌍에 대해 이동 최소비용 구하라.
"""

n, m = int(input()), int(input())
mat = [[float('inf') if r != c else 0 for c in range(n+1)] for r in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    mat[a][b] = min(mat[a][b], c)  # 중복 있음
# 중계 지점 가장 바깥 루프로.
for mid in range(1, n + 1):
    for st in range(1, n + 1):
        for ed in range(1, n + 1):
            mat[st][ed] = min(mat[st][ed], mat[st][mid] + mat[mid][ed])
for st in range(1, n + 1):
    for ed in range(1, n + 1):
        if mat[st][ed] == float('inf'):  # 갈 수 없는 경우 0으로
            mat[st][ed] = 0
for st in range(1, n + 1):
    print(*mat[st][1:])

"""
골드4. 제출 51207, 정답률 41.660 % // 문제풀고 커밋하기 전에 깃 실수로 파일을 날려먹었다. 다음날 확인한 데이터임.
오랜만에 플로이드 워셜을 풀어서 중계지점 루프를 가장 밖에 둬야 한다는 점을 깜빡했었다.
"""