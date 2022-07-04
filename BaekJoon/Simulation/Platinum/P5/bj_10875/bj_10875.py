# https://www.acmicpc.net/problem/10875
import sys

# 배열 인덱싱. 위가 마이너스. 우 상 좌 하
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
sys.stdin = open("input.txt")
# 가로세로 2L+1
L = int(input())
# 머리 몇 번 회전할 것인가
N = int(input())
# 몇 초 후, 어느 방향으로 방향을 틀 것인가
ti_dir_info = [input().split() for _ in range(N)]

route_stack = [
    [
        [-1, 2 * L + 1],
        [2 * L + 1, 2 * L + 1],
        0
    ],
    [
        [-1, 2 * L + 1],
        [-1, -1],
        0
    ],
    [
        [-1, -1],
        [-1, 2 * L + 1],
        1
    ],
    [
        [2 * L + 1, 2 * L + 1],
        [-1, 2 * L + 1],
        1
    ],
]
time_acc = 0
rot_count = cnt_dir = 0  # cnt_dir가 0, 2면 가로, 1, 3이면 세로
x = y = L
r_fin = 0  # 마지막 회전 체크 후 고정용 변수
while True:
    # 충돌기록 초기화
    crash = []
    # 마지막 회전이 아니고 회전명령이 있을 경우
    if r_fin == 0 and ti_dir_info:
        x_end = x + dx[cnt_dir] * int(ti_dir_info[rot_count][0])
        y_end = y + dy[cnt_dir] * int(ti_dir_info[rot_count][0])
    # 마지막 회전 했거나 회전명령이 없으면 맵 끝까지 쭉 진행
    else:
        x_end = x + dx[cnt_dir] * (2 * L + 1)
        y_end = y + dy[cnt_dir] * (2 * L + 1)
    cnt_route = [
        [min(x, x_end), max(x, x_end)],
        [min(y, y_end), max(y, y_end)],
        cnt_dir % 2
    ]
    # 현재 경로가 가로일 경우
    if cnt_route[2] == 0:
        # 과거 루트 하나씩 갖고와서
        for past in route_stack:
            # 과거경로도 가로면
            if past[2] == 0:
                # y좌표가 다르면 충돌 안함
                if cnt_route[1][0] != past[1][0]:
                    continue
                # 같은 선상이면 충돌체크
                else:
                    # 현재 오른쪽으로 진행중이면
                    if cnt_dir == 0:
                        # 현재루트 왼쪽끝(출발)보다 과거루트 왼쪽끝이 크고
                        # (같은경우는 이미 이전루트에서 충돌체크함)
                        # 현루트 오른끝(도착)이 과거루트 왼쪽끝보다 크거나 같으면 충돌
                        if (cnt_route[0][0] < past[0][0]) \
                                and (past[0][0] <= cnt_route[0][1]):
                            # 가장 가까운 충돌까지의 시간 기록
                            crash.append(past[0][0] - cnt_route[0][0])
                        else:  # 충돌 없으면 다음 과거경로 체크
                            continue
                    # 현재 왼쪽으로 진행중
                    else:
                        # 현 루트 왼쪽끝(도착)은 과거루트 오른끝보다 작거나 같고
                        # 현루트 오른끝(출발)은 과거루트 오른끝보다 크면 충돌
                        if (cnt_route[0][0] <= past[0][1]) \
                                and (past[0][1] < cnt_route[0][1]):
                            # 가장 가까운 충돌까지의 시간 기록
                            crash.append(cnt_route[0][1] - past[0][1])
                        else:  # 충돌 없으면 다음 과거경로 체크
                            continue
            # 과거 경로가 세로면
            else:
                # 현재루트가 과거 경로 y축 범위에 있지 않으면 충돌x
                if not (past[1][0] <= cnt_route[1][0] <= past[1][1]):
                    continue
                # y축 범주 같으면 충돌체크
                else:
                    # 현재 오른쪽으로 진행중이면
                    if cnt_dir == 0:
                        # 현루트 왼끝(출발)이 과거루트 x좌표보다 작고
                        # 현루트 오른끝(도착)이 과거루트 x좌표보다 크거나 같으면 충돌
                        if (cnt_route[0][0] < past[0][0]) \
                                and (past[0][0] <= cnt_route[0][1]):
                            # 충돌시간 기록
                            crash.append(past[0][0] - cnt_route[0][0])
                        else:  # 충돌 없으면 다음 과거경로 체크
                            continue
                    # 현재 왼쪽으로 진행중
                    else:
                        # 현루트 왼끝(도착)이 과거루트 x좌표보다 작거나 같고
                        # 현루트 오른끝(출발)이 과거루트 x좌표보다 크면 충돌
                        if (cnt_route[0][0] <= past[0][0]) \
                                and (past[0][0] < cnt_route[0][1]):
                            # 충돌시간 기록
                            crash.append(cnt_route[0][1] - past[0][0])
                        else:  # 충돌 없으면 다음 과거경로 체크
                            continue
    # 현재 경로가 세로일 경우 (매트릭스상에서 위가 y작음)
    else:
        # 과거 루트 하나씩 갖고와서
        for past in route_stack:
            # 과거경로도 세로면
            if past[2] == 1:
                # x좌표가 다르면 충돌 안함
                if cnt_route[0][0] != past[0][0]:
                    continue
                # 같은 선상이면 충돌체크
                else:
                    # 현재 위로 진행중이면
                    if cnt_dir == 1:
                        # 현재루트 아래끝(출발)보다 과거루트 아래끝이 작고
                        # (매트릭스상에서 아래가 y큼)
                        # 현루트 위끝(도착)이 과거루트 아래끝보다 작거나 같으면 충돌
                        if (cnt_route[1][1] > past[1][1]) \
                                and (past[1][1] >= cnt_route[1][0]):
                            # 충돌까지의 시간 기록(현루트 출발 - 과거루트 아래끝)
                            crash.append(cnt_route[1][1] - past[1][1])
                        else:  # 충돌 없으면 다음 과거경로 체크
                            continue
                    # 현재 아래로 진행중이면
                    else:
                        # 현루트 아래끝(도착)보다 과거루트 위끝이 작거나 같고
                        # (매트릭스상에서 아래가 y큼)
                        # 현루트 위끝(출발)이 과거루트 위끝보다 작으면 충돌
                        if (cnt_route[1][1] >= past[1][0]) \
                                and (past[1][0] > cnt_route[1][0]):
                            # 충돌까지의 시간 기록
                            crash.append(past[1][0] - cnt_route[1][0])
                        else:  # 충돌 없으면 다음 과거경로 체크
                            continue
            # 과거 경로가 가로일 경우
            else:
                # 현재루트가 과거 경로 x축 범위에 있지 않으면 충돌x
                if not (past[0][0] <= cnt_route[0][0] <= past[0][1]):
                    continue
                # x축 범주 같으면 충돌체크
                else:
                    # 현재 위로 움직이고 있으면
                    if cnt_dir == 1:
                        # 현재루트 아래끝(출발)보다 과거루트 y좌표가 작고
                        # 현루트 위끝(도착)이 과거루트 y좌표보다 작거나 같으면 충돌
                        if (cnt_route[1][1] > past[1][0]) \
                                and (past[1][0] >= cnt_route[1][0]):
                            # 충돌까지의 시간 기록
                            crash.append(cnt_route[1][1] - past[1][0])
                        else:  # 충돌 없으면 다음 과거경로 체크
                            continue
                    # 현재 아래로 진행중이면
                    else:
                        # 현루트 아래끝(도착)보다 과거루트 y좌표가 작거나 같고
                        # 현루트 위끝(출발)이 과거루트 y좌표보다 작으면 충돌
                        if (cnt_route[1][1] >= past[1][0]) \
                                and (past[1][0] > cnt_route[1][0]):
                            # 충돌까지의 시간 기록
                            crash.append(past[1][0] - cnt_route[1][0])
                        else:  # 충돌 없으면 다음 과거경로 체크
                            continue
    # 충돌기록이 있으면 누적시간 출력 후 브레이크
    if crash:
        time_acc += min(crash)
        print(time_acc)
        break
    # 충돌기록이 없으면 누적시간
    else:
        time_acc += int(ti_dir_info[rot_count][0])
        # 좌표 갱신
        x = x_end
        y = y_end
        # 아직 회전 다 안했으면 방향전환, 루트기록
        if rot_count < N - 1:
            if ti_dir_info[rot_count][1] == 'L':
                cnt_dir = (cnt_dir + 1) % 4
            else:
                cnt_dir = (cnt_dir - 1) % 4
            rot_count += 1
            # 현재 루트 기록
            route_stack.append(cnt_route)
        # 마지막 회전인 경우 회전수 증가하면 위쪽에서 인덱싱할때 오류생김.
        elif rot_count == N - 1:
            # 처음 도달한거면 마지막 방향전환.
            # 같은방향으로 쭉 갈거라 루트 기록 안함.
            # 지나온 길이랑 충돌 일어날 일은 없음
            if r_fin == 0:
                if ti_dir_info[rot_count][1] == 'L':
                    cnt_dir = (cnt_dir + 1) % 4
                else:
                    cnt_dir = (cnt_dir - 1) % 4
                r_fin = 1
