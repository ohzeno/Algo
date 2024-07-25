# https://leetcode.com/problems/contiguous-array/
from typing import Optional, List

"""
constraints:
  1 <= nums.length <= 10^5
  nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        acc = 0
        cnt_d = {0: -1}  # 누적합 key값: 최근에 발견된 누적합이 key인 인덱스
        for i, num in enumerate(nums):
            if num == 0:
                acc -= 1
            else:
                acc += 1
            # 누적합이 같으면 그 사이는 합이 0임(0과 1의 개수가 같다는 뜻)
            if acc in cnt_d:
                max_len = max(max_len, i - cnt_d[acc])
            else:
                cnt_d[acc] = i
        return max_len


inputdatas = [
    {"data": [[0, 1]], "answer": 2},
    {"data": [[0, 1, 0]], "answer": 2},
    {"data": [[0, 1, 0, 1]], "answer": 4},
]

"""
LeetCode Medium.
제출 950.5K, 정답률 49.0%%
처음에 2중for문을 사용하려 했는데
누적합으로 쉽게 풀 수 있었다.
누적합 다루는게 오랜만이라 그런지 좀 오래걸리긴 했다.
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
