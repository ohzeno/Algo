# https://leetcode.com/problems/subarray-product-less-than-k/
from typing import Optional, List

"""
constraints:
  • 1 <= nums.length <= 3 * 10^4
  • 1 <= nums[i] <= 1000
  • 0 <= k <= 10^6
"""
from operator import mul
from itertools import accumulate

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        pre = [1] + list(accumulate(nums, mul))
        if pre[-1] < k:
            return len(nums) * (len(nums) + 1) // 2
        cnt = 0
        for i in range(1, len(nums)+1):
            for j in range(i, len(nums)+1):
                if pre[j] // pre[i-1] >= k:
                    break
                cnt += 1
        return cnt


inputdatas = [
    {"data": [[10, 5, 2, 6], 100], "answer": 8},
    {"data": [[1, 2, 3], 0], "answer": 0}
]

"""
LeetCode Medium.
제출 919K, 정답률 52.6%
2중 for문으로 통과하긴 했는데 실행 시간이 하위 6%에 속한다.
안쪽 for문을 이진탐색으로 바꿔봤으나 오히려 시간초과가 발생했다.
이론적으로는 이분탐색이 빠르니 테스트 케이스가 불완전한 것으로 보인다.
"""
import inspect

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = my_func(sol, *data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
