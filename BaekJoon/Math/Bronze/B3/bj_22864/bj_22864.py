# https://www.acmicpc.net/problem/22864
import sys

sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


fatigue, work, rest, burn_out = map(int, input().split())
i = 1
acc_work = 0
acc_fatigue = 0
while i <= 24:  # 24시간
    if acc_fatigue + fatigue <= burn_out:  # 한시간 더 일해도 번아웃 안오면
        acc_fatigue += fatigue  # 일하고
        acc_work += work  # 누적 일 갱신
    else:  # 번아웃오면 휴식
        acc_fatigue -= rest
        if acc_fatigue < 0:
            acc_fatigue = 0  # 피로도 음수면 0으로 수정
    i += 1  # 시간 갱신
print(acc_work)
