# https://www.acmicpc.net/problem/2745
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


n, b = input().split()  # b진수 n
# 정석
alpha = {chr(i): i - 55 for i in range(65, 91)}
b = int(b)
n = n[::-1]  # 뒤집기
ans = 0
for i, s in enumerate(n):
    if s.isalpha():  # 알파벳이면 딕셔너리에서 숫자로 변환
        ans += alpha[s] * b ** i
    else:
        ans += int(s) * b ** i
print(ans)
# int(바꿀 숫자 문자열, 현 숫자 진법) > 10진법으로 바꿔줌
print(int(n, int(b)))
