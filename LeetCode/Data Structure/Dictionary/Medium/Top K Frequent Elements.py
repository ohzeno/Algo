# https://leetcode.com/problems/top-k-frequent-elements/
from typing import Optional, List

"""
constraints:
  • 1 <= nums.length <= 10^5
  • -10^4 <= nums[i] <= 10^4
  • k is in the range [1, the number of unique elements in the array].
  • It is guaranteed that the answer is unique.
"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_d = Counter(nums)
        return [x[0] for x in c_d.most_common(k)]



inputdatas = [
    {"data": [[1, 1, 1, 2, 2, 3], 2], "answer": [1, 2]},
    {"data": [[1], 1], "answer": [1]}
]

"""
LeetCode Medium.
제출 4.3M, 정답률 64.3%
카운팅소트 할까 하다가 
-10^4 <= nums[i] <= 10^4를 보고 Counter를 사용했다.
dict사용해도 되지만 most_common없이 풀려면 
keys를 정렬하는 과정까지 포함돼서 좀 귀찮다.
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
