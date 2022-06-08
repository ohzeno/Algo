# https://www.acmicpc.net/problem/17202
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

A = input()
B = input()
s = ''
for i in range(len(A)):
    s += A[i] + B[i]
while True:
    new_s = ''
    if len(s) == 2:
        print(s)
        break
    for i in range(len(s) - 1):
        # 01, 12, 23 자리 더한 숫자의 일의자리 숫자만으로 새 문자열 구성.
        new_s += str(int(s[i]) + int(s[i + 1]))[-1]
    s = new_s
