# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())
# 통과하려고 만든 같은 로직...
for tc in range(T):
    n = int(input())
    num_li = list(map(int, input().split()))
    mode = 0  # 큰 수 자리인지 작은 수 자리인지 판별하는 용도
    count = 0  # 몇 개 출력했는지 체크하는 용도
    print('#{}'.format(tc + 1), end='')
    while count < 10:  # 10번 출력하도록
        if mode == 0:  # 큰 수 출력차례
            max_num = max(num_li)  # 최대값 찾기
            max_i = num_li.index(max_num)  # 최대값 인덱스
            num_li[0], num_li[max_i] = \
                num_li[max_i], num_li[0]  # 최대값과 첫 자리 원소 교체
            mode = 1  # 다음 차례는 작은 수 나오도록 모드변경
        elif mode == 1:
            min_num = min(num_li)
            min_i = num_li.index(min_num)
            num_li[0], num_li[min_i] = \
                num_li[min_i], num_li[0]
            mode = 0
        print(' {}'.format(num_li[0]), end='')
        count += 1  # 원소 출력 후 카운트 +1
        del num_li[0]  # 첫자리 원소 삭제
    if tc < T - 1:  # 마지막 케이스 아닌 경우 줄바꿈
        print()
