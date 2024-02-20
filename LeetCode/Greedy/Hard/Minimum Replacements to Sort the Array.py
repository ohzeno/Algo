# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
from typing import Optional, List

"""
정수 배열이 주어진다.
한 번의 작업으로 특정 원소를 교환할 수 있는데,
두 수를 더하여 그 원소가 되는 두 수로 교체할 수 있다.
예를 들면 [5, 6, 7]에서 6을 2, 4로 교체하여 
[5, 2, 4, 7]로 만들 수 있다.
감소하지 않는 배열로 만들기 위한 최소 작업 횟수를 리턴하라.

constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""
# from math import ceil
# class Solution:
#     def minimumReplacement(self, nums: List[int]) -> int:
#         ops = 0
#         small = nums.pop()
#         for num in reversed(nums):
#             if num < small:
#                 small = num
#             elif num > small:
#                 n_group = ceil(num / small)
#                 ops += n_group - 1
#                 small = num // n_group
#         return ops


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        small = nums.pop()
        for num in reversed(nums):
            if num < small:
                small = num
            elif num > small:
                q, r = divmod(num, small)
                if r:  # 나머지가 있다면 그룹 하나 더 필요
                    q += 1
                ops += q - 1  # 그룹 수 - 1번 연산이 필요함
                small = num // q  # 그룹 수로 나누고 내림
        return ops


inputdatas = [
    [[3, 9, 3], 2],
    [[1, 2, 3, 4, 5], 0],
    [[2, 10, 20, 19, 1], 47],
    [[12, 9, 7, 6, 17, 19, 21], 6],
]

"""
LeetCode Hard.
제출 117.7K, 정답률 53.7%
증가하지 않는 배열로 만들어야 하므로 뒤에서부터 순회하며 가장 작은 원소를 기록한다.
small보다 큰 원소가 나올 경우, 그룹을 나눠야 한다.
ceil을 사용하거나 divmod를 사용한다.
그룹 n개를 만드려면 n-1번의 작업이 필요하다.
나누어 떨어지면 n-1을 그대로 더하고
나머지가 있다면 q+1개의 그룹이 필요하다는 뜻이다.
그룹들의 수 중 가장 작은 수를 최대한 크게 유지해야 하므로
그룹 각각에 최대한 균등하게 나눠줘야 한다.
현 숫자를 그룹 수로 나눈 경우가 가장 균등한 경우고, 그 중 몇은 올리고 몇은 내려야 한다.
소수를 어떻게 분배하든 가장 작은 수는 내림인 경우이므로, 
//연산으로 나온 결과가 가장 작은 수가 된다.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
# for t in inputdatas:
#     print(my_func(*t))
for data, answer in inputdatas:
    res = my_func(data)
    if res == answer:
        print("pass")
    else:
        print("fail\n", f"expected:{answer}\n", f"got:{res}\n")
