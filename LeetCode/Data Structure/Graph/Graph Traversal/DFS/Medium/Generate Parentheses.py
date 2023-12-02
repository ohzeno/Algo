# https://leetcode.com/problems/generate-parentheses/
from typing import Optional, List
"""
constraints:
1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(s, l, r):
            if r == n:  # r이 n이 되기 전 l은 이미 n임
                ans.append(s)
                return
            if l < n:  # l n개 추가
                dfs(s+'(', l+1, r)
            if r < l:  # 괄호가 열린 갯수 만큼만 추가
                dfs(s+')', l, r+1)
        ans = []
        dfs('', 0, 0)
        return ans

inputdatas = [
    3, 1
]

"""
LeetCode Medium.
케이스를 다 만들어서 유효성 검사를 할까 했는데
dfs로 간단하게 해결할 수 있었다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
