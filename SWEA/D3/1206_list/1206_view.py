# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh
import sys
sys.stdin = open('input.txt')

for tc in range(10):    # 테스트케이스만큼 반복
    count = 0           # 케이스마다 카운트 초기화
    wide = int(input())     # 데이터 가로길이
    # 높이정보 리스트로
    h_list = list(map(int, input().split()))
    # 양끝 2칸은 비어있으므로 2, wide-2
    for j in range(2, wide - 2):
        # 인덱스 j 양옆 2칸 높이만 모음
        four_list = [
            h_list[j - 2], h_list[j - 1],
            h_list[j + 1], h_list[j + 2]
        ]
        # 최고높이 구하기 위해 첫 높이로 초기화
        max_h = four_list[0]
        # 양옆 2칸 건물중 최고높이 구하기
        for k in range(len(four_list)):
            if four_list[k] > max_h:
                max_h = four_list[k]
        # 현재 건물이 양 옆 최고높이보다 높으면 그 차이가
        # 조망권 확보된 집이니 count에 더해줌
        if h_list[j] - max_h > 0:
            count += h_list[j] - max_h
        # 테스트케이스별 카운트 출력
    print('#{} {}'.format(tc + 1, count))