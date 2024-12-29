# https://leetcode.com/problems/powx-n/
from typing import Optional, List
import math

"""
constraints:
  -100.0 < x < 100.0
  -2^31 <= n <= 2^31-1
  n is an integer.
  Either x is not zero or n > 0.
  -10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(base: float, exp: int) -> float:
            if exp == 0:
                return 1.0
            half = fastPow(base, exp // 2)
            if exp % 2 == 0:
                return half ** 2
            return base * half ** 2
        if n < 0:
            x = 1 / x
            n = -n
        return round(fastPow(x, n), 5)


inputdatas = [
    {"data": [2.00000, 10], "answer": 1024.00000},
    {"data": [2.10000, 3], "answer": 9.26100},
    {"data": [2.00000, -2], "answer": 0.25000}
]

"""
LeetCode Medium.
제출 5.5M, 정답률 36.1%
정석은 지수가 음수일 때 x뒤집고 n 반전시켜서 처리(재귀를 위해 지수를 양수로).
그 이후는 거듭제곱 분할정복.
두번째 테스트케이스가 부동소수점 오차 케이스로 추가됐는데, 문제 조건에는 없지만
output 예시들이 소수점 아래 5자리까지임. round(x ** n, 5)로 처리하면 통과됨.
이 테케때문에 기존 다른 풀이들 전부 오답처리된듯.
round만 쓰면 너무 꼼수같아서 거듭제곱 분할정복 사용해봤다. 그래도 round는 사용해야함...
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
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
