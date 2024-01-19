# https://www.acmicpc.net/problem/21736
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
nxm 캠퍼스에서 상하좌우로 이동.
캠퍼스 내에서 만날 수 있는 사람 수를 출력하라.
O는 빈 공간, X는 벽, I는 플레이어, P는 사람.
아무도 만나지 못하면 TT 출력
"""
sys.setrecursionlimit(10**6)
def find_st():
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                return (i, j)
def dfs(r, c):
    global cnt
    if campus[r][c] == 'P':
        cnt += 1
    visited[r][c] = 1
    for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and campus[nr][nc] != 'X' and not visited[nr][nc]:
            dfs(nr, nc)
n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]
cnt = 0
visited = [[0] * m for _ in range(n)]
dfs(*find_st())
if cnt:
    print(cnt)
else:
    print('TT')


"""
현 시점 실버 2. 제출 7746. 정답률 61.229 %
dfs 재귀를 사용하면 python3를 사용하고 visited를 2차원 배열로 사용해야 통과된다.
visited에 set를 사용하거나 pypy3를 사용하면 시간초과가 발생한다.
"""