# https://leetcode.com/problems/sort-an-array/description/
from typing import Optional, List

"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

constraints:
1 <= nums.length <= 5 * 10^4
-5 * 10^4 <= nums[i] <= 5 * 10^4
"""


class Solution:
    def merge(self, l_arr, r_arr):
        sorted_arr = []  # 새 배열 생성
        li = ri = 0
        l_left, l_right = len(l_arr), len(r_arr)
        while li < l_left and ri < l_right:  # 한 배열이 끝날 때까지
            if l_arr[li] < r_arr[ri]:  # 작은 값을 새 배열에 추가
                sorted_arr.append(l_arr[li])
                li += 1
            else:
                sorted_arr.append(r_arr[ri])
                ri += 1
        # 각 배열은 정렬돼있으니 남은 배열은 그냥 붙여주면 됨.
        sorted_arr.extend(l_arr[li:])
        sorted_arr.extend(r_arr[ri:])
        return sorted_arr

    def merge_sort(self, arr):
        if len(arr) <= 1:  # 원소가 1개 이하면 그대로 반환
            return arr
        mid = len(arr) // 2
        l_arr = self.merge_sort(arr[:mid])  # 왼쪽 반 정렬
        r_arr = self.merge_sort(arr[mid:])  # 오른쪽 반 정렬
        return self.merge(l_arr, r_arr)  # 병합

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)


inputdatas = [
    {"data": [[5, 2, 3, 1]], "answer": [1, 2, 3, 5]},
    {"data": [[5, 1, 1, 2, 0, 0]], "answer": [0, 0, 1, 1, 2, 5]},
    {"data": [[5, 3, 8, 4, 9, 1, 6, 2, 7]], "answer": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
]

"""
LeetCode Medium.
제출 1M, 정답률 56.7%
정렬 복습할 겸 찾은 문제. 퀵정렬로 먼저 풀어봤는데
모든 원소가 같은 최악의 케이스가 있어서 시간초과(O(n^2))
그래서 최악의 경우에도 O(nlogn)인 병합정렬로 풀었다.
"""
import inspect

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[1]
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
