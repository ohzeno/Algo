# https://www.acmicpc.net/problem/2638
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
nxm 모눈종이 위에 얇은 치즈가 퍼져있다.
치즈는 2변 이상 실내온도 공기와 접촉하면 한시간 만에 녹아 없어진다.
치즈에 둘러싸인 공간의 공기와는 접촉해도 괜찮다.
모눈종이 테두리에는 치즈가 놓이지 않는다.
입력으로 주어진 치즈가 모두 녹아 없어지는 데 걸리는 시간을 출력하라.
"""
from collections import deque

def get_air_field():
    q = deque([(0, 0)])
    air_field = [[False] * m for _ in range(n)]
    air_field[0][0] = True
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not air_field[nr][nc] and mat[nr][nc] == 0:
                air_field[nr][nc] = True
                q.append((nr, nc))
    return air_field

def melt_cheese():
    air_field = get_air_field()
    for r, c in list(cheese):
        if not mat[r][c]:
            continue
        air_cnt = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if air_field[nr][nc]:
                air_cnt += 1
        if air_cnt >= 2:
            mat[r][c] = 0
            cheese.remove((r, c))

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cheese = set()
for r in range(n):
    for c in range(m):
        if mat[r][c] == 1:
            cheese.add((r, c))
t = 0
while cheese:
    melt_cheese()
    t += 1
print(t)


"""
현 시점 골드 3. 제출 28976. 정답률 46.052 %
비효율적이지만 매번 공기를 bfs로 다시 찾는 방법으로 일단 풀었다.
제거한 치즈를 공기에 추가하는 것 만으로는 공기 영역을 업데이트 할 수 없다. 
치즈에 둘러싸여 있던 부분들도 새로 공기에 포함되어야 하기 때문이다.
"""