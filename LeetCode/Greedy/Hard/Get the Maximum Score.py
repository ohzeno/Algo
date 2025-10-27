# https://leetcode.com/problems/get-the-maximum-score/description/
from typing import Optional, List

"""
constraints:
  • 1 <= nums1.length, nums2.length <= 10^5
  • 1 <= nums1[i], nums2[i] <= 10^7
  • nums1 and nums2 are strictly increasing.
"""


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        sum1, sum2 = 0, 0  # 현재 구간의 합
        result = 0
        # 두 배열을 동시에 순회
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:  # 공통 요소 발견
                # 두 구간 중 큰 값 선택 + 공통 요소 추가
                result += max(sum1, sum2) + nums1[i]
                sum1, sum2 = 0, 0  # 구간 합 초기화
                i += 1
                j += 1
        # 남은 요소들 더하기
        sum1 += sum(nums1[i:])
        sum2 += sum(nums2[j:])
        # 마지막 구간 처리
        result += max(sum1, sum2)
        return result % int(1e9+7)


inputdatas = [
    {"data": [[2, 4, 5, 8, 10], [4, 6, 8, 9]], "answer": 30},
    {"data": [[1, 3, 5, 7, 9], [3, 5, 100]], "answer": 109},
    {"data": [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], "answer": 40}
]

"""
LeetCode Hard.
제출 83.7K, 정답률 40.4%
처음엔 그래프 생성이나 누적합도 생각했다.
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
