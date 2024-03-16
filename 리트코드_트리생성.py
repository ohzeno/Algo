from collections import deque
from typing import List, Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

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
        for side in ["left", "right"]:  # 자식 추가
            if i < l_datas and datas[i] is not None:
                child = Node(datas[i])
                setattr(cur_node, side, child)  # cur_node.side = child
                child.parent = cur_node
                queue.append(child)
                update_node_info(child, node_refs)
            i += 1
    p_node, q_node, ans_node = node_refs["p"]["node"], node_refs["q"]["node"], node_refs["ans"]["node"]
    return root, p_node, q_node, ans_node