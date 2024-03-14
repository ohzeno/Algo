# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
from typing import Optional, List
from collections import deque

"""
이진트리의 노드 p, q가 주어지면 lowest common ancestor를 찾아라.
노드 자신도 후손이 될 수 있다.
constraints:
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q exist in the tree.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        ancestors = set()
        while p:
            ancestors.add(p)
            p = p.parent
        while q not in ancestors:
            q = q.parent
        return q


inputdatas = [
    {
        "data": [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1],
        "answer": 3,
    },
    {
        "data": [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4],
        "answer": 5,
    }
]

"""
LeetCode Medium.
제출 270.6K, 정답률 79.2%
최소 공통 조상 문제.
한 쪽의 조상을 다 기록하고
다른 쪽을 하나씩 거슬러 올라가며 기록된 조상에 있는지 확인한다. 

문제 내용과 별개로 tree 생성 로직을 업데이트 했다.
"""


def update_node_info(node: Node, node_refs: dict[str, dict[str, any]]):
    for key, value in node_refs.items():
        if not value["node"] and node.val == value["target"]:
            value["node"] = node


def build_binary_tree(datas: List[Optional[int]], p, q, ans):
    if not datas:
        return None
    root = Node(datas[0])
    node_refs = {
        "p": {"node": None, "target": p},
        "q": {"node": None, "target": q},
        "ans": {"node": None, "target": ans},
    }
    update_node_info(root, node_refs)
    queue = deque([root])
    i = 1  # 인덱스 0은 이미 처리했으므로, 인덱스 1부터 시작
    l_datas = len(datas)
    while i < l_datas:
        cur_node = queue.popleft()
        for side in ["left", "right"]:
            if i < l_datas and datas[i] is not None:
                child = Node(datas[i])
                setattr(cur_node, side, child)  # cur_node.side = child
                child.parent = cur_node
                queue.append(child)
                update_node_info(child, node_refs)
            i += 1
    p_node, q_node, ans_node = (
        node_refs["p"]["node"],
        node_refs["q"]["node"],
        node_refs["ans"]["node"],
    )
    return root, p_node, q_node, ans_node


import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    root, p, q, ans = build_binary_tree(*data, ans)
    res = my_func(p, q)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
