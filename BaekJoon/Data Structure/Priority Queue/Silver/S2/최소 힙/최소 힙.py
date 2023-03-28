# https://www.acmicpc.net/problem/1927
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
- 배열에 자연수 x를 넣는다.
- 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작한다.
"""
from heapq import heappush as hpush, heappop as hpop
arr = []
for _ in range(int(input())):
    x = int(input())
    if x:
        hpush(arr, x)
    else:
        print(hpop(arr) if arr else 0)

"""
현 시점 실버2. 제출 60749, 정답률 48.953%
힙큐 문제. 파이썬의 경우 직접 구현할 필요 없어서 쉽게 풀 수 있다.
"""