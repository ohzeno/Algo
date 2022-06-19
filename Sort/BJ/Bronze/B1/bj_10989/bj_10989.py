# https://www.acmicpc.net/problem/10989
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
# sorted_list = []
# for _ in range(N):
#     k = int(input())
#     sorted_list.append(k)
# for num in sorted(sorted_list):
#     print(num)
"""
어렵다. sorted 자체에서 메모리초과가 발생한다.
리스트를 사용했는데 메모리 초과가 나서 처음엔 리스트의 메모리 초과할당 문제라 생각해 append를 없애봤다.
정렬 알고리즘을 무엇을 쓰느냐가 문제가 아니다.
정렬을 안하도록 처음부터 index에 할당하면 해결된다.
"""
sorted_list = [0] * 10001
for _ in range(N):
    k = int(input())
    sorted_list[k] += 1
for i in range(10001):
    if sorted_list[i]:
        for j in range(sorted_list[i]):
            print(i)
