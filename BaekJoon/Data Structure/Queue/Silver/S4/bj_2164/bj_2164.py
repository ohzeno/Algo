# https://www.acmicpc.net/problem/2164
from collections import deque
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
data = deque(i for i in range(1, n+1))
while True:
    if len(data) == 1:
        print(data[0])
        break
    data.popleft()
    data.append(data.popleft())

