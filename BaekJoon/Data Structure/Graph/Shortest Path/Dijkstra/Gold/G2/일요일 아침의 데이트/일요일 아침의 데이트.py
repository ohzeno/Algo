# https://www.acmicpc.net/problem/1445
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
S 시작점, F 도착점, g는 쓰레기, .는 빈칸
쓰레기 칸을 최대한 적게 지나가야 하고, 그런 경로가 여럿이면
쓰레기 칸과 인접한 칸을 최대한 적게 지나가야 한다.
S, F는 세지 않는다. 지나가는 쓰레기 최소 개수, 쓰레기 인접 칸 최소 개수 출력.
"""
from heapq import heappush, heappop

lr, lc = map(int, input().split())
mat = [list(input()) for _ in range(lr)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for r in range(lr):
    for c in range(lc):
        if mat[r][c] == 'S':
            st = (r, c)
        elif mat[r][c] == 'g':
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < lr and 0 <= nc < lc and mat[nr][nc] == '.':
                    mat[nr][nc] = 'a'  # adjacent
def dijkstra():
    heap = [(0, 0, st[0], st[1])]  # 쓰레기 수, 인접 칸 수, r, c
    visited = {st}
    while heap:
        gcnt, acnt, r, c = heappop(heap)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < lr and 0 <= nc < lc and (nr, nc) not in visited:
                cell = mat[nr][nc]
                ngcnt, nacnt = gcnt, acnt
                if cell == 'g':
                    ngcnt += 1
                elif cell == 'a':
                    nacnt += 1
                elif cell == 'F':
                    return gcnt, acnt
                visited.add((nr, nc))
                heappush(heap, (ngcnt, nacnt, nr, nc))
print(*dijkstra())


"""
현 시점 Gold II. 제출 5473. 정답률 26.444 %
'인접' 정의가 없어서 좀 짜증났다. 예제를 보면 가로 세로 이동 가능 칸만 인접으로 취급하는 듯.
"""
