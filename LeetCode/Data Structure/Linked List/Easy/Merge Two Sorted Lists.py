# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional, List
"""
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ListNode()를 가리키는 포인터가 저장되는 것이라,
        # tmp에 재할당 해도 before_ans는 변하지 않는다.
        # a = b = ListNode()로 작성하면 시간을 약간 더 사용한다.
        before_ans = ListNode()
        tmp = before_ans
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next
        tmp.next = list1 if list1 else list2
        return before_ans.next

inputdatas = [
    [[1,2,4], [1,3,4]],
    [[], []],
    [[], [0]],
]
"""
LeetCode Easy
linked list 클래스를 입력으로 받고, 
리턴도 linked list 클래스로 하는 방식을 LeetCode에서 처음 경험했었다.
클래스를 이해는 하고 있지만 아직은 사용하는데 익숙하지 않다.
더미를 사용하는 방법은 내가 떠올렸었지만, 다른 사람들이 훨씬 잘 사용하고 있다.
[]로 표시된 input이 ListNode()인지 None인지 파악하는데 시간이 걸렸고, 
return에서 []로 표시된 부분이 무엇인지 파악하는데도 시간이 걸렸다.
이후 8분 정도 사용하여 초안을 통과시켰고, 다른 풀이를 참고하여 더 깔끔하게 개선했다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    if len(t[0]) == 0:
        l1 = None
    else:
        l1 = ListNode(t[0][0])
    if len(t[1]) == 0:
        l2 = None
    else:
        l2 = ListNode(t[1][0])
    tmp1, tmp2 = l1, l2
    for i in range(1, len(t[0])):
        tmp1.next = ListNode(t[0][i])
        tmp1 = tmp1.next
    for i in range(1, len(t[1])):
        tmp2.next = ListNode(t[1][i])
        tmp2 = tmp2.next
    print(functions[0][1](l1, l2))
