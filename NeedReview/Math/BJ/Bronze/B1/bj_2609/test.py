# https://www.acmicpc.net/problem/2609
import sys, math
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
# Greatest Common Divisor, Least Common Multiple
# print(math.gcd(a, b))
# print(math.lcm(a, b))
"""
유클리드 호제법 이라고 한다. 잘 모르던 부분.
"""
def gcd(a, b):
    # 이건 증명 길던데 그냥 외우자...
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):  # 최소 공배수
    # a*b에서 교집합곱(최대공약수) 나누면 합집합 곱이 됨.
    return a * b // gcd(a, b)

print(gcd(n, m))
print(lcm(n, m))
