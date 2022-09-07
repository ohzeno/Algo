# https://www.acmicpc.net/problem/5597
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

check = [0] * 31  # 1~30 체크리스트
for i in range(1, 29):
    check[int(input())] = 1  # 과제 제출한 사람 체크
count = 0
for i in range(1, 31):  # 작은 번호 순 과제 제출 안한 2명 프린트
    if check[i] == 0:
        print(i)
        count += 1
    if count == 2:
        break