# https://www.acmicpc.net/problem/11286
import sys
import heapq

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


tree = []
T = int(input())
for _ in range(1, T+1):
    x = int(input())
    if x == 0:  # 0인 경우 절댓값이 가장 작은 값을 출력하고 제거.
        # 절댓값이 가장 작은 값이 여럿이면 가장 작은 수를 출력하고 그 값을 배열에서 제거
        # heapq는 튜플/리스트의 첫 원소로 정렬하지만 첫 원소가 같으면 두번째 원소로 정렬함.
        # 따라서 따로 처리가 필요하지 않다.
        if tree:
            res = heapq.heappop(tree)
            print(res[1])
        else:  # 배열이 비어있는 데 출력하라고 하면 0 출력
            print(0)
    else:  # 0이 아닌 경우 배열에 넣기
        heapq.heappush(tree, (abs(x), x))
