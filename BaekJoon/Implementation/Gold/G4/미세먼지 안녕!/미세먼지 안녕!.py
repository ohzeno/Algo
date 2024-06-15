# https://www.acmicpc.net/problem/17144
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
공기청정기는 항상 1열(첫열)에 설치. 두 행 차지.
1초 동안 일어나는 일
  1. 미세먼지 확산
    - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
    - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 확산 X
    - 확산되는 양은 Ar,c // 5
    - 확산 후 Ar,c에 남는 미세먼지의 양은 Ar,c - (Ar,c // 5) * (확산된 방향의 개수)
  2. 공기청정기 작동
    - 공기청정기에서 바람이 나옴
    - 위칸을 포함한 상위 절반 테두리는 반시계 방향, 
        아래쪽은 시계 방향으로 바람을 불어 대기를 정화
    - 바람의 방향대로 미세먼지가 모두 한 칸씩 이동
    - 공기청정기에서 부는 바람은 미세먼지가 없는 바람, 공기청정기로 들어간 미세먼지는 모두 정화됨

첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 
공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. 
-1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
"""
from collections import deque


def find_air_cleaner():
    for r in range(R):
        if mat[r][0] == -1:
            return (r, 0), (r + 1, 0)


def get_rotate_pos_li():
    sr = air_cleaner[0][0]
    upper = find_rotate_pos(sr, 0, -1)
    lower = find_rotate_pos(sr+1, 0, 1)
    return upper, lower


def find_rotate_pos(sx, sy, d):
    pos_li = [(sx, sy)]
    cr, cc = sx, sy
    i = 0
    while True:
        dr, dc = dirs[i]
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < R and 0 <= nc < C:
            if nr == sx and nc == sy:
                break
            pos_li.append((nr, nc))
            cr, cc = nr, nc
        else:
            i = (i + d) % 4
    return pos_li


def spread():
    q = deque()
    for r in range(R):
        for c in range(C):
            if mat[r][c] <= 0:
                continue
            amount = mat[r][c] // 5
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] != -1:
                    q.append((nr, nc, amount))
                    mat[r][c] -= amount
    while q:
        r, c, amount = q.popleft()
        mat[r][c] += amount


def air_clean():
    rotated_upper, rotated_lower = map(get_rotated_air, (upper, lower))
    push_air(upper, l_upper, rotated_upper)
    push_air(lower, l_lower, rotated_lower)


def get_rotated_air(pos):
    q = deque()
    for r, c in pos:
        q.append(mat[r][c])
    q.rotate(1)
    return q


def push_air(pos, l_pos, q):
    q.popleft()
    for i in range(1, l_pos):
        val = q.popleft()
        if val == -1:
            val = 0
        r, c = pos[i]
        mat[r][c] = val


R, C, T = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(R)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
air_cleaner = find_air_cleaner()
upper, lower = get_rotate_pos_li()
l_upper, l_lower = len(upper), len(lower)
for _ in range(T):
    spread()
    air_clean()
print(sum(sum(mat, [])) + 2)


"""
현 시점 골드 4. 제출 40689. 정답률 55.207 %
쉽고 재밌는 문제.
더 빠른 풀이들은 맵을 1차원 배열로 사용하고, 회전 부분을 변수 둘 교환으로 구현해놨다.
하지만 그런 풀이들은 덜직관적이라 시도 안해봤다.
골드4 주제에 함수가 7개나 나왔다. 풀이 시간을 생각하면 레벨 좀 높여야 하지 않나 싶다.
"""
