# https://www.acmicpc.net/problem/10798
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
왼쪽 글자부터 세로읽기. 글자가 없으면 다음 줄 글자를 이어붙임.
"""

datas = [input() for _ in range(5)]
s = ''
for c in range(15):
    for r in range(5):
        if c < len(datas[r]):
            s += datas[r][c]
print(s)
