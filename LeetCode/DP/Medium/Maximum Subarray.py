# https://leetcode.com/problems/maximum-subarray/
from typing import Optional, List
"""
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ll = rr = 0
        # maxsum = nums[0]
        # while rr < len(nums):
        #     if ll == rr:
        #         tmpsum = nums[ll]
        #     else:
        #         tmpsum += nums[rr]
        #     if maxsum < tmpsum:
        #         maxsum = tmpsum
        #     if tmpsum < 0:
        #         ll = rr + 1
        #     rr += 1
        # return maxsum
        tmpsum = maxsum = -float('inf')
        for num in nums:
            """
            num까지의 합이 num보다 작다는 말은 이전까지의 합이 음수라는 말이다.
            그러면 이전까지의 합은 버리고 num부터 새로 subarr를 찾는다.
            """
            tmpsum = max(num, tmpsum + num)
            maxsum = max(maxsum, tmpsum)
        return maxsum


inputdatas = [
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8],
]

"""
LeetCode Medium
처음에 5분정도 써서 투포인터로 통과했다.
다른 풀이들을 보니 간단한 로직이 있어서 채택했다.
그런데 이 로직이 알고보니 dp였고, 내 풀이도 같은 로직이었다.
dp테이블을 만들어서 풀면 마지막에 max(dp)를 하면 되고, dp테이블을 만들지 않아도 풀린다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
