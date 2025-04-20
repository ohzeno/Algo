# https://www.acmicpc.net/problem/3020
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
n: 동굴 길이
h: 동굴 높이
"""
n, h = map(int, input().split())
u_h2crash = [0] * (h + 1)  # 높이별 충돌 수
d_h2crash = [0] * (h + 1)  # 높이별 충돌 수
for _ in range(n // 2):
    di = int(input())
    ui = int(input())
    d_h2crash[di] += 1
    u_h2crash[ui] += 1
# 낮은 높이에서는 위쪽 충돌도 포함되니 역순 누적합.
for i in range(h - 1, 0, -1):
    d_h2crash[i] += d_h2crash[i + 1]
    u_h2crash[i] += u_h2crash[i + 1]

min_c = n
cnt = 0
for i in range(1, h + 1):
    crash = d_h2crash[i] + u_h2crash[h - i + 1]
    if crash < min_c:
        min_c = crash
        cnt = 1
    elif crash == min_c:
        cnt += 1
print(min_c, cnt)

"""
현 시점 Gold V. 제출 21872. 정답률 46.152 %
2차원 imos 보고 연습해보려고 1차원 imos 문제로 들어온건데
각 배열이 dp처럼 추상적이라서 2차원보다 더 어려웠다.
"""
