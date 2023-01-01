# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    # P: 페이지 수,
    # Pa: a가 찾을 페이지, Pb: b가 찾을 페이지
    P, Pa, Pb = map(int, input().split())
    la = lb = 1
    ra = rb = P
    count_a = count_b = 0
    cen_a = int((la + ra) / 2)
    cen_b = int((lb + rb) / 2)
    # 센터가 목표랑 다른 동안 반복
    while cen_a != Pa:
        count_a += 1
        cen_a = int((la + ra) / 2)
        # 목표페이지보다 센터가 크면 센터를 오른쪽끝으로
        if Pa < cen_a:
            ra = cen_a
        # 목표페이지보다 센터가 작으면 센터를 왼쪽끝으로
        elif cen_a < Pa:
            la = cen_a
    while cen_b != Pb:
        count_b += 1
        cen_b = int((lb + rb) / 2)
        if Pb < cen_b:
            rb = cen_b
        elif cen_b < Pb:
            lb = cen_b
    # 승부결과 따라 res 할당 후 출력
    if count_a > count_b:
        min_sum = 'B'
    elif count_b > count_a:
        min_sum = 'A'
    else:
        min_sum = 0
    print('#{} {}'.format(tc + 1, min_sum))
