# https://www.acmicpc.net/problem/15683
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호
감시거리 inf. 벽 투시 못하지만 cctv는 투시함.
1: 한 방향. 우상좌하 1, 2, 3, 4
2: 양 방향  13, 24
3: 직각 두 방향 12, 23, 34, 14
4: 세 방향 123, 124, 134, 234
5: 네 방향
"""


def see_single_direction(mat, cctv, direction):
    # cctv의 위치와 방향에 따라 감시하는 영역을 #으로 변경
    r, c = cctv
    if direction == 0:  # 우
        for nc in range(c + 1, m):
            if mat[r][nc] == 6:
                break
            mat[r][nc] = '#'
    elif direction == 1:  # 상
        for nr in range(r - 1, -1, -1):
            if mat[nr][c] == 6:
                break
            mat[nr][c] = '#'
    elif direction == 2:  # 좌
        for nc in range(c - 1, -1, -1):
            if mat[r][nc] == 6:
                break
            mat[r][nc] = '#'
    elif direction == 3:  # 하
        for nr in range(r + 1, n):
            if mat[nr][c] == 6:
                break
            mat[nr][c] = '#'

def apply_cctv(mat, cctv, directions):
    # cctv의 위치와 방향에 따라 감시하는 영역을 #으로 변경
    for direction in directions:
        see_single_direction(mat, cctv, direction)

def count_empty(mat):
    # 사각지대 카운팅
    return sum(row.count(0) for row in mat)

def get_cctv_directions(cctv_type, rotation):
    # CCTV 종류와 회전에 따른 감시 방향들 반환
    # 방향: 0=우, 1=상, 2=좌, 3=하
    directions = {
        1: [
            [0], [1], [2], [3]  # 1번은 4가지 방향
        ],
        2: [
            [0, 2], [1, 3]  # 2번은 2가지 방향 (반대편)
        ],
        3: [
            [0, 1], [1, 2], [2, 3], [3, 0]  # 3번은 4가지 방향 (직각)
        ],
        4: [
            [0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]  # 4번은 4가지 방향 (3방향)
        ],
        5: [
            [0, 1, 2, 3]  # 5번은 1가지 방향 (4방향)
        ]
    }
    return directions[cctv_type][rotation]

# n은 세로, m은 가로
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

# cctv의 위치와 종류를 저장
cctv_list = []
for i in range(n):
    for j in range(m):
        if 1 <= mat[i][j] <= 5:
            cctv_list.append(((i, j), mat[i][j]))


def dfs(idx, cur_mat):
    global min_blind_spot

    if idx == len(cctv_list):
        # 모든 CCTV의 방향을 정했을 때
        blind_spots = count_empty(cur_mat)
        min_blind_spot = min(min_blind_spot, blind_spots)
        return

    pos, cctv_type = cctv_list[idx]

    # 해당 CCTV 타입의 모든 가능한 회전에 대해 시도
    max_rotations = 4
    if cctv_type == 2:
        max_rotations = 2  # 2번 CCTV는 2가지 회전만 가능
    elif cctv_type == 3:
        max_rotations = 4  # 3번 CCTV는 4가지 회전 가능
    elif cctv_type == 4:
        max_rotations = 4  # 4번 CCTV는 4가지 회전 가능
    elif cctv_type == 5:
        max_rotations = 1  # 5번 CCTV는 회전이 필요 없음

    for rotation in range(max_rotations):
        # 현재 맵 상태를 복사
        tmp_mat = [cur_mat[i][:] for i in range(n)]

        # 현재 CCTV에 대해 감시 적용
        directions = get_cctv_directions(cctv_type, rotation)
        apply_cctv(tmp_mat, pos, directions)

        # 다음 CCTV로 재귀
        dfs(idx + 1, tmp_mat)


min_blind_spot = 64

# DFS로 모든 경우의 수 탐색
dfs(0, mat)
print(min_blind_spot)


"""
현 시점 Gold III. 제출 60893. 정답률 45.628 %
지금은 mat 매번 복사하고, 직접 see적용하는데
생각해보니 그냥 see 좌표들을 set로 모아서 n*m에서 빼면 된다.
지금 당장 구현할 수도 있지만 시간이 없어서 다음 기회에.
"""
