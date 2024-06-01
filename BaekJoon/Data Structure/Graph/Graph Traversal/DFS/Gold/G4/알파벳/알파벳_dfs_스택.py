# https://www.acmicpc.net/problem/1987
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
rxc 크기의 보드. 각 칸은 대문자 알파벳.
좌상단에는 말이 놓여있음.
말은 상하좌우로 인접한 네 칸 중 한 칸으로 이동 가능.
같은 알파벳이 적힌 칸을 두 번 지날 수 없음.
최대 몇 칸을 지날 수 있는지 출력하라. 좌상단도 칸 수에 포함.
1 <= r, c <= 20
"""

R, C = map(int, input().split())
mat = [input() for _ in range(R)]
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
max_cnt = 1
stack = [(0, 0, 1, mat[0][0])]
visited = [[set()] * C for _ in range(R)]
while stack:
    r, c, cnt, used = stack.pop()
    if max_cnt < cnt:
        max_cnt = cnt
    if cnt == 26:
        break
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] not in used:
            new_s = used + mat[nr][nc]
            if new_s not in visited[nr][nc]:
                visited[nr][nc].add(new_s)
                stack.append((nr, nc, cnt + 1, new_s))
print(max_cnt)


"""
현 시점 실버 1. 제출 950. 정답률 31.761 %
"""
