# https://leetcode.com/problems/reverse-linked-list/?envType=study-plan&id=level-1
from typing import Optional, List
"""
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 리스트에 넣고 뒤집어서 새로운 링크드 리스트에 삽입
        # forward = []
        # while head:
        #     forward.append(head.val)
        #     head = head.next
        # dummy = ListNode()
        # cur = dummy
        # for i in reversed(forward):
        #     cur.next = ListNode(i)
        #     cur = cur.next
        # return dummy.next
        rev = None  # 뒤집힌 리스트
        remain_li = head  # 남은 리스트
        while remain_li:  # 남은 리스트가 없을 때까지
            tmp_body = remain_li.next  # 남은 리스트의 머리를 제외한 몸통
            tmp_head = remain_li  # 남은 리스트의 머리(아직 몸통 안잘림)
            tmp_head.next = rev  # 머리에 뒤집힌 리스트를 붙임
            rev = tmp_head  # 뒤집힌 리스트의 머리를 갱신
            remain_li = tmp_body  # 남은 리스트를 잘린 몸통으로 갱신
        return rev  # 뒤집힌 리스트 반환

inputdatas = [
    [1, 2, 3, 4, 5],
    [1, 2],
]

"""
LeetCode Easy.
첫 풀이는 그냥 리스트로 만들고, 새 링크드 리스트에 순서대로 삽입했다.
다른 풀이를 참고해서 두 번째 풀이를 만들었다.
두번째 풀이는 Easy라기엔 좀 어렵게 느껴진다.
가독성을 위해 다른 풀이보다 변수를 하나 더 썼다.
1-2-3-4-5가 있으면 2-3-4-5를 임시 몸통에 저장하고 1.next에 rev(None)를 붙이고 새로 rev(1)로 삼는다.
그 다음엔 2-3-4-5에서 3-4-5를 임시 몸통에 저장하고 2.next에 rev(1)를 붙이고 새로 rev(2-1)로 삼는다.
그 다음엔 3-4-5에서 4-5를 임시 몸통에 저장하고 3.next에 rev(2-1)를 붙이고 새로 rev(3-2-1)로 삼는다.
그 다음엔 4-5에서 5를 임시 몸통에 저장하고 4.next에 rev(3-2-1)를 붙이고 새로 rev(4-3-2-1)로 삼는다.
그 다음엔 5에서 None을 임시 몸통에 저장하고 5.next에 rev(4-3-2-1)를 붙이고 새로 rev(5-4-3-2-1)로 삼는다.
이런 식으로 리스트를 한 번만 순회하면서 뒤집을 수 있다.
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
