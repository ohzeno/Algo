# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional, List
"""
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = head
        vals = []
        while tmp:
            vals.append(tmp.val)
            tmp = tmp.next
        return vals == vals[::-1]

inputdatas = [
    [1,2,2,1],
    [1,2],
]
"""
LeetCode Easy
그냥 값을 리스트에 넣고 비교.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    head = ListNode(t[0])
    tmp = head
    for i in range(1, len(t)):
        tmp.next = ListNode(t[i])
        tmp = tmp.next
    print(functions[0][1](head))
