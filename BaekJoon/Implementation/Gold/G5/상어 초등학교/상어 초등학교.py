# https://www.acmicpc.net/problem/21608
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
좌상단 1,1 우하단 N,N
선생은 학생의 순서를 정했음. 각 학생이 좋아하는 4명도 조사했음.
상하좌우는 인접칸.
1. 비어있는 칸 중 인접한 칸에 좋아하는 학생이 가장 많은 칸.
2. 1을 만족하는 칸이 여럿이면, 인접한 칸 중 비어있는 칸이 가장 많은 칸.
3. 2를 만족하는 칸도 여럿이면, 행의 번호가 가장 작은 칸. 그래도 여럿이면 열의 번호가 가장 작은 칸.
인접칸에 좋아하는 학생 수가 0이면 만족도 0
1이면 1, 2면 10, 3면 100, 4면 1000
학생 총 만족도?
좋아하는 학생은 모두 다른 학생으로 이루어짐. 자기 자신을 좋아하는 경우X
"""

n = int(input())
datas = [list(map(int, input().split())) for _ in range(n**2)]
# 0, n+1을 만들어서 인덱싱을 편하게 하도록 했다.
mat = [[0] * (n + 2) for _ in range(n + 2)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상
stu_likes = {}
for stu, f1, f2, f3, f4 in datas:
    stu_likes[stu] = [f1, f2, f3, f4]  # 학생별 좋아하는 친구들
    candis = []  # 배정자리 후보
    for r in range(1, n+1):
        for c in range(1, n+1):
            if not mat[r][c]:  # 비어있는 자리만
                like, empty = 0, 0
                for i in range(4):
                    nr, nc = r + dirs[i][0], c + dirs[i][1]
                    if 1 <= nr <= n and 1 <= nc <= n:  # 범위 이내일 때
                        if mat[nr][nc] in stu_likes[stu]:
                            like += 1
                        if not mat[nr][nc]:
                            empty += 1
                candis.append((like, empty, r, c))
    # like, empty는 내림차순, r, c는 오름차순으로 정렬
    candis.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    mat[candis[0][2]][candis[0][3]] = stu  # 첫 원소가 규칙에 따른 배정 자리.
ans = 0
for r in range(1, n+1):
    for c in range(1, n + 1):
        like = 0
        for i in range(4):
            nr, nc = r + dirs[i][0], c + dirs[i][1]
            if 1 <= nr <= n and 1 <= nc <= n:
                if mat[nr][nc] in stu_likes[mat[r][c]]:
                    like += 1
        if like:  # 점수 부여
            ans += 10 ** (like - 1)
print(ans)


"""
현 시점 골드5. 제출 13193 정답률 40.472 %
일단 무식하게 구현했는데, 케이스가 많아서 자꾸 놓치는 조건들 때문에 몇 번 틀렸다.
~~시간이 없어 일단 첫 통과본을 깃에 올리고, 추후 코드를 개선해볼 생각이다.~~
이전에는 각 조건을 체크한 후 다시 순회를 돌고는 했는데,
이번에는 한 번의 순회동안 like, empty를 체크하고, candis에 append에 기록한 후
candis를 정렬하여 자리를 배정했다.
점수도 다시 보니 10의 제곱이라 길이를 줄일 수 있었다.
"""