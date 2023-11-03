# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import Optional, List
"""
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idxs = {}  # {number: [index]}
        for i, n2 in enumerate(numbers, 1):
            dif = target - n2
            if dif in idxs:
                return [idxs[dif][0], i]  # 감소하지 않는 정렬이므로 i가 무조건 크다.
            idxs.setdefault(n2, []).append(i)

inputdatas = [
    [[2,7,11,15], 9],
    [[2,3,4], 6],
    [[-1,0], -1],
]

"""
LeetCode Medium
3sum을 실패한 후, Two sum II를 먼저 풀어보라기에 풀어봤다.
같은 원소를 두 번 사용하지 말라는 점이 좀 헷갈렸다. 
'감소하지 않는 정렬'이라고 했으니 중복원소가 있다는 건데,
[3, 3], 6 이런 경우 두 3이 같은 원소인지 아닌지 헷갈렸다.
일단 풀어보니 numbers[0]과 numbers[1]은 다른 원소였다.
전에 Pairs of Songs With Total Durations Divisible by 60에서 dict로 비슷한 풀이를 사용했었다.
처음에는 idxs를 먼저 다 기록하고 다시 순회를 했으나
한 번의 순회로도 해결할 수 있었다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t[0], t[1]))
