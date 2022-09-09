# https://www.acmicpc.net/problem/10807
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

# n = int(input())
# datas = list(map(int, input().split()))
# v = int(input())
# count = 0
# for data in datas:
#     if data == v:
#         count += 1
# print(count)

input()
print(input().split().count(input()))