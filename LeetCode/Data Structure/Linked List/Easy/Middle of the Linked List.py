# https://leetcode.com/problems/middle-of-the-linked-list/?envType=study-plan&id=level-1
from typing import Optional, List
"""
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        leng = 0
        while dummy:
            leng += 1
            dummy = dummy.next
        for _ in range(leng // 2):  # n번 반복하면 index n번째 노드가 head가 된다.
            head = head.next
        return head

inputdatas = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
]

"""
LeetCode Easy.
처음엔 또 리스트에 담아서 미들값을 리턴했으나
다시 보니 미들 위치의 노드를 반환하는 것이었다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    dummy = ListNode()
    cur = dummy
    for i in t:
        cur.next = ListNode(i)
        cur = cur.next
    print(functions[0][1](dummy.next))
