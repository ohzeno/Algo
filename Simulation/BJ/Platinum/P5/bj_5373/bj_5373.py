# https://www.acmicpc.net/problem/5373
import sys

sys.stdin = open("input.txt")

# 삼성 SW 기출
# 설명할 내용이 없다...B의 윗쪽은 처음과 마찬가지로 흰색 중앙이 있는 방향.
# D의 0행은 F방향.
# 회전하는 9개 큐브의 모든 면 값을 바꿈. 노가다풀이.
def rot(side, direction):
    if side == 'U':
        if direction == '+':
            up[0][0], up[0][1], up[0][2], \
            up[0][2], up[1][2], up[2][2], \
            up[2][2], up[2][1], up[2][0], \
            up[2][0], up[1][0], up[0][0], \
            bk[0][2], bk[0][1], bk[0][0], \
            ri[0][2], ri[0][1], ri[0][0], \
            fr[0][2], fr[0][1], fr[0][0], \
            lf[0][2], lf[0][1], lf[0][0] = \
                up[2][0], up[1][0], up[0][0], \
                up[0][0], up[0][1], up[0][2], \
                up[0][2], up[1][2], up[2][2], \
                up[2][2], up[2][1], up[2][0], \
                lf[0][2], lf[0][1], lf[0][0], \
                bk[0][2], bk[0][1], bk[0][0], \
                ri[0][2], ri[0][1], ri[0][0], \
                fr[0][2], fr[0][1], fr[0][0]
        elif direction == '-':
            up[0][0], up[0][1], up[0][2], \
            up[0][2], up[1][2], up[2][2], \
            up[2][2], up[2][1], up[2][0], \
            up[2][0], up[1][0], up[0][0], \
            bk[0][2], bk[0][1], bk[0][0], \
            ri[0][2], ri[0][1], ri[0][0], \
            fr[0][2], fr[0][1], fr[0][0], \
            lf[0][2], lf[0][1], lf[0][0] = \
                up[0][2], up[1][2], up[2][2], \
                up[2][2], up[2][1], up[2][0], \
                up[2][0], up[1][0], up[0][0], \
                up[0][0], up[0][1], up[0][2], \
                ri[0][2], ri[0][1], ri[0][0], \
                fr[0][2], fr[0][1], fr[0][0], \
                lf[0][2], lf[0][1], lf[0][0], \
                bk[0][2], bk[0][1], bk[0][0]
    elif side == 'D':
        if direction == '+':
            dn[0][0], dn[0][1], dn[0][2], \
            dn[0][2], dn[1][2], dn[2][2], \
            dn[2][2], dn[2][1], dn[2][0], \
            dn[2][0], dn[1][0], dn[0][0], \
            fr[2][0], fr[2][1], fr[2][2], \
            ri[2][0], ri[2][1], ri[2][2], \
            bk[2][0], bk[2][1], bk[2][2], \
            lf[2][0], lf[2][1], lf[2][2] = \
                dn[2][0], dn[1][0], dn[0][0], \
                dn[0][0], dn[0][1], dn[0][2], \
                dn[0][2], dn[1][2], dn[2][2], \
                dn[2][2], dn[2][1], dn[2][0], \
                lf[2][0], lf[2][1], lf[2][2], \
                fr[2][0], fr[2][1], fr[2][2], \
                ri[2][0], ri[2][1], ri[2][2], \
                bk[2][0], bk[2][1], bk[2][2],
        elif direction == '-':
            dn[0][0], dn[0][1], dn[0][2], \
            dn[0][2], dn[1][2], dn[2][2], \
            dn[2][2], dn[2][1], dn[2][0], \
            dn[2][0], dn[1][0], dn[0][0], \
            fr[2][0], fr[2][1], fr[2][2], \
            ri[2][0], ri[2][1], ri[2][2], \
            bk[2][0], bk[2][1], bk[2][2], \
            lf[2][0], lf[2][1], lf[2][2] = \
                dn[0][2], dn[1][2], dn[2][2], \
                dn[2][2], dn[2][1], dn[2][0], \
                dn[2][0], dn[1][0], dn[0][0], \
                dn[0][0], dn[0][1], dn[0][2], \
                ri[2][0], ri[2][1], ri[2][2], \
                bk[2][0], bk[2][1], bk[2][2], \
                lf[2][0], lf[2][1], lf[2][2], \
                fr[2][0], fr[2][1], fr[2][2]
    elif side == 'F':
        if direction == '+':
            fr[0][0], fr[0][1], fr[0][2], \
            fr[0][2], fr[1][2], fr[2][2], \
            fr[2][2], fr[2][1], fr[2][0], \
            fr[2][0], fr[1][0], fr[0][0], \
            up[2][0], up[2][1], up[2][2],\
            ri[0][0], ri[1][0], ri[2][0], \
            dn[0][2], dn[0][1], dn[0][0], \
            lf[2][2], lf[1][2], lf[0][2] = \
                fr[2][0], fr[1][0], fr[0][0], \
                fr[0][0], fr[0][1], fr[0][2], \
                fr[0][2], fr[1][2], fr[2][2], \
                fr[2][2], fr[2][1], fr[2][0], \
                lf[2][2], lf[1][2], lf[0][2], \
                up[2][0], up[2][1], up[2][2], \
                ri[0][0], ri[1][0], ri[2][0], \
                dn[0][2], dn[0][1], dn[0][0]
        elif direction == '-':
            fr[0][0], fr[0][1], fr[0][2], \
            fr[0][2], fr[1][2], fr[2][2], \
            fr[2][2], fr[2][1], fr[2][0], \
            fr[2][0], fr[1][0], fr[0][0], \
            up[2][0], up[2][1], up[2][2], \
            ri[0][0], ri[1][0], ri[2][0], \
            dn[0][2], dn[0][1], dn[0][0], \
            lf[2][2], lf[1][2], lf[0][2] = \
                fr[0][2], fr[1][2], fr[2][2], \
                fr[2][2], fr[2][1], fr[2][0], \
                fr[2][0], fr[1][0], fr[0][0], \
                fr[0][0], fr[0][1], fr[0][2], \
                ri[0][0], ri[1][0], ri[2][0], \
                dn[0][2], dn[0][1], dn[0][0], \
                lf[2][2], lf[1][2], lf[0][2], \
                up[2][0], up[2][1], up[2][2]
    elif side == 'B':
        if direction == '+':
            bk[0][0], bk[0][1], bk[0][2], \
            bk[0][2], bk[1][2], bk[2][2], \
            bk[2][2], bk[2][1], bk[2][0], \
            bk[2][0], bk[1][0], bk[0][0], \
            up[0][2], up[0][1], up[0][0], \
            lf[0][0], lf[1][0], lf[2][0], \
            dn[2][0], dn[2][1], dn[2][2], \
            ri[2][2], ri[1][2], ri[0][2] = \
                bk[2][0], bk[1][0], bk[0][0], \
                bk[0][0], bk[0][1], bk[0][2], \
                bk[0][2], bk[1][2], bk[2][2], \
                bk[2][2], bk[2][1], bk[2][0], \
                ri[2][2], ri[1][2], ri[0][2], \
                up[0][2], up[0][1], up[0][0], \
                lf[0][0], lf[1][0], lf[2][0], \
                dn[2][0], dn[2][1], dn[2][2]
        elif direction == '-':
            bk[0][0], bk[0][1], bk[0][2], \
            bk[0][2], bk[1][2], bk[2][2], \
            bk[2][2], bk[2][1], bk[2][0], \
            bk[2][0], bk[1][0], bk[0][0], \
            up[0][2], up[0][1], up[0][0], \
            lf[0][0], lf[1][0], lf[2][0], \
            dn[2][0], dn[2][1], dn[2][2], \
            ri[2][2], ri[1][2], ri[0][2] = \
                bk[0][2], bk[1][2], bk[2][2], \
                bk[2][2], bk[2][1], bk[2][0], \
                bk[2][0], bk[1][0], bk[0][0], \
                bk[0][0], bk[0][1], bk[0][2], \
                lf[0][0], lf[1][0], lf[2][0], \
                dn[2][0], dn[2][1], dn[2][2], \
                ri[2][2], ri[1][2], ri[0][2], \
                up[0][2], up[0][1], up[0][0]
    elif side == 'L':
        if direction == '+':
            lf[0][0], lf[0][1], lf[0][2], \
            lf[0][2], lf[1][2], lf[2][2], \
            lf[2][2], lf[2][1], lf[2][0], \
            lf[2][0], lf[1][0], lf[0][0], \
            up[0][0], up[1][0], up[2][0], \
            fr[0][0], fr[1][0], fr[2][0], \
            dn[0][0], dn[1][0], dn[2][0], \
            bk[2][2], bk[1][2], bk[0][2] = \
                lf[2][0], lf[1][0], lf[0][0], \
                lf[0][0], lf[0][1], lf[0][2], \
                lf[0][2], lf[1][2], lf[2][2], \
                lf[2][2], lf[2][1], lf[2][0], \
                bk[2][2], bk[1][2], bk[0][2], \
                up[0][0], up[1][0], up[2][0], \
                fr[0][0], fr[1][0], fr[2][0], \
                dn[0][0], dn[1][0], dn[2][0]
        elif direction == '-':
            lf[0][0], lf[0][1], lf[0][2], \
            lf[0][2], lf[1][2], lf[2][2], \
            lf[2][2], lf[2][1], lf[2][0], \
            lf[2][0], lf[1][0], lf[0][0], \
            up[0][0], up[1][0], up[2][0], \
            fr[0][0], fr[1][0], fr[2][0], \
            dn[0][0], dn[1][0], dn[2][0], \
            bk[2][2], bk[1][2], bk[0][2] = \
                lf[0][2], lf[1][2], lf[2][2], \
                lf[2][2], lf[2][1], lf[2][0], \
                lf[2][0], lf[1][0], lf[0][0], \
                lf[0][0], lf[0][1], lf[0][2], \
                fr[0][0], fr[1][0], fr[2][0], \
                dn[0][0], dn[1][0], dn[2][0], \
                bk[2][2], bk[1][2], bk[0][2], \
                up[0][0], up[1][0], up[2][0]
    elif side == 'R':
        if direction == '+':
            ri[0][0], ri[0][1], ri[0][2], \
            ri[0][2], ri[1][2], ri[2][2], \
            ri[2][2], ri[2][1], ri[2][0], \
            ri[2][0], ri[1][0], ri[0][0], \
            up[2][2], up[1][2], up[0][2], \
            bk[0][0], bk[1][0], bk[2][0], \
            dn[2][2], dn[1][2], dn[0][2], \
            fr[2][2], fr[1][2], fr[0][2] = \
                ri[2][0], ri[1][0], ri[0][0], \
                ri[0][0], ri[0][1], ri[0][2], \
                ri[0][2], ri[1][2], ri[2][2], \
                ri[2][2], ri[2][1], ri[2][0], \
                fr[2][2], fr[1][2], fr[0][2], \
                up[2][2], up[1][2], up[0][2], \
                bk[0][0], bk[1][0], bk[2][0], \
                dn[2][2], dn[1][2], dn[0][2]
        elif direction == '-':
            ri[0][0], ri[0][1], ri[0][2], \
            ri[0][2], ri[1][2], ri[2][2], \
            ri[2][2], ri[2][1], ri[2][0], \
            ri[2][0], ri[1][0], ri[0][0], \
            up[2][2], up[1][2], up[0][2], \
            bk[0][0], bk[1][0], bk[2][0], \
            dn[2][2], dn[1][2], dn[0][2], \
            fr[2][2], fr[1][2], fr[0][2] = \
                ri[0][2], ri[1][2], ri[2][2], \
                ri[2][2], ri[2][1], ri[2][0], \
                ri[2][0], ri[1][0], ri[0][0], \
                ri[0][0], ri[0][1], ri[0][2], \
                bk[0][0], bk[1][0], bk[2][0], \
                dn[2][2], dn[1][2], dn[0][2], \
                fr[2][2], fr[1][2], fr[0][2], \
                up[2][2], up[1][2], up[0][2]


n = int(input())
for i in range(n):
    # 큐브 초기화
    up = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    fr = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    lf = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    ri = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    dn = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
    bk = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    # 필요없는 숫자
    input()
    # 면과 회전방향 데이터
    data = list(input().split())
    # 데이터데로 회전 수행
    for dat in data:
        rot(dat[0], dat[1])
    # 윗면 프린트
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(up[i][j], end='')
            else:
                print(up[i][j])

