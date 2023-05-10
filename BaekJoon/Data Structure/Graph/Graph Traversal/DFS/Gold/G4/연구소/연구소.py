# https://www.acmicpc.net/problem/14502
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
3 <= n, m <= 8
0은 빈 칸, 1은 벽, 2는 바이러스
바이러스는 상하좌우로 퍼져나감
벽 3개를 추가로 세워서 바이러스를 막아야함(빈 칸 최소 3개 주어짐)
바이러스가 퍼진 후 남은 0 갯수가 안전 영역의 크기임.
최대 안전 영역 크기를 구하라.
"""
from itertools import combinations
def virus_dfs(r, c):
    global infected
    if init_zeros - infected < max_safe:  # 최대 안전구역 확보 못하면 리턴.
        return
    visited.add((r, c))
    tmp_mat[r][c] = 2
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and tmp_mat[nr][nc] == 0:
            infected += 1  # 최초 바이러스는 이미 init_zeros에 반영된 것이니 셀 필요 없음.
            virus_dfs(nr, nc)
n, m = map(int, input().split())
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
mat = [list(map(int, input().split())) for _ in range(n)]
zeros, viruses = [], []
init_zeros, init_viruses = -3, 0  # 벽 3개를 세우므로 init_zeros는 미리 3을 빼놓음.
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            zeros.append((i, j))
            init_zeros += 1
        elif mat[i][j] == 2:
            viruses.append((i, j))
            init_viruses += 1
max_safe = 0
for case in combinations(zeros, 3):
    tmp_mat = [row[:] for row in mat]  # 얕은 복사이므로 줄 각각에 대해 복사해야함.
    for i, j in case:  # 벽 세우기
        tmp_mat[i][j] = 1
    visited = set()
    infected = 0
    for r, c in viruses:  # 바이러스 퍼뜨리기
        virus_dfs(r, c)
    safe = init_zeros - infected
    max_safe = max(max_safe, safe)
print(max_safe)

"""
현 시점 골드4. 제출 81027. 정답률 54.837%
평범한 구현 문제. dfs/bfs와 브루트포스를 사용한다.
"""