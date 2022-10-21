# https://www.acmicpc.net/problem/21300
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

# 맥주 맥아 와인 탄산 청량 물
datas = list(map(int, input().split()))
print(sum(datas) * 5)
