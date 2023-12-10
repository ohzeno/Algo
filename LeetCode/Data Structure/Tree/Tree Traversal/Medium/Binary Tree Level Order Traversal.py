# https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan&id=level-1
from typing import Optional, List
"""
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ans = []
        while q:
            level = []
            for _ in range(len(q)):  # len(q)를 사용해서 현재 레벨만 순회함.
                cur = q.popleft()
                if cur:  # None이 아닌 경우에만
                    level.append(cur.val)
                    q.append(cur.left)  # None도 추가함.
                    q.append(cur.right)
            if level:  # 레벨에 값이 있는 경우에만
                ans.append(level)
        return ans

inputdatas = [
    [3, 9, 20, None, None, 15, 7],
    [1],
    [],
]

""" 
LeetCode Medium.
input값 리스트로만 공개하고 클래스로 입력주는거 그만 좀 했으면 좋겠다...
리스트를 이진트리로 만드는 함수를 짜는데 시간을 좀 썼다.
예전에 비슷한 문제를 풀어본 기억이 있다.
q를 사용하며 안쪽에선 len(q)를 이용해 순회하며 
다음 단계를 q 뒤에 추가하더라도 현 단계만 순회하게 하는 방법을 사용했었다.
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

