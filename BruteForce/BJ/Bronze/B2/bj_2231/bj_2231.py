# https://www.acmicpc.net/problem/2231
import sys

sys.stdin = open("input.txt")

n = int(input())
cnt = 0
while True:
    if cnt == n:
        print(0)
        break
    b = 0
    for i in range(len(str(cnt))):
        b += int(str(cnt)[i])
    if cnt + b == n:
        print(cnt)
        break
    else:
        cnt += 1



