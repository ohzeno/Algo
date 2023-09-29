# https://leetcode.com/problems/n-ary-tree-preorder-traversal/?envType=study-plan&id=level-1
from typing import Optional, List
"""
The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The height of the n-ary tree is less than or equal to 1000.
"""
from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # if root is None:
        #     return
        # ans = [root.val]
        # for child in root.children:
        #     ans += self.preorder(child)
        # return ans
        if root is None:
            return
        q, ans = deque([root]), []
        while q:
            root = q.popleft()
            ans.append(root.val)
            q.extendleft(reversed(root.children))  # extendleft(data)는 deque의 왼쪽에 data를 뒤집어서 넣는다.
        return ans

inputdatas = [
    [1, None, 3, 2, 4, None, 5, 6],
    [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
]

""" 
LeetCode Easy.
일단 리스트로 노드 구조 만든다고 고생했다...
dataclass를 사용해서 그냥 인풋 데이터를 새로 만드는게 더 편했을 것도 같다.
build_tree 함수는 크게 리팩토링 했다.
전위순회 자체보다 build_tree 만드는게 더 어려웠다.

내 첫 풀이는 싸피에서 배웠던 방법대로 재귀를 사용했다.
stack을 사용한 풀이를 봤으나 기존 전위순회 이미지와 잘 연결되지 않아서
q를 사용한 풀이도 남겨놓는다.
"""

def build_tree(datas: List[Optional[int]]):
    if not datas:
        return None
    root = Node(datas[0])
    q = deque([root])
    i = 2  # 0은 루트, 1은 층 변경용 None이므로 2부터 시작
    l_datas = len(datas)
    while i < l_datas:  # datas 전부 순회
        node = q.popleft()
        # 현재 노드의 자식을 찾아 큐에 추가. 이런 식으로 한 층의 노드가 모두 추가되면 다음 층이 뒤에 추가되게 된다.
        while i < l_datas and datas[i] is not None:
            child = Node(datas[i])
            node.children.append(child)
            q.append(child)
            i += 1
        i += 1  # 줄바꿈, 같은 레벨에서 옆 노드로 이동 시에 나오는 None을 건너뜀.
    return root

import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    tree = build_tree(t)
    print(my_func(tree))

