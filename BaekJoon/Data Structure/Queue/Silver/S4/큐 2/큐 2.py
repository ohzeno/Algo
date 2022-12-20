# https://www.acmicpc.net/problem/18258
import sys
from collections import deque
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def push(data):
    stack.append(int(data))

def pop():
    if stack:
        print(stack.popleft())
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

def front():
    if stack:
        print(stack[0])
    else:
        print(-1)

def back():
    if stack:
        print(stack[-1])
    else:
        print(-1)

n = int(input())
stack = deque()
for _ in range(n):
    order = list(input().split())
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'size':
        size()
    elif order[0] == 'empty':
        empty()
    elif order[0] == 'front':
        front()
    elif order[0] == 'back':
        back()

