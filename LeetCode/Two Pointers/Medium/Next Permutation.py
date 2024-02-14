# https://leetcode.com/problems/next-permutation/
from typing import Optional, List
"""
constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        i = leng - 1
        while i > 0 and nums[i-1] >= nums[i]:  # 오름차순 찾기
            i -= 1
        if not i:  # 전체가 내림차순이면 오름차순으로.
            nums.reverse()
            return
        j = leng - 1
        while nums[i-1] >= nums[j]:  # 오른쪽에서 nums[i-1]보다 큰 수 중 가장 작은 수 찾기
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]  # 초기 순열보다 큰 순열로 만들고
        nums[i:] = nums[i:][::-1]  # nums[i-1]가 고정된 상태에서 가장 작은 수는 오른쪽이 오름차순.


inputdatas = [
    [1,2,3],
    [3,2,1],
    [1,1,5],
    [6,7,5,3,5,6,2,9,1,2,7,0,9]
]

"""
LeetCode Medium.
처음엔 permutations를 사용했으나 memory limit exceeded가 발생했다.
이후 방법이 생각나지 않아서 Editorial을 읽어본 후 구현했다.
자료구조를 추가로 사용하지 않고 입력을 변환하는 알고리즘을 in-place 알고리즘이라고 부른다고 한다.

이 풀이는 two pointer를 이용하고 있는데
우선 가장 큰 순열은 내림차순이고, 가장 작은 순열은 오름차순이다.
그러므로 우리가 바꿔야 할 부분은 오름차순인 부분이다.
사전순으로 정렬하라고 했으므로 int(nums.join(""))을 했을 때
지금 수보다 약간 큰 순열을 찾아야한다.
그러므로 자릿수가 작은 오른쪽부터 오름차순이 나오는 부분을 찾는다.

i=0이면 내림차순이므로 가장 작은 오름차순으로 바꾼 후 return한다.
이제 현재 순열보다 크게 만드려면 nums[i-1]를 더 큰 수와 교환해야 하는데, 
오른쪽에서 nums[i-1]보다 큰 수 중 
가장 작은 수와 바꿔야 바로 다음 순열이 된다.
그래서 j를 통해 찾아서 자리를 바꾸면 일단 초기보다 큰 순열이 된다.
하지만 우리가 찾던 것은 초기 순열 바로 다음의 순열이다.
그러므로 nums[i-1]은 그대로 두고, 뒤쪽을 가장 작은 오름차순으로 만들어준다.

그러면 초기 순열의 바로 다음 순열이 된다.
"""

import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for nums in inputdatas:
    functions[0][1](nums)
    print(nums)

