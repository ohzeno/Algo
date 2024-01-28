# https://www.acmicpc.net/problem/20529
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
mbti 각 분류가 다른 정도로 심리적 거리를 정의한다.
a, b, c 세 사람 사이의 심리적 거리는
Dab + Dbc + Dac
n명의 mbti가 주어질 때, 세 학생 사이의 심리적 거리가 가장 작은 경우의 거리를 출력하라.
3 <= n <= 10_0000
"""
from itertools import combinations

def get_dist(a, b, c):
    key = tuple(sorted([a, b, c]))
    if key in dist_d:
        return dist_d[key]
    dist = sum([(i != j) + (j != k) + (i != k) for i, j, k in zip(a, b, c)])
    dist_d[key] = dist
    return dist

dist_d = {}

def get_three_dist(n, mbtis):
    if n > 32:  # 32를 넘으면 무조건 중복되는 세 사람이 존재.
        return 0
    return min([get_dist(a, b, c) for a, b, c in combinations(mbtis, 3)])


for _ in range(int(input())):
    n = int(input())
    mbtis = input().split()
    print(get_three_dist(n, mbtis))


"""
현 시점 실버 1. 제출 9742. 정답률 36.172 %
일단 왠지 모르겠지만 파이썬 상위 정답들은 죄다 틀렸다.
로직을 보고 논리 오류가 명백해서 어리둥절 했는데
질문게시판을 보니 7개월 전, 3개월 전 나와 같은 생각을 한 사람들이 데이터 추가를 요청했다.
하지만 왠지 모르게 무시당하는 중.
상위 답들은 n이 32를 넘지 않을 때 조합을 순회하며 최소값을 찾는데, 
dist가 2가 되면 break하도록 되어 있다. 가능한 최소 거리라고 가정하고 break하는 것이다.
하지만 n이 32를 넘지 않더라도 세 사람이 중복될 수 있고, 두 사람이 중복될 수도 있다.
이는 문제에 제시된 테스트케이스에도 나온 케이스다.
그런 경우 dist가 0~1이므로 2일 때 break하면 최소값이 아닐 수 있다.
도대체 왜 데이터 추가를 하지 않는 것인지 이해가 되지 않는다.
"""
