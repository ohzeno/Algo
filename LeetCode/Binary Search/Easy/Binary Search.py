# https://leetcode.com/problems/binary-search/
from typing import Optional, List
"""
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ll, rr = 0, len(nums) - 1
        while ll <= rr:
            mid = (ll + rr) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:  # 타겟보다 작으면
                ll = mid + 1
            else:  # 타겟보다 크면
                rr = mid - 1
        return -1

inputdatas = [
    [[-1,0,3,5,9,12], 9],
    [[-1,0,3,5,9,12], 2],
]
"""
LeetCode Easy
이진탐색은 항상 <, <=, 증감 조건 등등으로 고생하는데
이번은 타겟을 정확히 찾는 문제라 편했다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t[0], t[1]))

