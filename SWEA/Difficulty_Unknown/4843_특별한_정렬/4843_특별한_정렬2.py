# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())
# 통과하려고 만든 같은 로직...
for tc in range(T):
    n = int(input())
    num_li = sorted(list(map(int, input().split())))
    mode = 0  # 큰 수 자리인지 작은 수 자리인지 판별하는 용도
    count = 0  # 몇 개 출력했는지 체크하는 용도
    l, r = 0, -1
    ans = []
    print('#{}'.format(tc + 1), end='')
    while count < 10:  # 10번 출력하도록
        now = 0
        if mode == 0:  # 큰 수 출력차례
            now = num_li[r]
            r -= 1
            mode = 1
        elif mode == 1:
            now = num_li[l]
            l += 1
            mode = 0
        print(' {}'.format(now), end='')
        count += 1  # 원소 출력 후 카운트 +1
    if tc < T - 1:  # 마지막 케이스 아닌 경우 줄바꿈
        print()
