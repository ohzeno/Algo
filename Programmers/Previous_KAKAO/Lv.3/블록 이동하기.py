# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque
def solution(board):
    # 로봇은 2x1 크기. n,n까지 이동
    # 좌상단은 1,1임. 0은 빈공간, 1은 벽
    # 좌표는 (세로, 가로)
    # (1, 1), (1, 2)에 놓여있는 채로 시작.
    # 이동은 가로/세로 유지하며 이동. 한 칸이라도 n,n에 닿으면 됨.
    # 한 칸을 축으로 회전 가능. 회전방향에 벽이 없어야함.
    # 이동/회전에 1초 소모.  도달에 걸리는 최소 시간 리턴
    # board 한 변 길이 5~100, 원소는 0/1
    # 목적지에 도달하지 못하는 경우는 주어지지 않음.
    n = len(board)
    def is_ok(r, c):  # 해당 좌표가 맵을 벗어나지 않고 벽이 아니라면 True 리턴하는 함수.
        if 0 <= r < n and 0 <= c < n and not board[r][c]:
            return True
        return False

    def shift(r1, c1, r2, c2, type):
        # 좌 우 상 하
        # 하축 좌우회전
        # 좌축 좌우회전
        # 상축 좌우회전
        # 우축 좌우회전
        nr1, nr2, nc1, nc2 = -1, -1, -1, -1
        if type < 4:  # 회전 아닌 경우
            if type == 0:  # 좌
                nr1, nr2 = r1, r2
                nc1, nc2 = c1 - 1, c2 - 1
            elif type == 1:  # 우
                nr1, nr2 = r1, r2
                nc1, nc2 = c1 + 1, c2 + 1
            elif type == 2:  # 상
                nr1, nr2 = r1 - 1, r2 - 1
                nc1, nc2 = c1, c2
            elif type == 3:  # 하
                nr1, nr2 = r1 + 1, r2 + 1
                nc1, nc2 = c1, c2
        else:  # 회전의 경우
            if c1 == c2:  # 세로인 경우만
                minr, maxr = min(r1, r2), max(r1, r2)
                if type == 4:  # 하축 좌회전
                    if 0 <= minr < n and 0 <= c1 - 1 < n and not board[minr][c1 - 1]:  # 왼쪽 위가 비어있으면
                        nr1, nr2 = maxr, maxr
                        nc1, nc2 = c1 - 1, c2
                elif type == 5:  # 하축 우회전
                    if 0 <= minr < n and 0 <= c1 + 1 < n and not board[minr][c1 + 1]:  # 오른쪽 위가 비어있으면
                        nr1, nr2 = maxr, maxr
                        nc1, nc2 = c1, c2 + 1
                elif type == 6:  # 상축 좌회전
                    if 0 <= maxr < n and 0 <= c2 - 1 < n and not board[maxr][c2 - 1]:  # 왼쪽 아래가 비어있으면
                        nr1, nr2 = minr, minr
                        nc1, nc2 = c1 - 1, c2
                elif type == 7:  # 상축 우회전
                    if 0 <= maxr < n and 0 <= c2 + 1 < n and not board[maxr][c2 + 1]:  # 오른쪽 아래가 비어있으면
                        nr1, nr2 = minr, minr
                        nc1, nc2 = c1, c2 + 1
            else:  # 가로인 경우만
                minc, maxc = min(c1, c2), max(c1, c2)
                if type == 8:  # 좌축 좌회전
                    if 0 <= r2 - 1 < n and 0 <= maxc < n and not board[r2 - 1][maxc]:  # 오른쪽 위가 비어있으면
                        nr1, nr2 = r1 - 1, r2
                        nc1, nc2 = minc, minc
                elif type == 9:  # 좌축 우회전
                    if 0 <= r2 + 1 < n and 0 <= maxc < n and not board[r2 + 1][maxc]:  # 오른쪽 아래가 비어있으면
                        nr1, nr2 = r1, r2 + 1
                        nc1, nc2 = minc, minc
                elif type == 10:  # 우축 좌회전
                    if 0 <= r1 + 1 < n and 0 <= minc < n and not board[r1 + 1][minc]:  # 왼쪽 아래가 비어있으면
                        nr1, nr2 = r1, r2 + 1
                        nc1, nc2 = maxc, maxc
                elif type == 11:  # 우축 우회전
                    if 0 <= r1 - 1 < n and 0 <= minc < n and not board[r1 - 1][minc]:  # 왼쪽 위가 비어있으면
                        nr1, nr2 = r1 - 1, r2
                        nc1, nc2 = maxc, maxc
        if is_ok(nr1, nc1) and is_ok(nr2, nc2):  # 해당 좌표들로 이동 가능하면 리턴
            return ((nr1, nc1), (nr2, nc2))
        return False  # 불가하면 False 리턴

    def check(rc1, rc2):
        r1, c1 = rc1
        r2, c2 = rc2
        possible = []
        for i in range(12):  # 가능한 모든 움직임에 대해 체크
            data = shift(r1, c1, r2, c2, i)
            if data:  # 이동 가능하면 추가
                possible.append(data)
        return possible  # rc1, rc2에서 이동 가능한 모든 좌표 리스트 리턴

    visited = set()
    visited.add(((0, 0), (0, 1)))
    q = deque()
    q.append(((0, 0), (0, 1), 0))
    while q:
        nrc1, nrc2, t = q.popleft()
        if nrc1 == (n - 1, n - 1) or nrc2 == (n - 1, n - 1):  # 목표지점이면
            return t  # bfs이므로 최초 if문이 최단시간임.
        datas = check(nrc1, nrc2)
        for data in datas:  # 현 좌표에서 이동 가능한 모든 좌표
            if not data in visited:  # 방문한 적 없으면
                visited.add(data)  # 방문처리. shift에서 정렬되므로 바로 넣으면 됨.
                q.append((data[0], data[1], t + 1))  # 다음 이동 좌표, 소모한 시간 업데이트


inputdatas = [
    [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
]

"""
2020 카카오 공채 기출. Lv.3.
옮겨적기, 문제 이해에 7분 소모했다. 처음엔 dfs로 할지 bfs로 할지 고민했다.
시간제한 얘기가 없고 딱히 보드가 크지 않아 보여서 dfs부터 해봤다.
106분에 dfs 초안 제출. 회전때문에 구현이 너무 많았고 좌표가 헷갈려서 오래걸렸다.
테케 1~3번 제외하고 전부 시간초과.
110분에 bfs 제출. 통과.
정답률 24%인 이유가 아마 구현할게 많고 노가다가 많아서 실수가 많아 그럴 듯 하다.
시험 시간 안에 풀지 못한 사람이 꽤 많을거라 생각한다.
아이디어 자체는 기본적인 bfs문제와 같다 느낀다.
"""

# dfs 풀이
import sys
sys.setrecursionlimit(10**9)
def solution2(board):
    # 로봇은 2x1 크기. n,n까지 이동
    # 좌상단은 1,1임. 0은 빈공간, 1은 벽
    # 좌표는 (세로, 가로)
    # (1, 1), (1, 2)에 놓여있는 채로 시작.
    # 이동은 가로/세로 유지하며 이동. 한 칸이라도 n,n에 닿으면 됨.
    # 한 칸을 축으로 회전 가능. 회전방향에 벽이 없어야함.
    # 이동/회전에 1초 소모.  도달에 걸리는 최소 시간 리턴
    # board 한 변 길이 5~100, 원소는 0/1
    # 목적지에 도달하지 못하는 경우는 주어지지 않음.
    n = len(board)
    def is_ok(r, c):
        if 0 <= r < n and 0 <= c < n and not board[r][c]:
            return True
        return False
    def shift(r1, c1, r2, c2, type):
        # 좌 우 상 하
        # 하축 좌우회전
        # 좌축 좌우회전
        # 상축 좌우회전
        # 우축 좌우회전
        if type < 4:  # 회전 아닌 경우
            if type == 0:  # 좌
                nr1, nr2 = r1, r2
                nc1, nc2 = c1 - 1, c2 - 1
            elif type == 1:  # 우
                nr1, nr2 = r1, r2
                nc1, nc2 = c1 + 1, c2 + 1
            elif type == 2:  # 상
                nr1, nr2 = r1 - 1, r2 - 1
                nc1, nc2 = c1, c2
            elif type == 3:  # 하
                nr1, nr2 = r1 + 1, r2 + 1
                nc1, nc2 = c1, c2
        else:
            nr1, nr2, nc1, nc2 = -1, -1, -1, -1
            if c1 == c2:  # 세로인 경우만
                minr = min(r1, r2)
                maxr = max(r1, r2)
                if type == 4:  # 하축 좌회전
                    if 0 <= minr < n and 0 <= c1 - 1 < n and not board[minr][c1 - 1]:  # 왼쪽 위가 비어있으면
                        nr1, nr2 = maxr, maxr
                        nc1, nc2 = c1 - 1, c2
                elif type == 5:  # 하축 우회전
                    if 0 <= minr < n and 0 <= c1 + 1 < n and not board[minr][c1 + 1]:  # 오른쪽 위가 비어있으면
                        nr1, nr2 = maxr, maxr
                        nc1, nc2 = c1, c2 + 1
                elif type == 6:  # 상축 좌회전
                    if 0 <= maxr < n and 0 <= c2 - 1 < n and not board[maxr][c2 - 1]:  # 왼쪽 아래가 비어있으면
                        nr1, nr2 = minr, minr
                        nc1, nc2 = c1 - 1, c2
                elif type == 7:  # 상축 우회전
                    if 0 <= maxr < n and 0 <= c2 + 1 < n and not board[maxr][c2 + 1]:  # 오른쪽 아래가 비어있으면
                        nr1, nr2 = minr, minr
                        nc1, nc2 = c1, c2 + 1
            else:  # 가로인 경우만
                minc = min(c1, c2)
                maxc = max(c1, c2)
                if type == 8:  # 좌축 좌회전
                    if 0 <= r2 - 1 < n and 0 <= maxc < n and not board[r2 - 1][maxc]:  # 오른쪽 위가 비어있으면
                        nr1, nr2 = r1 - 1, r2
                        nc1, nc2 = minc, minc
                elif type == 9:  # 좌축 우회전
                    if 0 <= r2 + 1 < n and 0 <= maxc < n and not board[r2 + 1][maxc]:  # 오른쪽 아래가 비어있으면
                        nr1, nr2 = r1, r2 + 1
                        nc1, nc2 = minc, minc
                elif type == 10:  # 우축 좌회전
                    if 0 <= r1 + 1 < n and 0 <= minc < n and not board[r1 + 1][minc]:  # 왼쪽 아래가 비어있으면
                        nr1, nr2 = r1, r2 + 1
                        nc1, nc2 = maxc, maxc
                elif type == 11:  # 우축 우회전
                    if 0 <= r1 - 1 < n and 0 <= minc < n and not board[r1 - 1][minc]:  # 왼쪽 위가 비어있으면
                        nr1, nr2 = r1 - 1, r2
                        nc1, nc2 = maxc, maxc
        if is_ok(nr1, nc1) and is_ok(nr2, nc2):
            return ((nr1, nc1), (nr2, nc2))
        return False
    def check(rc1, rc2):
        # 좌 우 상 하
        # 좌축 우회전 좌회전
        # 우축 좌회전 우회전
        r1, c1 = rc1
        r2, c2 = rc2
        possible = []
        for i in range(12):
            datas = shift(r1, c1, r2, c2, i)
            if datas and datas not in visited:
                possible.append(datas)
        return possible
    def dfs(rc1, rc2, t):
        if rc1 == (n - 1, n - 1) or rc2 == (n - 1, n - 1):
            if t < min_t[0]:
                min_t[0] = t
            return
        datas = check(rc1, rc2)
        for data in datas:
            if not data in visited:
                visited.add(data)
                dfs(data[0], data[1], t + 1)
                visited.remove(data)
    visited = set()
    visited.add(((0, 0), (0, 1)))
    min_t = [float('inf')]
    dfs((0, 0), (0, 1), 0)
    return min_t[0]

for t in inputdatas:
    print(solution(t))
