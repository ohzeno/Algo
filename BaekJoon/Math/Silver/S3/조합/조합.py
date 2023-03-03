# https://www.acmicpc.net/problem/2407
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
nCm을 출력하라
"""

from math import factorial as fac
n, r = map(int, input().split())
print(fac(n) // (fac(r) * fac(n - r)))

"""
현 시점 실버3. 제출 28724, 정답률 41.716%
라이브러리 없이 구현하려면 약분 좀 하고 분모, 분자 팩토리얼 계산하면 될 듯 하다. 
n, m이 크지 않고 시간 제한이 2초라 그정도면 충분하리라 예상한다.
"""