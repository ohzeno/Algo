# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))
    min_num = max_num = num_list[0]  # 최소 최대값 초기화
    for i in range(len(num_list)):  # 리스트 순회
        if num_list[i] > max_num:   # 최대값 갱신
            max_num = num_list[i]
        if num_list[i] < min_num:   # 최소값 갱신
            min_num = num_list[i]
    print('#{} {}'.format(tc + 1, max_num - min_num))