# https://leetcode.com/problems/unique-paths/?envType=study-plan&id=level-1
from typing import Optional, List
"""
1 <= m, n <= 100
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # 왼쪽과 위쪽에서 올 수 있으므로 둘을 더해준다.
        return dp[-1][-1]

inputdatas = [
    [3, 7],
    [3, 2],
]

"""
LeetCode Medium.
전형적인 dp문제.
얼마 전에 코테에서 똑같은 문제를 풀었었다. 
math.factorial을 import해서 조합으로 풀 수도 있다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t[0], t[1]))
