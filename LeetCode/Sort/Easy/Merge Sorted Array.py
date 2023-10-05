# https://leetcode.com/problems/merge-sorted-array/
from typing import Optional, List

"""
constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
감소하지 않는 순서로 정렬된 nums1, nums2
m, n은 nums1, nums2에 있는 원소 수
nums1 내부에 감소하지 않는 순서로 두 배열을 병합하라.
nums1의 초기배열의 오른쪽 n개의 원소는 0으로 초기화되어 있다.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        i = j = 0
        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                nums1[i + j] = nums1_copy[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1
        if i < m:
            nums1[i + j :] = nums1_copy[i:]
        elif j < n:
            nums1[i + j :] = nums2[j:]


inputdatas = [
    [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
    [[1], 1, [], 0],
    [[0], 0, [1], 1],
]

"""
LeetCode Easy.
병합정렬의 일반적인 진행과정을 그대로 구현했다.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    num1, m, num2, n = t
    my_func(num1, m, num2, n)
    print(num1)
