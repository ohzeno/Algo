# https://www.acmicpc.net/problem/23337
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
drunk passenger problem 변형.
1번 승객은 무조건 다른 사람의 자리에 앉는다.
이후 승객은 자신의 자리가 비어있으면 자신의 자리에,
자리에 사람이 있으면 무작위로 다른 자리에 앉는다.
n번 승객이 자신의 자리에 앉지 못할 확률을 구하시오.
"""

# def drunk_passenger(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 0.5
#     denom = 1 + (n - 2) * drunk_passenger(n - 1)
#     return denom/n
#
# def custom(n):
#     denom = 1 + (n - 2) * drunk_passenger(n - 1)
#     return denom/(n - 1)

n = int(input())
print((1+(n-2)*0.5)/(n-1))


"""
현 시점 골드 5. 제출 220. 정답률 78.912 %
drunk passenger problem 변형.
drunk passenger problem 공부하다가 점화식 이해하고 나서 풀었다.
위의 함수들은 조건부확률로 점화식 구한 케이스다. 
custom은 1번 승객이 무조건 다른 사람 자리 앉는다는 조건 때문에
기존 식에서 확률이 좀 달라져서 추가했다.
그런데 drunk_passenger는 n이 2 이상일 때 전부 0.5다.
이 문제의 n은 2 이상이니 P(1)이 되는 n=2가 문제인데,
denom에서 P(n-1)의 계수가 (n-2)라 n=2일 때 P는 사라진다.
그래서 그냥 입력값 식에서 P를 0.5로 두고 바로 출력해도 된다.
"""