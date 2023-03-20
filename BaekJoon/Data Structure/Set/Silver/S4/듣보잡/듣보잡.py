# https://www.acmicpc.net/problem/1764
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
"""

n, m = map(int, input().split())
listen = set()  # 듣도 못한 사람
see = set()  # 보도 못한 사람
for _ in range(n):
    listen.add(input())
for _ in range(m):
    see.add(input())
both = listen & see  # 듣보잡
both = sorted(both)  # set를 바로 넣어도 리스트로 반환
print(len(both))
for name in both:
    print(name)

"""
현 시점 실버4. 제출 73671, 정답률 40.382%
sorted에 순서 없는 set를 넣어도 정렬된 리스트를 반환하는 건 처음 알았다.
"""