# https://leetcode.com/problems/most-frequent-subtree-sum/
from typing import Optional, List

"""
constraints:
  • The number of nodes in the tree is in the range [1, 10^4].
  • -10^5 <= Node.val <= 10^5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def post_order(node):
            if not node:
                return 0
            left_sum = post_order(node.left)
            right_sum = post_order(node.right)
            total = left_sum + right_sum + node.val
            sum_count[total] = sum_count.get(total, 0) + 1
            return total
        sum_count = {}
        post_order(root)
        if not sum_count:
            return []
        max_freq = max(sum_count.values())
        return [s for s, freq in sum_count.items() if freq == max_freq]


inputdatas = [
    {"data": [[5, 2, -3]], "answer": [2, -3, 4]},
    {"data": [[5, 2, -5]], "answer": [2]}
]

"""
LeetCode Medium.
제출 247.9K, 정답률 68.7%
서브트리 합이라 전위순회나 중위순회는 안된다.
다른 방식으로는 dfs가 가능한데, 후위순회와 다를게 없다.
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

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    root = build_binary_tree(*data)
    res = my_func(sol, root)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
