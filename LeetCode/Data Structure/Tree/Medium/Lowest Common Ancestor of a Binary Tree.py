# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
from typing import Optional, List

"""
constraints:
  • The number of nodes in the tree is in the range [2, 10^5].
  • -10^9 <= Node.val <= 10^9
  • All Node.val are unique.
  • p != q
  • p and q will exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 둘 다 찾았으면 root가 최소 조상.
            return root
        # 한쪽만 있으면 그쪽이 최소 조상.
        # root에서 시작하기 때문에 p만 포함된 서브트리가 최종적으로 반환될 일은 없음.
        return left if left else right


inputdatas = [
    {"data": [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1], "answer": 3},
    {"data": [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4], "answer": 5},
    {"data": [[1, 2], 1, 2], "answer": 1}
]

"""
LeetCode Medium.
제출 3.2M, 정답률 66.5%
최소조상 문제를 오랜만에 풀어서 방법을 잊었다.
거기에 p, q, root, 반환값까지 TreeNode라 채점 코드 작성도 힘들었다.
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

def find_node(val, root):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(val, root.left)
    right = find_node(val, root.right)
    return left if left else right

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    root, p, q = build_binary_tree(data[0]), data[1], data[2]
    p, q = find_node(p, root), find_node(q, root)
    ans = find_node(ans, root)
    res = my_func(sol, root, p, q)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
