# https://www.acmicpc.net/problem/10866
import sys


sys.stdin = open("input.txt")

deque = []
def solution(arr):
    command = arr[0]
    if command == "push_back":
        deque.append(int(arr[1]))
    elif command == "push_front":
        deque.insert(0, int(arr[1]))
    elif command == "pop_front":
        if deque:
            print(deque[0])
            del deque[0]
        else:
            print(-1)
    elif command == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(deque))
    elif command == "empty":
        if not deque:
            print(1)
        else:
            print(0)
    elif command == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)


T = int(input())

for tc in range(1, T+1):
    # input()으로 받으면 시간초과.
    solution(sys.stdin.readline().rstrip().split())
