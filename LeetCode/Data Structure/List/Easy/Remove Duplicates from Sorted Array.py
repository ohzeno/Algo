# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import Optional, List
"""
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # dup = set()
        # cnt = 0
        # for i in range(len(nums)):
        #     if nums[i] not in dup:
        #         dup.add(nums[i])
        #         nums[cnt] = nums[i]
        #         cnt += 1
        # return cnt
        nums[:] = sorted(set(nums))
        return len(nums)

inputdatas = [
    [[1, 1, 2], 2],
    [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5]
]

"""
LeetCode Easy.
1분만에 작성하고 실행했는데, 예제 통과를 못했다.
k를 return하라고 했는데 return하면 예제를 틀렸다.
문제에 nums를 수정하라는 말이 있다. 
nums를 반환하지 않는데 nums를 왜 바꾸라는지 이해 못했다.

custom judge가 무슨 언어인지 몰라서 보지 않고 넘어갔었는데, 
removeDuplicates에 nums 객체를 전달하기에,
함수 안에서 nums를 수정하면 함수 밖의 nums가 수정된다.
그 후 nums를 평가한다.

원본 배열을 수정하는 nums[:] = 데이터 방식을 처음 사용했다.
[:]가 우변에 있을 경우 nums의 값들을 가져와서 새로운 리스트를 만들어 좌변에 할당한다.
하지만 [:]가 좌변에 있을 경우 nums의 주소값은 유지되고 내부 값들이 우변으로 수정된다.
[::]와 기능적으로는 동일하나, 객체 전체를 선택할 때는 [:]를 주로 사용한다고 한다.
특이한 평가방식.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for nums, n in inputdatas:
    k = functions[0][1](nums)
    expected = sorted(set(nums))
    for i in range(k):
        if nums[i] != expected[i]:
            print("Wrong answer")
            break
    else:
        if k != n:
            print("Wrong answer")
        else:
            print("Correct answer")
