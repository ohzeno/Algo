# https://www.acmicpc.net/problem/2580
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
스도쿠 퍼즐이 주어지면 마저 끝내라.
"""

mat = [list(map(int, input().split())) for _ in range(9)]
rows = [[False] * 10 for _ in range(9)]
cols = [[False] * 10 for _ in range(9)]
blocks = [[False] * 10 for _ in range(9)]
todo = []
for r in range(9):
    for c in range(9):
        if mat[r][c] != 0:
            val = mat[r][c]
            rows[r][val] = cols[c][val] = blocks[(r//3)*3 + c//3][val] = True
        else:
            todo.append((r, c))

def dfs(idx):
    if idx == l_todo:
        print('\n'.join([' '.join(map(str, row)) for row in mat]))
        sys.exit()
    r, c = todo[idx]
    row, col, block = rows[r], cols[c], blocks[(r//3)*3 + c//3]
    for i in range(1, 10):
        if not row[i] and not col[i] and not block[i]:
            row[i] = col[i] = block[i] = True
            mat[r][c] = i
            dfs(idx+1)
            row[i] = col[i] = block[i] = False
            mat[r][c] = 0

l_todo = len(todo)
dfs(0)

"""
현 시점 골드 4. 제출 100902. 정답률 27.023 %
간단한 dfs로 풀리는 초보적인 문제.
"""