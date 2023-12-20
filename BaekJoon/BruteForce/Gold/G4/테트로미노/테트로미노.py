# https://www.acmicpc.net/problem/14500
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
폴리오미노: 정사각형 여럿 이어붙인 도형
- 정사각형끼리 겹치면 안됨
- 도형은 모두 연결되어 있어야 함
- 정사각형은 변끼리 연결되어야 함.

정사각형 4개를 이어붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있음
https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14500/1.png
nxm인 종이 위에 테트로미노 하나 놓아서 칸에 쓰인 수의 합의 최대값을 구하라.
회전, 대칭 가능.
4 ≤ N, M ≤ 500
"""

def dfs(r, c, cnt, total):
    global max_total
    if total + (4 - cnt) * max_val <= max_total:
        return
    if cnt == 4:
        max_total = max(max_total, total)
        return
    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            if cnt == 2:  # ㅗ 모양
                # 셋째 칸 하나를 이미 방문한 상태에서 되돌아와서 둘째칸에서 다른 쪽으로 뻗음.
                dfs(r, c, cnt + 1, total + mat[nr][nc])
            dfs(nr, nc, cnt + 1, total + mat[nr][nc])
            visited[nr][nc] = 0

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_total = 0
max_val = max(map(max, mat))
for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, 1, mat[r][c])
        visited[r][c] = 0
print(max_total)


"""
현 시점 골드 4. 제출 84249. 정답률 36.218 %
ㅗ모양 때문에 둘째칸에서 처리를 추가해줄까 까지는 생각했으나 
방법을 생각할 시간에 하드코딩하는게 빠를 것 같아서 따로 ㅗ모양을 하드코딩으로 체크했다.
푼 이후 다른 풀이들을 보고 추가처리를 해줬다. 
그냥 단순히 방문처리, 점수에 더한 채로 둘째 칸에서 dfs를 다시 진행하면 되는거였다.
원소들이 자연수라 원본 배열에서 0이나 음수처리로 방문처리를 하면 더 빠르지만
가독성이 끔찍해지니 visited배열을 따로 만들어서 처리했다.
"""
