# https://www.acmicpc.net/problem/2239
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
스도쿠 퍼즐이 주어지면 마저 끝내라.
답이 여럿이라면 81자리 수가 제일 작은 경우를 출력하라.
"""


mat = [list(map(int, input())) for _ in range(9)]
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
        print('\n'.join([''.join(map(str, row)) for row in mat]))
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
현 시점 골드 4. 제출 23931. 정답률 45.845 %
까다롭다, 어렵다는 사람들 반응과 달리 그냥 간단한 dfs로 풀리는 초보적인 문제.

바로 풀긴 했는데, 훨씬 빠른 풀이들이 있다.
칸마다 가능한 숫자 세트를 두고 관리하는 듯 한데,
코드가 엄청 길고 난잡해져서 이해하기 어려웠다.
시간 단축 효과에 비해 가독성 희생이 심각해서 그냥 패스했다.
"""