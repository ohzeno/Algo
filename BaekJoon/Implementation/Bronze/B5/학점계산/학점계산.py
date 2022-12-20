# https://www.acmicpc.net/problem/2754
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

data = input()
if data[0] == 'A':
    tmp = 4.0
elif data[0] == 'B':
    tmp = 3.0
elif data[0] == 'C':
    tmp = 2.0
elif data[0] == 'D':
    tmp = 1.0
else:
    tmp = 0.0
if tmp != 0:  # 0점이 아니면 +-0있음
    if data[1] == '+':
        tmp += 0.3
    elif data[1] == '-':
        tmp -= 0.3
print(tmp)