# https://leetcode.com/problems/two-sum/
"""
2 <= nums.length <= 10^4
-109 <= nums[i] <= 10^9
-109 <= target <= 10^9
Only one valid answer exists.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # leng = len(nums)
        # for i in range(leng):
        #     for j in range(i + 1, leng):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        idxs = {}
        for i, n2 in enumerate(nums):
            dif = target - n2
            if dif in idxs:
                return [idxs[dif], i]
            # 중복값인데 if문을 통과하지 못했으면 target이 될 수 없으니 덮어써도 된다.
            idxs[n2] = i


inputdatas = [
    [[2,7,11,15], 9],
    [[3,2,4], 6],
    [[3,3], 6],
]

"""
LeetCode Easy. 제한이 빡빡하지 않아서 그냥 2중 for문으로 풀었다.
여러 풀이들이 있는 듯 한데 쉬운 문제고, 너무 여럿이라 살펴보진 않았다.

2차시도
hashmap 카테고리 학습문제로 나와서 이번엔 딕셔너리를 사용해 풀었다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t[0], t[1]))