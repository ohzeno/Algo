# https://www.acmicpc.net/problem/21425
import sys
sys.stdin = open('input.txt')
# def input():
#     return sys.stdin.readline().rstrip()
def input():
    line = sys.stdin.readline().rstrip()
    while not line:  # 본래 빈 줄로 층 구분하는 것이 규칙이나 백준의 input 데이터에 오류가 있어서 이렇게 통과했다.
        line = sys.stdin.readline().rstrip()
    return line
"""
h레벨(층)의 미궁 최상층에서 깨어남.
각 층은 m*n 크기의 격자로 이루어져 있음.
일부 격자에는 기둥이 있어 들어갈 수 없음.
왕자는 동일한 층의 인접한 격자로만 이동할 수 있고 5초가 걸림.
최하층에 있지 않다면 왕자는 바닥을 부숴 아래층으로 내려갈 수 있고 5초가 걸림.
악당 자파르와의 결혼을 거부한 공주가 최하층 한 구역에서 왕자를 기다림
공주를 만나기 위해 필요한 최소 시간을 구하라.
첫 줄: 높이, 층의 가로/세로 크기 2 <= h, m, n <= 50
다음 각각 블럭 위에서부터 설명하는 h블럭 정보.
각 블록에는 m개의 줄과 n개의 문자가 있음.
'.'은 자유구간
'o'는 기둥
'1'은 왕자의 시작 위치
'2'는 공주의 위치
각 블록은 빈 줄로 구분함.
"""
from collections import deque
def bfs(h, m, n, levels):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    visited.add((0, st_x, st_y))
    queue = deque([(0, st_x, st_y, 0)])
    while queue:
        lv, x, y, time = queue.popleft()
        if levels[lv][x][y] == '2':
            return time
        for dr, dc in moves:
            nr, nc = x + dr, y + dc
            if 0 <= nr < m and 0 <= nc < n and (lv, nr, nc) not in visited and levels[lv][nr][nc] != 'o':
                visited.add((lv, nr, nc))
                queue.append((lv, nr, nc, time + 5))
        if lv + 1 < h and levels[lv + 1][x][y] != 'o':
            if (lv + 1, x, y) not in visited:
                visited.add((lv + 1, x, y))
                queue.append((lv + 1, x, y, time + 5))

h, m, n = map(int, input().split())
levels = []
for i in range(h):
    levels.append(tuple(input() for _ in range(m)))
    # if i != h-1:
    #     input()  # 빈 줄로 층 구분
suc = 0
for x in range(m):
    for y in range(n):
        if levels[0][x][y] == '1':
            st_x, st_y = x, y
            suc = 1
            break
    if suc:
        break
print(bfs(h, m, n, levels))

"""
현 시점 골드5. 제출 80, 정답률 24.074%
예시에 나온 input과 실제 input이 다르다.
또한 input값이 원 문제와 달라서 파이썬으로 풀면 IndexError가 발생한다.
원 문제가 있는 러시아 사이트에서는 같은 코드로 통과된다.
전형적인 bfs 문제.

input함수 자체에서 빈 줄이 나오면 다음 줄을 읽도록 수정하니 문제가 해결되었다.
아마 블럭 구분하는 빈 줄이 하나여야 하는데, 둘 이상의 빈 줄이 입력된 경우가 있는 것 같다.
결국 python, pypy 최초 통과자가 되었다.
"""
