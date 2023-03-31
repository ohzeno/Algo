# https://www.acmicpc.net/problem/1074
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
2^N x 2^N 크기의 2차원 배열을 Z모양으로 탐색한다.
N > 1인 경우, 배열을 크기가 2^(N-1) × 2^(N-1)로 4등분 한 후에 재귀적으로 순서대로 방문한다.
N이 주어졌을 때, r행 c열을 몇 번째로 방문했는지 출력하는 프로그램을 작성하시오.
"""

def find_order(n, r, c):
    if n == 1:
        return 2 * r + c
    else:  # n이 2 이상
        if r < 2 ** (n - 1):  # 1, 4사분면
            if c < 2 ** (n - 1):  # 4사분면
                return find_order(n - 1, r, c)
            else:  # 1사분면
                return 2 ** (2 * n - 2) \
                    + find_order(n - 1, r, c - 2 ** (n - 1))
        else:  # 2, 3사분면
            if c < 2 ** (n - 1):  # 3사분면
                return 2 ** (2 * n - 2) * 2 \
                    + find_order(n - 1, r - 2 ** (n - 1), c)
            else:  # 2사분면
                return 2 ** (2 * n - 2) * 3 \
                    + find_order(n - 1, r - 2 ** (n - 1), c - 2 ** (n - 1))

n, r, c = map(int, input().split())
print(find_order(n, r, c))

"""
현 시점 실버1. 제출 61988, 정답률 39.688%
전형적인 재귀 분할정복.
"""
