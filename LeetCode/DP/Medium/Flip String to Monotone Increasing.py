# https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""
1 <= s.length <= 10^5
s[i] is either '0' or '1'.
"""
from typing import Optional, List
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0 if s[0] == '0' else 1  # 현재까지 1의 갯수
        leng = len(s)
        dp = [0] * leng  # dp[0]은 안바꿔도 모노톤 인크리징(이하 mi)이므로 0.
        for i in range(1, leng):
            """
            dp[i]는 s[:i + 1]까지의 문자열을 mi로 만드는 최소 횟수이다.
            마지막 문자가 0이면 
                ones: 앞쪽의 1을 전부 뒤집어서 mi로 만든다.
                dp[i-1] + 1: 마지막 문자를 1로 바꿔(+1) mi로 만든다.
                앞쪽 끝이 0이든 1이든 끝에 1을 붙이면 mi다.
            """
            if s[i] == '0':
                dp[i] = min(dp[i-1] + 1, ones)
            else:  # 마지막 문자가 1이면 바꾸지 않아도 조건을 만족한다.
                dp[i] = dp[i-1]  # 바꾸지 않았으니 이전 값
                ones += 1  # 1의 갯수를 증가시킨다.
        return dp[-1]


inputdatas = [
    "00110",
    "010110",
    "00011000",
    '11011',
    '0101100011'
]

"""
LeetCode Medium
dp는 역시 어렵다. 더 깔끔하게 작성할 수 있지만 dp 이해도를 높이기 위해 dp테이블을 이용했다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
