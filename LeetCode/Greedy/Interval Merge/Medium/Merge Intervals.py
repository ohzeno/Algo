# https://leetcode.com/problems/merge-intervals/
from typing import Optional, List
"""
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        s, e = intervals[0]
        for s2, e2 in intervals:
            if s2 <= e:
                e = max(e, e2)
            else:
                ans.append([s, e])
                s, e = s2, e2
        ans.append([s, e])
        return ans
        # leng = len(intervals)
        # for i in range(leng):
        #     a = intervals[i]
        #     if not a:
        #         continue
        #     for j in range(i+1, leng):
        #         b = intervals[j]
        #         if a[1] >= b[0]:
        #             a[1] = max(a[1], b[1])
        #             intervals[j] = None
        #         else:
        #             break
        #     ans.append(a)
        # return ans


inputdatas = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]],
]

"""
LeetCode Medium
생각보다 어려워서 22분에 통과했다.
다른 풀이를 보니 s, e를 따로 기록해두면 훨씬 깔끔하게 진행할 수 있었다.
해당 방법으로 다시 풀어봤더니 코드는 깔끔해졌는데 메모리 사용량이 좀 늘었다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
