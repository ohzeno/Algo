# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    # move: 한 번 충전으로 최대 이동할 수 있는 정류장 수
    # end_loc: 종점 (정류장 수)
    # n_o_chrg: 충전소 갯수
    move, end_loc, n_o_chrg = map(int, input().split())
    # 충전소 위치정보
    charge_loc = list(map(int, input().split()))
    my_loc = 0
    count = 0
    # 안넣어도 통과되지만 문제 조건대로면 넣어야 하는 부분
    # move가 1일 경우
    if move == 1:
        # move가 1이면 거리만큼 충전소가 필요.
        # 매번 충전
        if n_o_chrg >= end_loc:
            count = end_loc
            print('#{} {}'.format(tc + 1, count))
            continue
        # move가 1인데 충전소 수가 종점까지 거리보다 작으면
        # 도달 못하니 0
        else:
            count = 0
            print('#{} {}'.format(tc + 1, count))
            continue
    while move != 1:
        # 현재 위치가 종점 이상이면 중단
        if my_loc >= end_loc:
            break
        # 이동할 수 있는 최대 범위부터 줄여가며 충전소 확인
        for i in range(my_loc + move, my_loc, -1):
            # 이동을 더한 위치가 종점 이상이면 충전 필요X 종료
            if i >= end_loc:
                my_loc = end_loc
                break
            # 이동을 더한 위치에 충전소가 있으면 이동하고 카운트+
            if i in charge_loc:
                my_loc = i
                count += 1
                break
        # 이동 범위 내에 충전소가 없으면 0, 종료
        else:
            count = 0
            break
    print('#{} {}'.format(tc+1, count))

