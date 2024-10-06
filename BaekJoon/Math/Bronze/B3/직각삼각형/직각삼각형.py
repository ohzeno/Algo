# https://www.acmicpc.net/problem/4153
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    nums.sort()
    a, b, c = nums
    isRight = a ** 2 + b ** 2 == c ** 2
    print("right" if isRight else "wrong")

"""
현 시점 Bronze III. 제출 102086. 정답률 50.521 %
예전에 풀었는데 레포에는 없어서 다시 풀었다.
"""
