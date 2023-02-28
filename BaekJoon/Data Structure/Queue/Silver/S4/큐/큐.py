# https://www.acmicpc.net/problem/10845
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
정수를 저장하는 큐를 구현 후 명령을 처리하라.
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

def push(x):
    q.append(x)

def pop():
    if q:
        return q.pop(0)
    return -1

def size():
    return len(q)

def empty():
    if q:
        return 0
    return 1

def front():
    if q:
        return q[0]
    return -1

def back():
    if q:
        return q[-1]
    return -1

n = int(input())
q = []
for _ in range(n):
    order = input()
    if order.startswith('push'):
        order, num = order.split()
        push(num)
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'front':
        print(front())
    elif order == 'back':
        print(back())


"""
현 시점 실버4. 제출 96245, 정답률 49.120 %
pypy3에서조차 자꾸 시간초과가 발생해서 고생했는데, 알고보니 input()이 느려서 
sys.stdin.readline().rstrip()을 사용하면 python3에서도 바로 통과된다.
백준의 시간 제한 기준이란...
"""