# https://www.acmicpc.net/problem/9012
from collections import deque
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    data = input()
    stack = deque()
    fail = 0
    for i in range(len(data)):
        cnt = data[i]
        if cnt == '(':
            stack.append(cnt)
        else:
            # cnt가 )이고 스택에 원소가 있고 마지막 원소가 (면 매칭. 제거.
            if stack and stack[-1] == '(':
                stack.pop()
            else:  # 매칭 아니면 그냥 추가
                stack.append(cnt)
    if stack:  # 전부 매칭되지 않고 남아있는게 있으면 NO
        print("NO")
    else:
        print("YES")





