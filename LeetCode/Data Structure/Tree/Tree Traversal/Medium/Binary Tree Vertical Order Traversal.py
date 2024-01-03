# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
from typing import Optional, List

"""
이진트리 루트가 주어졌을 때 vertical order traversal을 리턴하라.
from top to bottom, column by column.
같은 행과 열에 있으면 왼쪽부터 오른쪽 순서로 정렬한다.

constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # rcd = {}
        # def dfs(node, row, col):
        #     rcd.setdefault(col, []).append((row, node.val))
        #     if node.left:
        #         dfs(node.left, row+1, col-1)
        #     if node.right:
        #         dfs(node.right, row+1, col+1)
        # dfs(root, 0, 0)
        # res = []
        # for col in sorted(rcd.keys()):
        #     res.append([val for row, val in sorted(rcd[col], key=lambda x: x[0])])
        # return res
        col_d = {}
        q = deque([(root, 0)])
        while q:
            node, col = q.popleft()
            col_d.setdefault(col, []).append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        return [col_d[i] for i in sorted(col_d.keys())]


inputdatas = [
    # [[3,9,20,None,None,15,7],[[9],[3,15],[20],[7]]],
    # [[3,9,8,4,0,1,7], [[4],[9],[3,0,1],[8],[7]]],
    # [[3,9,8,4,0,1,7,None,None,None,2,5], [[4],[9,5],[3,0,1],[8,2],[7]]],
    [
        [1, 2, 3, 4, 5, 6, None, None, 7, 8, None, None, 9, None, 10, None, 11, 10],
        [[4], [2, 7, 8], [1, 5, 6, 10, 11, 10], [3, 9]],
    ]
]

"""
LeetCode Hard.
제출 670K, 정답률 53.3%
어떻게 할까 하다가 dfs로 먼저 풀었다.
통과 후 bfs풀이를 보니 이 문제에 한해 bfs가 더 직관적이다(시간은 dfs가 더 빨랐다).
dfs의 경우 왼쪽으로 타고 들어가서 기록하니 열 자체의 순서는 문제가 되지 않는다.
하지만 아래쪽부터 기록하다보니 같은 열 내에서 행의 순서가 뒤집어질 수 있다.
그래서 행까지 기록해서 정렬을 해줘야 한다.

bfs로 하면 행을 차례대로 내려가면서 열 순서로 큐에 넣을 수 있어서 추가 정렬이 필요하지 않다.
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
# for t in inputdatas:
#     print(my_func(*t))
for data, answer in inputdatas:
    tree = build_binary_tree(data)
    res = my_func(tree)
    if res == answer:
        print("pass")
    else:
        print("fail\n", f"expected:{answer}\n", f"got:{res}\n")
