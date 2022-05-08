# https://www.acmicpc.net/problem/11279

import sys
from collections import deque

sys.stdin = open("input.txt")


def change(n):
    if n == 0:
        return
    parent = (n - 1) // 2
    # 부모 노드와 비교, 교체
    if tree[parent] < tree[n]:
        tree[parent], tree[n] = tree[n], tree[parent]
        change(parent)


def update(n):
    child_a, child_b = 2 * n + 1, 2 * n + 2
    if child_a <= cur_node:
        if child_b <= cur_node:
            # 자식 둘일 경우 둘 중 큰 노드랑 비교.
            # 큰 자식노드와 부모노드 값 비교 후 교체
            if tree[child_a] > tree[child_b]:
                if tree[child_a] > tree[n]:
                    tree[n], tree[child_a] = tree[child_a], tree[n]
                    update(child_a)
            else:
                if tree[child_b] > tree[n]:
                    tree[n], tree[child_b] = tree[child_b], tree[n]
                    update(child_b)
        else:  # 자식 a만 존재하면 a랑 비교, 교체
            if tree[child_a] > tree[n]:
                tree[n], tree[child_a] = tree[child_a], tree[n]
                update(child_a)
    else:  # a가 없으면 b노드는 존재x
        return


tree = deque()
cur_node = -1

T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    order = int(sys.stdin.readline().rstrip())
    if order:  # 트리 추가명령
        tree.append(order)
        cur_node += 1
        if cur_node:  # 2개 이상일 경우만 정렬
            change(cur_node)
    else:  # 최대값 출력 후 제거 명령
        if tree:
            print(tree[0])  # 최대값 출력
            if cur_node:  # 가장 나중 노드랑 루트노드 교체
                tree[cur_node], tree[0] = tree[0], tree[cur_node]
            tree.pop()  # 가장 나중(이전 루트노드값) 노드 제거
            cur_node -= 1
            update(0)
        else:  # 배열 비어있을 경우 0 출력
            print(0)
