# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    num_li = list(map(int, input().split()))
    for i in range(N - M + 1):
        container = 0   # 구간합 카운팅용
        summation = 0
        # 구간 합 구현
        while container < M:
            summation += num_li[i + container]
            container += 1
        # summation = sum(num_li[i:i + M])
        # 최소 최대값 초기화
        if i == 0:
            min_sum = max_sum = summation
        # 최소 최대값 찾기
        elif i > 0:
            if summation > max_sum:
                max_sum = summation
            elif summation < min_sum:
                min_sum = summation
    print('#{} {}'.format(tc + 1, max_sum - min_sum))
