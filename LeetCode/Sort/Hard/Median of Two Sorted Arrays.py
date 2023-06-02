# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import Optional, List
"""
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        leng = len(nums)
        if leng % 2 == 0:
            return (nums[leng//2-1] + nums[leng//2]) / 2
        else:
            return nums[leng//2]

inputdatas = [
    [[1,3], [2]],
    [[1,2], [3,4]],
]

"""
LeetCode Hard.
3분도 안걸렸다. 처음엔 median을 잘못 알아들어서 평균값을 구하라는 줄 알았다.
[1,5], [8]을 생각해보니 평균으로 계산하면 안됐다. 중앙값을 구하라는 것을 이해하고
단순하게 두 배열을 합친 후 정렬하고, 중앙값을 구했다.
O(log(m+n))이 되어야 한다고 적혀있고 sorted는 O(nlogn)까지 느려질 수 있기에 통과되더라도 하위권일 줄 알았는데
Runtime 79 ms Beats 98.75%가 나와서 좀 황당했다.
추천이 많은 풀이들은 훨씬 난잡했고, Runtime과 Memory 상위권을 보니 내 풀이와 로직이 동일했다.
손으로 풀게 되면 정렬을 직접 해야할 테니 귀찮을지도 모르겠다.
아마 파이썬이라 쉽게 풀린 것 같다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t[0], t[1]))
