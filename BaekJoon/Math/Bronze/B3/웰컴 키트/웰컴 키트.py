# https://www.acmicpc.net/problem/30802
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
티셔츠는 S, M, L, XL, XXL, XXXL의 6가지 사이즈가 있음
티셔츠는 같은 사이즈의 T장 묶음으로만 주문할 수 있습니다.
펜은 한 종류로, P자루씩 묶음으로 주문하거나 한 자루씩 주문할 수 있습니다.
총 N명의 참가자 중 
S, M, L, XL, XXL, XXXL 사이즈의 티셔츠를 신청한 사람은 각각 
S, M, L, XL, XXL, XXXL명. 
티셔츠는 남아도 되지만 부족해서는 안 되고 신청한 사이즈대로 나눠주어야 합니다. 
펜은 남거나 부족해서는 안 되고 정확히 참가자 수만큼 준비되어야 합니다.

티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지, 
그리고 펜을 P자루씩 최대 몇 묶음 주문할 수 있고, 
그 때 펜을 한 자루씩 몇 개 주문하는지 구하세요.
"""

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())
shirt = 0
for size in sizes:
    q, r = divmod(size, t)
    shirt += q + (1 if r else 0)
print(shirt)
print(*divmod(n, p))


"""
현 시점 브론즈 3. 제출 3565. 정답률 61.150 %
간단한 몫, 나머지 문제
"""