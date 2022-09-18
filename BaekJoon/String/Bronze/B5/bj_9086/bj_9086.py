# https://www.acmicpc.net/problem/9086
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    data = input()
    print(f'{data[0]}{data[-1]}')