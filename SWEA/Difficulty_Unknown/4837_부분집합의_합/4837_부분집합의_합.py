# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    # n은 부분집합 원소 수, k는 원소의 합
    n, k = map(int, input().split())
    count = 0
    for i in range(1 << 12):
        sum_el = []  # 부분집합 원소 넣을 리스트
        for j in range(12):
            # 해당 원소가 들어가는 부분집합인지 체크
            if i & (1 << j):
                # 부분집합에 속하는 원소면 추가
                sum_el.append(j+1)
        # 부분집합이 원소 수, 원소 합 만족할 경우 카운트 +1
        if len(sum_el) == n and sum(sum_el) == k:
            count += 1
    print('#{} {}'.format(tc + 1, count))

