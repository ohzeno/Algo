# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional, List

"""
constraints:
  • k == lists.length
  • 0 <= k <= 10^4
  • 0 <= lists[i].length <= 500
  • -10^4 <= lists[i][j] <= 10^4
  • lists[i] is sorted in ascending order.
  • The sum of lists[i].length will not exceed 10^4.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        vals = []
        for node in lists:
            cur = node
            while cur:
                vals.append(cur.val)
                cur = cur.next
        if not vals:
            return None
        vals.sort(reverse=True)
        prev = None
        for i in vals:
            node = ListNode(i)
            node.next = prev
            prev = node
        return node



inputdatas = [
    {"data": [[[1, 4, 5], [1, 3, 4], [2, 6]]], "answer": [1, 1, 2, 3, 4, 4, 5, 6]},
    {"data": [[]], "answer": []},
    {"data": [[[]]], "answer": []}
]

"""
LeetCode Hard.
제출 4.3M, 정답률 56.2%
채점 코드는 만들기 귀찮아서 패스했다.
Hard인 것 치고 그냥 sort 사용하면 최상위 실행시간으로 통과한다.
원래 의도는 병합정렬인듯.
"""
# import inspect
#
# functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
# my_func = functions[0]
# sol = Solution()
# for inputdata in inputdatas:
#     data, ans = inputdata["data"], inputdata["answer"]
#     processed_data = []
#     for d in data[0]:
#         if d:
#             node = ListNode(d[0])
#             head = node
#             for i in range(1, len(d)):
#                 node.next = ListNode(d[i])
#                 node = node.next
#             processed_data.append(head)
#         else:
#             processed_data.append(None)
#     res = my_func(sol, processed_data)
#     if res == ans:
#         print("pass")
#     else:
#         summary = "fail"
#         for label, content in [("expected:", ans), ("got:", res)]:
#             summary += f"\n  {label}\n"
#             summary += f"    {content}"
#             summary = summary.rstrip()
#         print(summary)
