# https://school.programmers.co.kr/learn/courses/30/lessons/42892
"""
constraints:
  • nodeinfo는 이진트리를 구성하는 각 노드의 좌표가 1번 노드부터 순서대로 들어있는 2차원 배열이다.
    ◦ nodeinfo의 길이는 1 이상 10,000 이하이다.
    ◦ nodeinfo[i] 는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다.
    ◦ 모든 노드의 좌표 값은 0 이상 100,000 이하인 정수이다.
    ◦ 트리의 깊이가 1,000 이하인 경우만 입력으로 주어진다.
    ◦ 모든 노드의 좌표는 문제에 주어진 규칙을 따르며, 잘못된 노드 위치가 주어지는 경우는 없다.
"""
import sys

sys.setrecursionlimit(10 ** 6)  # 깊이 1000 이하


class Node:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None


def insert(root, node):
    if node.x < root.x:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)


def pre_order(node, result):
    result.append(node.idx)
    if node.left:
        pre_order(node.left, result)
    if node.right:
        pre_order(node.right, result)


def post_order(node, result):
    if node.left:
        post_order(node.left, result)
    if node.right:
        post_order(node.right, result)
    result.append(node.idx)


def solution(nodeinfo):
    nodes = []
    for i, (x, y) in enumerate(nodeinfo):
        nodes.append(Node(x, y, i + 1))
    # y 내림, x 오름차순 정렬
    nodes.sort(key=lambda n: (-n.y, n.x))
    root = nodes[0]
    for node in nodes[1:]:
        insert(root, node)
    pre_orders = []
    post_orders = []
    pre_order(root, pre_orders)
    post_order(root, post_orders)
    return pre_orders, post_orders


inputdatas = [
    {"data": [[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]],
     "answer": [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]}
]

"""
2019 KAKAO BLIND RECRUITMENT
Lv.3. 현 시점 완료한 사람 7,864명, 정답률 38%
옮겨적기부터 채점까지 1시간 39분 걸렸다.
무작위 노드를 받아서 부모/자식 기록하는 방식을 기억해둬야 할 듯 하다.
1시간 37분 걸려서 초기 제출안을 만들었다.
처음에는 노드를 순회하면서 부모, 좌자식, 우자식을 기록하는 방법을 찾다가 까다로워서
왼쪽, 오른쪽 서브트리를 따로 만들어 순회하는 것을 시도했고, 
다행히 메모리, 시간 초과 없이 부모/자식 배열을 기록했다.
(sorted, filter 남발했는데 통과하니까 오히려 어색하다...)
그 후 전위, 후위 순회를 시도했는데 테케 6, 7에서 런타임 에러가 발생했다.
알고보니 재귀 제한 해제 코드를 제출하지 않았었다...

2차. 예전에 어떻게 풀었는진 기억 안나고, (-y, x)로 정렬하고 이진탐색트리 만드는걸 1차 목표로 삼았다.
의외로 정렬 후 트리 만드는 것은 쉬워서 금방 끝났다.
클래스 사용하니 예전보다 코드가 깔끔하고 알아보기 쉽다.
"""

for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
