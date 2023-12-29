# https://leetcode.com/problems/validate-binary-search-tree/?envType=study-plan&id=level-1
from typing import Optional, List
from collections import deque
"""
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root: Optional[TreeNode]) -> bool:
            if not root:  # 리프노드의 자식이면 True
                return True
            if not inorder(root.left):  # 왼쪽 먼저 탐색
                return False
            if prev[0] >= root.val:  # 이전값보다 클 때만 True
                return False
            prev[0] = root.val  # 탐색한 현재 노드의 값을 기록
            return inorder(root.right)  # 오른쪽 탐색
        prev = [-float('inf')]  # 이전값 초기는 -무한대.
        return inorder(root)

inputdatas = [
    [2, 1, 3],
    [5, 1, 4, None, None, 3, 6],
    [5, 4, 6, None, None, 3, 7]
]

"""
LeetCode Medium.
처음엔 각 레벨에서 자식들이랑만 비교했는데, 
이진탐색트리이므로 루트의 왼쪽은 항상 루트보다 작고 오른쪽은 항상 루트보다 커야 한다.
dfs 말고 다른 방법이 있나 찾아보다가 inorder를 이용하는 방법을 찾았다.
inorder를 사용하면 왼쪽부터 하나하나 탐색하게 되므로 순서대로 탐색하면서 이전값과 비교하면 된다.
"""
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

import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    tree = build_binary_tree(t)
    print(my_func(tree))
