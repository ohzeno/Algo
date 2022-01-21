# https://www.acmicpc.net/problem/2720
import sys

sys.stdin = open("input.txt")

T = int(input())

change = [0.25, 0.1, 0.05, 0.01]
for tc in range(1, T+1):
    c = float(input())
    # 달러로 변환
    dollar = (c / 100)
    count = [0, 0, 0, 0]
    while dollar != 0:
        # 반올림 안하면 float 계산오류 생김
        if dollar >= 0.25:
            dollar = round(dollar - 0.25, 2)
            count[0] += 1
        elif dollar >= 0.1:
            dollar = round(dollar - 0.1, 2)
            count[1] += 1
        elif dollar >= 0.05:
            dollar = round(dollar - 0.05, 2)
            count[2] += 1
        else:
            dollar = round(dollar - 0.01, 2)
            count[3] += 1
    for i in range(4):
        if i != 3:
            print('{}'.format(count[i]), end=' ')
        else:
            print('{}'.format(count[i]))
