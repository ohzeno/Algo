# https://leetcode.com/problems/move-zeroes/
from typing import Optional, List

"""
constraints:
  • 1 <= nums.length <= 10^4
  • -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        to_sort_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[to_sort_idx], nums[i] = nums[i], nums[to_sort_idx]
                to_sort_idx += 1


inputdatas = [
    {"data": [[0, 1, 0, 3, 12]], "answer": [1, 3, 12, 0, 0]},
    {"data": [[0]], "answer": [0]},
    {"data": [[0,0,1]], "answer": [1,0,0]},
]

"""
LeetCode Easy.
제출 6.3M, 정답률 62.7%
풀긴 했는데 어려웠다.
처음엔 0을 찾을 때마다 제일 뒤로 보내고 다음 0을 배치할 인덱스를 기록했다.
그러니 0끼리도 교환이 돼서, 중간에 0을 만나면 i를 증가시키지 않아야 했다.
0을 만났을 때 교환을 안하면 또 포인터 처리가 까다로워져서 그렇게 했다.
그렇게 푸니 실행시간이 상당히 길었다.
풀이를 보니 나와 반대로 0이 아닌 숫자를 배치할 인덱스를 기록했다.
이렇게 하면 0을 따로 처리해줄 이유가 없어져서 O(n)으로 해결할 수 있다.
"""
import inspect

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    my_func(sol, *data)
    for a, b in zip(data[0], ans):
        if a != b:
            break
    else:
        res = ans
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
