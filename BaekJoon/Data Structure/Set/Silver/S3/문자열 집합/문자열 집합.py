# https://www.acmicpc.net/problem/14425
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
count = 0
set_s = set(input() for _ in range(N))
for _ in range(M):
    # set는 해시테이블로 구현되어 있어 in 연산이 리스트보다 압도적으로 빠르다.
    if input() in set_s:
        count += 1
print(count)
