# https://www.acmicpc.net/problem/3029
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def time_to_sec(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

def sec_to_time(s):
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    return f'{h:02}:{m:02}:{s:02}'

cur_t = time_to_sec(input())
thr_t = time_to_sec(input())
if cur_t > thr_t:  # 다음날이면 + 24시간
    thr_t += 24 * 3600
dif = thr_t - cur_t
# 정인이는 적어도 1초, 많아야 24시간을 기다린다.
# 즉, 0이 나오면 0초 기다리는게 아니라 24시간 기다리는 것이다.
if dif == 0:
    print('24:00:00')
else:
    print(sec_to_time(dif))
