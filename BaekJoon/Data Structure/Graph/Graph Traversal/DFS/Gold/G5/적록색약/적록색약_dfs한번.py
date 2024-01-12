# https://www.acmicpc.net/problem/10026
import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
적록색약은 R과 G를 구분하지 못한다.
R, G, B로 이루어진 그리드가 주어졌을 때, 적록색약과 일반인이 구분하는 구역의 수를 출력하라.
"""


def dfs(r, c, is_blind=False):
    color = mat[r][c]
    if not is_blind:  # 색약 dfs 방문은 normal에 기록하지 않는다.
        visited["normal"].add((r, c))
    visited["blind"].add((r, c))
    for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if mat[nr][nc] == color:  # 색이 같은 경우
                if not is_blind and (nr, nc) not in visited["normal"]:
                    dfs(nr, nc)
                elif is_blind and (nr, nc) not in visited["blind"]:
                    dfs(nr, nc, True)
            else:  # 색이 다르면
                # 현재, 다음이 B가 아닌 경우에만 색약 dfs에 진입한다.
                if (
                    color != "B"
                    and mat[nr][nc] != "B"
                    and (nr, nc) not in visited["blind"]
                ):
                    dfs(nr, nc, True)


n = int(input())
mat = [list(input()) for _ in range(n)]
visited = {"normal": set(), "blind": set()}
cnt = {"normal": 0, "blind": 0}
for r in range(n):
    for c in range(n):
        if (r, c) not in visited["normal"]:
            # B는 normal에서 방문처리하니 처음 나온 B는 blind에도 카운트한다.
            # B가 아니고 색약 dfs에서 처리되지도 않았으면 첫 방문이니 blind에도 카운트한다.
            if mat[r][c] == "B" or (r, c) not in visited["blind"]:
                cnt["blind"] += 1
            dfs(r, c)
            cnt["normal"] += 1
print(cnt["normal"], cnt["blind"])


"""
현 시점 골드 5. 제출 61081. 정답률 56.387 %
처음에는 첫 순회 dfs후 visited를 초기화하고 G를 전부 R로 바꾸고 다시 순회를 했다.
순회를 세번이나 하는게 맘에 안들어서 visited를 따로 두고 dfs에 is_blind를 추가해서
한 번의 순회에서 dfs를 두 번 돌리는 방식으로 바꿨다.
B는 노멀에서 처음 방문할 때 blind에도 카운트해주면 다시 방문하지 않아도 된다.

dfs 중복이 맘에 안들어서 바꿨다.
기존 방법은 한 순회에서 dfs를 두 번 돌리는 방식이었다.
지금 방법은 한 순회에서 dfs를 한 번 돌리고, 
    dfs 내에서 r과 g 경계일 때 blind dfs에 진입한다.
dfs 내 분기문을 간략화할 수는 있지만 직관적이지 않아서 그대로 두었다.
"""
