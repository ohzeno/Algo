# https://www.acmicpc.net/problem/1259
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

num_of_cards, max_value = map(int, input().split())
data = list(map(int, input().split()))
res = []
for n1 in range(num_of_cards - 2):
    for n2 in range(n1 + 1, num_of_cards - 1):
        for n3 in range(n2 + 1, num_of_cards):
            res.append(data[n1] + data[n2] + data[n3])
# 모든 경우의 수 중에서 최대값 넘지 않는 녀석들만 정렬.
res = sorted(list(filter(lambda x: x <= max_value, res)))
print(res[-1])  # 정렬된 리스트 중 마지막이 가장 큼.
