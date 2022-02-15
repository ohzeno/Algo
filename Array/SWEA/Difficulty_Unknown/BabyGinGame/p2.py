# https://swexpertacademy.com/main/learn/course/lectureHtmlViewer.do
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = input()
    min_sum = []
    c = [0] * 10  # 각 숫자 갯수 카운팅.
    tri = run = 0
    for i in range(6):
        c[int(numbers[i])] += 1
    i = 0
    while i < 10:
        if c[i] >= 3:   # 트리플릿 있으면 카운팅하고 제거
            tri += 1
            c[i] -= 3
            continue
        if i < 8:  # i+2까지 보기때문에 7이면 9까지 다 체크.
            # run 있으면 카운팅 후 제거
            if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
                run += 1
                c[i] -= 1
                c[i+1] -= 1
                c[i+2] -= 1
                continue
        i += 1
    if run + tri == 2:
        print('Baby Gin')
    else:
        print('Lose')

