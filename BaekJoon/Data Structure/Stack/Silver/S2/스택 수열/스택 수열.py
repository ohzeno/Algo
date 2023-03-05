# https://www.acmicpc.net/problem/1874
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
1부터 n까지 수를 스택에 넣었다 뽑아 하나의 수열을 만든다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop을 수행해야 하는지를 계산하는 프로그램을 작성하시오.
"""

n = int(input())
target = [int(input()) for _ in range(n)]
stack = []
orders = []
for i in range(1, n+1):  # push는 오름차순
    stack.append(i)
    orders.append('+')
    while stack and stack[-1] == target[0]:  # 스택 최상위가 타겟이면 pop
        stack.pop()
        target.pop(0)
        orders.append('-')
if stack:  # 스택이 남아있으면 실패
    print('NO')
else:  # 스택 비어있으면 성공.
    for s in orders:  # 순서대로 출력
        print(s)


"""
현 시점 실버2. 제출 116392, 정답률 36.925%
"""