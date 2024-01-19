# https://www.acmicpc.net/problem/21736
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
nxm 캠퍼스에서 상하좌우로 이동.
캠퍼스 내에서 만날 수 있는 사람 수를 출력하라.
O는 빈 공간, X는 벽, I는 플레이어, P는 사람.
아무도 만나지 못하면 TT 출력
"""
from collections import deque
def find_st():
    for i in range(n):
        for j in range(m):
            if campus[i][j] == "I":
                q.append((i, j))
                visited[i][j] = 1
                return
n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]
q = deque()
visited = [[0] * m for _ in range(n)]
find_st()
cnt = 0
while q:
    r, c = q.popleft()
    if campus[r][c] == "P":
        cnt += 1
    for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and campus[nr][nc] != "X" and not visited[nr][nc]:
            q.append((nr, nc))
            visited[nr][nc] = 1
if cnt:
    print(cnt)
else:
    print("TT")


"""
현 시점 실버 2. 제출 7746. 정답률 61.229 %
bfs가 재귀 dfs보다 빠르고
visited는 set보다 2차원 배열이 빨랐다.
"""
