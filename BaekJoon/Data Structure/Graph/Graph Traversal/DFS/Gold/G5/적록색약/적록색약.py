# https://www.acmicpc.net/problem/10026
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
적록색약은 R과 G를 구분하지 못한다.
R, G, B로 이루어진 그리드가 주어졌을 때, 적록색약과 일반인이 구분하는 구역의 수를 출력하라.
"""
def dfs(r, c, color, is_blind=False):
    if is_blind:
        visited['blind'].add((r, c))
    else:
        visited['normal'].add((r, c))
    for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if is_blind:
                if (nr, nc) not in visited['blind'] and mat[nr][nc] != 'B':
                    dfs(nr, nc, color, is_blind)
            else:
                if (nr, nc) not in visited['normal'] and mat[nr][nc] == color:
                    dfs(nr, nc, color)

n = int(input())
mat = [list(input()) for _ in range(n)]
visited = {'normal': set(), 'blind': set()}
cnt = {'normal': 0, 'blind': 0}
for r in range(n):
    for c in range(n):
        if (r, c) not in visited['normal']:
            if mat[r][c] == 'B':  # B는 색약이 봐도 구분되니 dfs 중복 필요없다.
                cnt['blind'] += 1
            dfs(r, c, mat[r][c])
            cnt['normal'] += 1
        if (r, c) not in visited['blind'] and mat[r][c] != 'B':
            dfs(r, c, mat[r][c], True)
            cnt['blind'] += 1
print(cnt['normal'], cnt['blind'])


"""
현 시점 골드 5. 제출 61081. 정답률 56.387 %
처음에는 첫 순회 dfs후 visited를 초기화하고 G를 전부 R로 바꾸고 다시 순회를 했다.
순회를 세번이나 하는게 맘에 안들어서 visited를 따로 두고 dfs에 is_blind를 추가해서
한 번의 순회에서 dfs를 두 번 돌리는 방식으로 바꿨다.
B는 노멀에서 처음 방문할 때 blind에도 카운트해주면 다시 방문하지 않아도 된다.
"""