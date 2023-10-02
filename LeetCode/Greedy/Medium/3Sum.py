# https://leetcode.com/problems/3sum/description/
from typing import Optional, List
"""
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nli, pli, zeros = [], [], 0
        res = set()
        for num in nums:
            if num < 0:
                nli.append(num)
            elif num > 0:
                pli.append(num)
            else:
                zeros += 1
        nset, pset = set(nli), set(pli)
        if zeros:  # 0이 있으면
            for n in nset:  # 음수들을 순회하면서
                if -n in pset:  # 대응하는 양수가 있으면 케이스 추가
                    res.add((n, 0, -n))
            if zeros > 2:  # 0이 3개 이상이면 0, 0, 0 케이스 추가
                res.add((0, 0, 0))
        for curli, oppset in ((nli, pset), (pli, nset)):  # nli, pli 모두 순회 해야한다. 각각에서 v1, v2뽑는 것이기 때문.
            for i, v1 in enumerate(curli):
                for j, v2 in enumerate(curli[i+1:]):  # li에서 2개를 뽑는 조합.
                    v3 = -(v1 + v2)  # v1, v2의 합의 반대값을 찾는다. li가 음수면 양의 세트에서. 양수면 음의 세트에서.
                    if v3 in oppset:  # 반대값이 있으면 정렬해서 케이스 추가
                        res.add(tuple(sorted([v1, v2, v3])))
        return res

inputdatas = [
    [-1, 0, 1, 2, -1, -4],
    [0, 1, 1],
    [0, 0, 0],
    [-1,0,1,2,-1,-4,-2,-3,3,0,4]
]

"""
LeetCode Medium
Two Sum에 비해 상당히 어려웠다. Hard 푸는 기분.
시간, 메모리 제약이 좀 컸다.
중복도 좀 까다로웠다.
0에 위치한 1과 1에 위차한 1은 같이 사용할 수 있지만, 
다른 인덱스를 사용하더라도 같은 값의 조합은 사용할 수 없다.
여러 풀이를 시도했고, 다른 사람의 풀이를 참조하여 위 풀이로 굳어졌다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
