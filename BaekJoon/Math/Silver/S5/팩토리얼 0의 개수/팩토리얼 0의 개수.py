# https://www.acmicpc.net/problem/1676
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n!에서 뒤에서부터 0이 아닌 숫자가 나올 때까지 0의 개수를 세면 된다.
"""

from math import factorial as fac
n = int(input())
n_fac = str(fac(n))[::-1]
count = 0
for s in n_fac:
    if s != '0':
        break
    count += 1
print(count)

"""
현 시점 실버5. 제출 57567, 정답률 47.926%
예제로 추정해보면 '뒤'라는건 문자열 오른쪽 끝을 의미한다.
"""