# https://www.acmicpc.net/problem/1920
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
datas = set(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
for num in nums:
    if num in datas:  # 탐색은 set가 O(1)이라 빠르다.
        print(1)
    else:
        print(0)
