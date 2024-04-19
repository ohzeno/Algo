# https://leetcode.com/problems/buildings-with-an-ocean-view/description/
from typing import Optional, List

"""
There are n buildings in a line. 
You are given an integer array heights of size n 
that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. 
A building has an ocean view if the building can see the ocean without obstructions. 
Formally, a building has an ocean view 
if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings 
that have an ocean view, sorted in increasing order.

constraints:
1 <= heights.length <= 10^5
1 <= heights[i] <= 10^9
"""

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        max_h = 0
        for i in reversed(range(len(heights))):
            if heights[i] > max_h:
                ans.append(i)
                max_h = heights[i]
        return ans[::-1]


inputdatas = [
    {"data": [[4,2,3,1]], "answer": [0,2,3]},
    {"data": [[4,3,2,1]], "answer": [0,1,2,3]},
    {"data": [[1,3,2,4]], "answer": [3]},
]

"""
LeetCode Medium.
제출 250.9K, 정답률 79.5%
초보 시절 백준에서 풀었던 문제와 같은 로직.
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
