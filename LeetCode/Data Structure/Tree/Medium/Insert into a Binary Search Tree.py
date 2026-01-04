# https://leetcode.com/problems/insert-into-a-binary-search-tree/
from typing import Optional, List

"""
constraints:
  • The number of nodes in the tree will be in the range [0, 10^4].
  • -10^8 <= Node.val <= 10^8
  • All the values Node.val are unique.
  • -10^8 <= val <= 10^8
  • It's guaranteed that val does not exist in the original BST.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left =  TreeNode(val)
        else:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        return root


inputdatas = [
    {"data": [[4, 2, 7, 1, 3], 5], "answer": [4, 2, 7, 1, 3, 5]},
    {"data": [[40, 20, 60, 10, 30, 50, 70], 25], "answer": [40, 20, 60, 10, 30, 50, 70, None, None, 25]},
    {"data": [[4, 2, 7, 1, 3, None, None, None, None, None, None], 5], "answer": [4, 2, 7, 1, 3, 5]}
]

"""
LeetCode Medium.
제출 1.1M, 정답률 73.3%
[], () 범위 표시를 너무 오랜만에 봐서 헷갈렸는데,
[]가 닫힌 구간, ()가 열린 구간이다.
"""
from collections import deque
import inspect
def build_binary_tree(datas: List[Optional[int]]):
    if not datas:
        return None
    root = TreeNode(datas[0])
    queue = deque([root])
    i = 1  # 인덱스 0은 이미 처리했으므로, 인덱스 1부터 시작
    l_datas = len(datas)
    while i < l_datas:
        node = queue.popleft()
        # 왼쪽 자식을 찾고 큐에 추가.
        if i < l_datas and datas[i] is not None:
            left_child = TreeNode(datas[i])
            node.left = left_child
            queue.append(left_child)
        i += 1
        # 오른쪽 자식을 찾고 큐에 추가.
        if i < l_datas and datas[i] is not None:
            right_child = TreeNode(datas[i])
            node.right = right_child
            queue.append(right_child)
        i += 1
    return root

def compare_trees(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
    """두 이진 트리의 구조와 값이 동일한지 비교"""
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if tree1.val != tree2.val:
        return False
    return compare_trees(tree1.left, tree2.left) and compare_trees(tree1.right, tree2.right)

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    root = build_binary_tree(data[0])
    ans = build_binary_tree(ans)
    data = (root, data[1])
    res = my_func(sol, *data)
    if compare_trees(res, ans):
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
