# https://www.acmicpc.net/problem/2417
import sys, math
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def solution(target):
    tmp = math.ceil(target ** (0.5))
    if tmp ** 2 >= target:
        return tmp
    elif tmp ** 2 < target:
        return tmp + 1

"""
64비트 부동소수점 자료형 제곱근 연산 사용하면 오류 생기나본데...
실버가 그런걸 신경써야 하는 난이도가 맞나...
그거때문에 if문 추가해줬다.
"""
n = int(input())
print(solution(n))
