# https://leetcode.com/problems/unique-number-of-occurrences/
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # cnt_dic = Counter(arr)
        # return len(cnt_dic) == len(set(cnt_dic.values()))
        vcnt = set()
        for v in Counter(arr).values():
            if v in vcnt:
                return False
            vcnt.add(v)
        return True

inputdatas = [
    [1,2,2,1,1,3],
    [1,2],
    [-3,0,1,-3,1,1,1,-3,10,0]
]
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))

"""
LeetCode Easy. 
처음엔 Counter와 len을 사용했다. 생각보다 runtime beats 22.33%. 하위권이었다.
Counter의 value를 순회하며 set에 추가하고, 추가 전에 set에 이미 있는지 확인하니
runtime beats 90.88%가 되었다. 메모리 사용량은 딱히 크게 변하지 않았다.
"""

