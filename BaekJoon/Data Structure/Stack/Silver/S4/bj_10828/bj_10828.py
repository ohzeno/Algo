# https://www.acmicpc.net/problem/10828
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def push(data):
    stack.append(int(data))

def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

n = int(input())
stack = []
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
    elif order[0] == 'top':
        top()

