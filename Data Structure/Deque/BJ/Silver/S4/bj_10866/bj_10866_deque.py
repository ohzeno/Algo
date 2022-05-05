# https://www.acmicpc.net/problem/10866
import sys
from collections import deque

sys.stdin = open("input.txt")

que = deque()
def solution(arr):
    # import 과정이 오래걸리는건지 데이터가 적어서 그런지 모르겠지만
    # 리스트를 사용한 풀이보다 시간도 오래걸리고 메모리도 더 썼다.
    command = arr[0]
    if command == "push_back":
        que.append(int(arr[1]))
    elif command == "push_front":
        que.appendleft(int(arr[1]))
    elif command == "pop_front":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command == "pop_back":
        if que:
            print(que.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(que))
    elif command == "empty":
        if not que:
            print(1)
        else:
            print(0)
    elif command == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif command == "back":
        if que:
            print(que[-1])
        else:
            print(-1)


T = int(input())

for tc in range(1, T+1):
    # input()으로 받으면 시간초과.
    solution(sys.stdin.readline().rstrip().split())