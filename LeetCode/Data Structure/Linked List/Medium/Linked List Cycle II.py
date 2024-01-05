# https://leetcode.com/problems/linked-list-cycle-ii/?envType=study-plan&id=level-1
from typing import Optional, List
"""
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return head  # 사이클이 없으면 tail.next = None이라 head 반환하면 됨.

inputdatas = [
    [[3, 2, 0, -4], 1],
    [[1, 2], 0],
    [[1], -1],
]

"""
LeetCode Medium
아무래도 영어라 파악이 느린 것 같다.
LeetCode 특성상 예시의 output과 실제 요구하는 output이 다른 경우가 많다.
이번엔 output은 내가 리턴해야하는 값이 아니라 자체 채점시스템의 출력값이었다...
문제 설명을 읽고 pos를 반환하라는 줄 알고 처음엔 idx를 반환했고
리스트노드를 반환해야한다는 오류가 뜨길래 node.val을 반환했다.
문제를 다시 읽어보니 헤드를 반환하래서 헤드를 반환했고, 사이클 없을 때 -1을 반환했다.
계속 틀려서 다시 읽다보니 제일 위에 사이클 없을 때는 null을 반환하라고 적혀있다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for datas, target in inputdatas:
    dummy = ListNode()
    cur = dummy
    cnt = -1
    cycle = None
    for i in datas:
        cur.next = ListNode(i)
        cur = cur.next
        cnt += 1
        if cnt == target:
            cycle = cur
    cur.next = cycle
    print(functions[0][1](dummy.next))
