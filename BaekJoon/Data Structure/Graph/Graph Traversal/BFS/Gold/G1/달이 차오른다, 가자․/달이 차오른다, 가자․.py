# https://www.acmicpc.net/problem/1194
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
.: 빈 칸
#: 벽
a~f: 항상 이동 가능. 처음 들어가면 열쇠 얻음
A~F: 대응 열쇠 있어야 이동 가능
0: 시작 위치
1: 출구
상하좌우 이동.
미로 탈출 최소 이동 횟수?
"""


from collections import deque

n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]
def get_st():
    for r in range(n):
        for c in range(m):
            if mat[r][c] == '0':
                return r, c
st_r, st_c = get_st()
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()
q = deque([(st_r, st_c, frozenset(), 0)])
visited.add((st_r, st_c, frozenset()))
ans = -1
while q:
    r, c, keys, dist = q.popleft()
    if mat[r][c] == '1':
        ans = dist
        break
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            cell = mat[nr][nc]
            if cell == '#':
                continue
            if cell.isupper() and cell.lower() not in keys:
                continue
            new_keys = keys
            if cell.islower():
                new_keys = keys | {cell}
            state = (nr, nc, new_keys)
            if state not in visited:
                visited.add(state)
                q.append((nr, nc, new_keys, dist + 1))
print(ans)


"""
현 시점 Gold I. 제출 20758. 정답률 40.167 %
열쇠가 소모품인지 아닌지 문제에 명시해야 한다.
"""
