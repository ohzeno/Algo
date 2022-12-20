# https://www.acmicpc.net/problem/4358
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
트라이로 풀어본 후 그냥 편하게 딕셔너리로 풀어봤다.
"""
trees = {}
count = 0
while True:
    data = input()
    if data == '':
        break
    else:
        if data in trees:
            trees[data] += 1
        else:
            trees[data] = 1
        count += 1  # 총 단어 수
for tree in sorted(trees.keys()):  # 사전 순으로
    # round(0.5)는 0으로 나옴. round연산의 문제점이기에 .4f로 반올림.
    print(f'{tree} {trees[tree]/count * 100:.4f}')
