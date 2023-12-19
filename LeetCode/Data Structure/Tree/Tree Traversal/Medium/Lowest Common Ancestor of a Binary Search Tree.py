# https://leetcode.com/problems/validate-binary-search-tree/?envType=study-plan&id=level-1
from typing import Optional, List
from collections import deque
"""
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the BST.
find the lowest common ancestor (LCA) node of two given nodes in the BST.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if p.val < root.val and q.val < root.val:  # 루트가 p, q보다 크면 왼쪽 서브트리에 존재.
                root = root.left
            elif root.val < p.val and root.val < q.val:  # 루트가 p, q보다 작으면 오른쪽 서브트리에 존재.
                root = root.right
            else:  # 루트가 둘 사이에 있는 경우. 또는 루트가 둘 중 하나와 같은 경우. 이진탐색트리 특성에 따라 최소공통조상이 됨.
                return root

inputdatas = [
    [[6,2,8,0,4,7,9,None,None,3,5], 2, 8],
    [[6,2,8,0,4,7,9,None,None,3,5], 2, 4],
    [[2, 1], 2, 1],
]

"""
LeetCode Medium.
분명 예전에 공통조상 문제 풀었던 것 같은데 못찾겠다.
더러운 방법밖에 생각나지 않아서 풀이를 참고했다.
굉장히 깔끔한 논리를 보고 놀랐다. 나는 그냥 이진트리만 생각했는데 주어진 트리가 이진탐색트리였다.
풀이는 이진탐색트리의 특성을 이용하였다.
"""
def build_binary_tree(datas: List[Optional[int]], p, q):
    if not datas:
        return None
    root = TreeNode(datas[0])
    if root.val == p:
        p = root
    if root.val == q:
        q = root
    queue = deque([root])
    i = 1  # 인덱스 0은 이미 처리했으므로, 인덱스 1부터 시작
    l_datas = len(datas)
    while i < l_datas:
        node = queue.popleft()
        # 왼쪽 자식을 찾고 큐에 추가.
        if i < l_datas and datas[i] is not None:
            left_child = TreeNode(datas[i])
            if left_child.val == p:
                p = left_child
            if left_child.val == q:
                q = left_child
            node.left = left_child
            queue.append(left_child)
        i += 1
        # 오른쪽 자식을 찾고 큐에 추가.
        if i < l_datas and datas[i] is not None:
            right_child = TreeNode(datas[i])
            if right_child.val == p:
                p = right_child
            if right_child.val == q:
                q = right_child
            node.right = right_child
            queue.append(right_child)
        i += 1
    return root, p, q

import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    tree, p, q = build_binary_tree(t[0], t[1], t[2])
    print(my_func(tree, p , q))
