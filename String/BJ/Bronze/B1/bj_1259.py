# https://www.acmicpc.net/problem/1259
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

while True:
    data = input()
    if data == '0':
        break
    if data == data[::-1]:
        print('yes')
    else:
        print('no')