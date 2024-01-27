# https://www.acmicpc.net/problem/2667
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
정사각형 모양 지도. 1은 집 있음, 0은 집 없음.
연결된 집은 단지. 대각선은 연결된거 아님.
지도가 주어질 때 단지 수와 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하라.
5 <= N <= 25
"""
n = int(input())
mat = [list(map(int, input())) for _ in range(n)]
visited = set()
groups = {}


def dfs(r, c):
    visited.add((r, c))
    groups[g_num] += 1
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and mat[nr][nc] and (nr, nc) not in visited:
            dfs(nr, nc)


cnt_g = 0
for r in range(n):
    for c in range(n):
        if mat[r][c] and (r, c) not in visited:
            cnt_g += 1
            g_num = cnt_g
            groups[g_num] = 0
            dfs(r, c)
print(cnt_g)
for val in sorted(groups.values()):
    print(val)


"""
현 시점 실버 1. 제출 174956. 정답률 42.343 %
간단한 그래프 탐색 문제.
"""
