# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    length = int(input())
    # 매트릭스 만들기
    mat = [[0] * length for _ in range(length)]
    # 오른쪽 아래 왼쪽 위 방향전환용 리스트
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 방향 선택용 변수
    direction = 0
    # 초기위치
    i, j = 0, -1
    # 현재 넣을 숫자
    cnt = 1
    # 숫자가 매트릭스 셀 수보다 작거나 같은동안 실행
    while cnt <= length * length:
        # 다음 위치를 미리 할당
        ni, nj = i + di[direction], j + dj[direction]
        # 다음 위치가 mat 안벗어나고 다음 셀에 아직 할당 X일 때
        if ni < length and \
                nj < length and \
                mat[ni][nj] == 0:
            # 셀에 숫자 할당
            mat[ni][nj] = cnt
            # 마지막 숫자 넣은 후에는 cnt가 l*l 초과하니
            # 다음은 while 탈출
            cnt += 1
            # 현재 위치 갱신
            i, j = ni, nj
        # 방향전환. 인덱스 4가되면 0으로 전환되도록 % 4
        else:
            direction = (direction + 1) % 4
    print('#{}'.format(tc + 1))
    # 매트릭스 행의 모든 요소 출력 후 다음 행 출력
    for i in mat:
        print(*i)
