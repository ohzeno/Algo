# https://www.acmicpc.net/problem/25314
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
print(f'{"long " * (n//4)}int')  # f스트링 내부에 따옴표를 사용하여 스트링을 입력할 때는 외부 따옴표와 다른 종류를 사용해야 함.
