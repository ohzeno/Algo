# https://www.acmicpc.net/problem/14645
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
for _ in range(n):  # 종착역 도착 후 출력하라고 했으므로 input데이터를 다 인식 후 출력
    input()
print('비와이')