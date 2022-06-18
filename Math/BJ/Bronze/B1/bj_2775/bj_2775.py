# https://www.acmicpc.net/problem/2775
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
# pypy로 제출해야 시간초과x
def solution(a, b):
    if a == 1:
        # 1층의 경우 d = 1인 등차수열의 합.
        return (b * (b + 1)) / 2
    else:
        ans = 0
        # a-1층의 1~b호 사람 수 합
        for i in range(1, b + 1):
            ans += solution(a - 1, i)
        return ans

for _ in range(T):
    k = int(input())
    n = int(input())
    print(int(solution(k, n)))




