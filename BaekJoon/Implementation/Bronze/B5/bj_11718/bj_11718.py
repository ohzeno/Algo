# https://www.acmicpc.net/problem/18108
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

while True:
    data = input()
    if data == '':
        break
    else:
        print(data)