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
mat = [[0] * (n + 2) for _ in range(n + 2)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상
stu_likes = {}
for stu, f1, f2, f3, f4 in datas:
    stu_likes[stu] = [f1, f2, f3, f4]
    likes = {}
    max_likes = 0
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if not mat[r][c]:
                like = 0
                for i in range(4):
                    nr, nc = r + dirs[i][0], c + dirs[i][1]
                    if mat[nr][nc] in stu_likes[stu]:
                        like += 1
                if like >= max_likes:
                    max_likes = like
                    likes.setdefault(max_likes, []).append((r, c))
    if max_likes and len(likes[max_likes]) == 1:
        mat[likes[max_likes][0][0]][likes[max_likes][0][1]] = stu
    else:
        max_empty = 0
        empties = {}
        if not max_likes:
            for r in range(1, n + 1):
                for c in range(1, n + 1):
                    if not mat[r][c]:
                        empty = 0
                        for i in range(4):
                            nr, nc = r + dirs[i][0], c + dirs[i][1]
                            if ((1 <= nr <= n) and (1 <= nc <= n)) and not mat[nr][nc]:
                                empty += 1
                        if empty >= max_empty:
                            max_empty = empty
                            empties.setdefault(max_empty, []).append((r, c))
                        else:
                            empties.setdefault(empty, []).append((r, c))
        else:
            for r, c in likes[max_likes]:
                empty = 0
                for i in range(4):
                    nr, nc = r + dirs[i][0], c + dirs[i][1]
                    if ((1 <= nr <= n) and (1 <= nc <= n)) and not mat[nr][nc]:
                        empty += 1
                if empty >= max_empty:
                    max_empty = empty
                    empties.setdefault(max_empty, []).append((r, c))
                else:
                    empties.setdefault(empty, []).append((r, c))
        if len(empties[max_empty]) == 1:
            mat[empties[max_empty][0][0]][empties[max_empty][0][1]] = stu
        else:
            empties[max_empty].sort()
            mat[empties[max_empty][0][0]][empties[max_empty][0][1]] = stu
tot_sati = 0
for r in range(1, n + 1):
    for c in range(1, n + 1):
        if mat[r][c]:
            like = 0
            for i in range(4):
                nr, nc = r + dirs[i][0], c + dirs[i][1]
                if mat[nr][nc] in stu_likes[mat[r][c]]:
                    like += 1
            if like == 1:
                tot_sati += 1
            elif like == 2:
                tot_sati += 10
            elif like == 3:
                tot_sati += 100
            elif like == 4:
                tot_sati += 1000
print(tot_sati)

"""
현 시점 골드5. 제출 13193 정답률 40.472 %
일단 무식하게 구현했는데, 케이스가 많아서 자꾸 놓치는 조건들 때문에 몇 번 틀렸다.
시간이 없어 일단 원본을 깃에 올리고, 추후 코드를 개선해볼 생각이다.
"""