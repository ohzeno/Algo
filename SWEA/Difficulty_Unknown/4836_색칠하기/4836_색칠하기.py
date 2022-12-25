# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n = int(input())
    # 색은 1, 2 둘 중 하나이니 색 별로 컨테이너 생성
    # 같은 색 영역 겹치는 항목 제거 위해 set
    color_container = [set(), set()]
    # 영역별로 반복 / 완전탐색
    for i in range(n):
        # 각 좌표와 컬러 할당
        i1, j1, i2, j2, color = map(int, input().split())
        # 각 영역 모든 좌표를 색에 해당하는 컨테이너에 넣기
        for x in range(i1, i2 + 1):
            for y in range(j1, j2 + 1):
                color_container[color - 1].add((x, y))
    # &로 교집합만 추출
    overlap = color_container[0] & color_container[1]
    # 들어있는 튜플의 갯수가 겹치는 영역 넓이
    min_sum = len(overlap)
    print('#{} {}'.format(tc + 1, min_sum))
