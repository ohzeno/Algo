# https://www.acmicpc.net/problem/10162

import sys
sys.stdin = open("input1.txt")

T = int(input())
btn_a_300 = 0
btn_b_60 = 0
btn_c_10 = 0

# 10초로 나누어 떨어지지 않으면 세 버튼으로 시간 맞출 수 없음
if T % 10 != 0:
    print('-1')
else:
    # 10초로 나누어 떨어지면 무조건 0으로 끝남
    while T != 0:
        if T >= 300:
            T -= 300
            btn_a_300 += 1
        elif T >= 60:
            T -= 60
            btn_b_60 += 1
        elif T >= 10:
            T -= 10
            btn_c_10 += 1
    print(btn_a_300, btn_b_60, btn_c_10)