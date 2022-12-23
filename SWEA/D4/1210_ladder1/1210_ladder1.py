# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh
import sys
sys.stdin = open('input.txt')

# 위 좌 우 방향전환용 리스트
di = [-1, 0, 0]
dj = [0, -1, 1]

for tc in range(10):
    # 방향 선택용 변수
    dirctn = 0
    T = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    # 마지막줄 2(도착 지점)의 y, x좌표
    cnt = [99, mat[99].index(2)]

    # 0행 도달 전까지 반복
    while cnt[0] != 0:
        # 위로 가는 중일 경우
        if dirctn == 0:
            # 좌우에 길이 있으면 회전
            if cnt[1] - 1 >= 0 and \
                    mat[cnt[0]][cnt[1] - 1] == 1:
                dirctn = 1
            elif cnt[1] + 1 <= 99 and \
                    mat[cnt[0]][cnt[1] + 1] == 1:
                dirctn = 2
        # 좌우 가던 경우
        elif dirctn == 1 or dirctn == 2:
            # 위쪽 길이 있으면 위로
            if mat[cnt[0]-1][cnt[1]] == 1:
                dirctn = 0
        # 다음 위치를 미리 할당.
        # 케이스에 오류 없으면 범위 초과할 일 없으니
        # if없이 그대로 진행
        ni, nj = cnt[0] + di[dirctn], cnt[1] + dj[dirctn]
        # 마지막에는 cnt가 0행 도달하니
        # 다음은 while 탈출
        # 현재 위치 갱신
        cnt[0], cnt[1] = ni, nj
    # x좌표 = 칼럼 인덱스이므로 cnt[1]출력
    print('#{} {}'.format(T, cnt[1]))
