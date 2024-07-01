# https://www.acmicpc.net/problem/31403
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
JavaScript에서 
+, -은 수에 대해서는 일반적인 의미의 덧셈 뺄셈의 의미를 가지고 있습니다. 
하지만 문자열에 대해서 
+는 두 문자열을 이어붙이라는 의미이고, 
-는 양쪽 문자열을 수로 해석한 이후에 빼라는 의미입니다.

A, B, C를 각각 수와 문자열로 생각했을 때 
A+B-C를 출력하세요.
"""


A = input()
B = input()
C = input()
print(int(A) + int(B) - int(C))
print(int(A + B) - int(C))


"""
현 시점 브론즈 4. 제출 4629. 정답률 66.349 %
solved 클래스에 새로 생겼길래 풀어봤다.
"""
