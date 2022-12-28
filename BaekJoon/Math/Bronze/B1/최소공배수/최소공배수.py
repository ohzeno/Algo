# https://www.acmicpc.net/problem/1934
import sys, math
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

# a, b 최소공배수?
# Greatest Common Divisor, Least Common Multiple
# print(math.gcd(a, b))
# print(math.lcm(a, b))
"""
유클리드 호제법. NeedReview에도 한 문제 넣어놨는데 또 까먹었다.
이게 진짜 코테에 나오고 math를 사용 못하면 그냥 수학 덕후를 찾는게 아닌지...
"""
def gcd(a, b):
    # 이건 증명 길던데 그냥 외우자...
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):  # 최소 공배수
    # a*b에서 교집합곱(최대공약수) 나누면 합집합 곱이 됨.
    return a * b // gcd(a, b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
