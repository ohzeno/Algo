# https://www.acmicpc.net/problem/16916
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
s, p가 주어졌을 때 p가 s의 부분 문자열이면 1, 아니면 0 출력
"""
s = input()
p = input()
if p in s:
    print(1)
else:
    print(0)


"""
이게 왜 브론즈2인가 의아했으나 다른 언어 풀이들을 보니 매우 힘들어보인다...
"""