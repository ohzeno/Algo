# https://www.acmicpc.net/problem/2562
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

a = []
max_num = 0
max_idx = 0
for i in range(9):
    b = int(input())
    a.append(b)
    if b > max_num:
        max_num = b
        max_idx = i + 1
print(max_num)
print(max_idx)


"""
현 시점 Bronze III. 제출 346771. 정답률 45.438 %
예전에 풀었는데 레포에는 없어서 다시 풀었다.
"""
