# https://www.acmicpc.net/problem/17626
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n이 주어지면 합이 n이 되는 제곱수의 최소 갯수를 출력하라
"""
from math import sqrt

def fourSquares(n):
    n1 = sqrt(n)
    if n1.is_integer():  # n 자체가 제곱수면 1개가 최소
        return 1
    for i in range(1, int(n1) + 1):  # 제곱 해줘야하니 sqrt(n)까지만
        if sqrt(n - i ** 2).is_integer():  # i 제곱수를 뺀 나머지가 제곱수면 2개가 최소
            return 2
    for i in range(1, int(n1) + 1):
        n2 = sqrt(n - i ** 2)
        for j in range(1, int(n2) + 1):
            n3 = sqrt(n - i ** 2 - j ** 2)
            if n3.is_integer():  # i, j 제곱수를 뺀 나머지가 제곱수면 3개가 최소
                return 3
    return 4  # 나머지는 전부 4개

print(fourSquares(int(input())))


"""
현 시점 실버3. 제출 18684, 정답률 44.387%
처음에 이걸 브루트포스를 사용하면서 어떻게 0.5초를 맞출 수 있나 당황스러웠다.
제곱수가 최대 4개라는 점을 이용할 수 있었다.
"""