# https://www.acmicpc.net/problem/23337
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
drunk passenger problem 변형.
1번 승객은 무조건 다른 사람의 자리에 앉는다.
이후 승객은 자신의 자리가 비어있으면 자신의 자리에,
자리에 사람이 있으면 무작위로 다른 자리에 앉는다.
n번 승객이 자신의 자리에 앉지 못할 확률을 구하시오.
"""

def drunk_passenger(n):
    if n == 1:
        return 1
    if n == 2:
        return 0.5
    numer = 1
    for i in range(2, n):
        numer += drunk_passenger(n - i + 1)
    return numer / n

def custom_success(n):
    if n == 2:
        return 0
    numer = 0
    for i in range(2, n):
        numer += drunk_passenger(n - i + 1)
    return numer / (n - 1)

def custom_failure(n):
    return 1 - custom_success(n)

n = int(input())
print(custom_failure(n))


"""
현 시점 골드 5. 제출 220. 정답률 78.912 %
drunk passenger problem 변형.
drunk passenger problem 공부하다가 점화식 이해하고 나서 풀었다.
위의 함수들은 조건부확률로 점화식 구한 케이스다. 
custom은 1번 승객이 무조건 다른 사람 자리 앉는다는 조건 때문에
기존 식에서 확률이 좀 달라져서 추가했다.
"""