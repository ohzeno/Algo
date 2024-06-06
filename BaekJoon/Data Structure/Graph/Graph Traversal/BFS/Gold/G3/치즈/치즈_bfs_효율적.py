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

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q, nq = deque([(0, 0)]), deque()
t = 0
while q or nq:
    if not q:  # air_field가 비었으면 시간 지남
        q, nq = nq, q
        t += 1
    r, c = q.popleft()
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if not mat[nr][nc]:  # 공기면 방문처리, q에 넣기
                mat[nr][nc] = -1
                q.append((nr, nc))
            elif mat[nr][nc] > 0:  # 치즈면 접촉 횟수 증가
                mat[nr][nc] += 1
                if mat[nr][nc] >= 3:  # 2면 이상 접촉하면 녹음
                    mat[nr][nc] = -1  # 녹은 치즈는 공기로 바꿈
                    nq.append((nr, nc))  # 다음 타임에 녹은 치즈의 주변을 탐색
print(t)


"""
현 시점 골드 3. 제출 28976. 정답률 46.052 %
bfs 과정에서 -1로 visited 처리, +=1로 접촉 처리를 해서
시간마다 공기 영역을 다시 탐색하지 않도록 바꿨다.
훨씬 빨라졌다.

로직에서 한가지 신경쓰일 수 있는 부분이, q가 비어야 시간이 지났다고 판단하는 점이다.
만약 세 면이 공기와 접촉하는 치즈가 공기를 막고 있다면, 
세번째 접근에서 q에 넣어버려서 안쪽 공기까지 
한 타임에 처리해버릴 수 있으리라 생각할 수 있다. 
하지만 bfs이므로 한 칸씩 이동하기 때문에, 한 점에서 출발한 이상 
한 타임에 한 블럭의 3방향을 모두 탐색할 수는 없다.
"""