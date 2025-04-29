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
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        before_head = ListNode()
        cur = before_head
        # 링크드리스트는 비교 불가하므로 heqp에 넣으려면 비교연산자를 정의해야 함
        # 비교연산자 기억하긴 힘드니 idx 넣음
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heappush(heap, (node.val, i))
        while heap:
            val, node_idx = heappop(heap)
            node = lists[node_idx]
            cur.next = node
            cur = node
            if node.next:
                heappush(heap, (node.next.val, node_idx))
                # idx로 모든 노드 구분하려면 업데이트 해줘야함.
                lists[node_idx] = node.next
        return before_head.next



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

병합정렬 구현은 실수가 많을 것 같아서 heapq를 써봤다.
이론상으론 이게 시간복잡도가 낮을텐데 이전 풀이는 3ms, 힙큐는 11ms가 나왔다.
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
