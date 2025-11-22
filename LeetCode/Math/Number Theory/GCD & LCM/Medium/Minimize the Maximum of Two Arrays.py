# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/
from typing import Optional, List

"""
constraints:
  • 2 <= divisor1, divisor2 <= 10^5
  • 1 <= uniqueCnt1, uniqueCnt2 < 10^9
  • 2 <= uniqueCnt1 + uniqueCnt2 <= 10^9
"""
import math

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)

    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # 최소공배수
        lcm = math.lcm(divisor1, divisor2)

        def can_distribute(mid):
            # arr1에 사용 가능한 숫자 개수 (divisor1으로 나누어떨어지지 않는 숫자)
            available_for_arr1 = mid - mid // divisor1

            # arr2에 사용 가능한 숫자 개수 (divisor2으로 나누어떨어지지 않는 숫자)
            available_for_arr2 = mid - mid // divisor2

            # 둘 다 사용 가능한 숫자 개수 (lcm으로 나누어떨어지지 않는 숫자)
            available_for_both = mid - mid // lcm

            # 세 가지 조건 모두 만족해야 함
            return (available_for_arr1 >= uniqueCnt1 and
                    available_for_arr2 >= uniqueCnt2 and
                    available_for_both >= uniqueCnt1 + uniqueCnt2)

        ll, rr = 1, 2 * (uniqueCnt1 + uniqueCnt2)
        succeeded = None
        while ll <= rr:
            mid = (ll + rr) // 2
            if can_distribute(mid):
                succeeded = mid
                rr = mid - 1
            else:
                ll = mid + 1
        return succeeded


inputdatas = [
    {"data": [2, 7, 1, 3], "answer": 4},
    {"data": [3, 5, 2, 1], "answer": 3},
    {"data": [2, 4, 8, 2], "answer": 15},
    {"data": [12, 3, 2, 10], "answer": 14},
]

"""
LeetCode Medium.
제출 50K, 정답률 31.5%
lcm 아이디어 떠올리기가 힘들다.
math 못쓰는 경우가 있을까 싶긴 한데 gcd, lcm 구현 오랜만에 다시 해봤다.

rr을 2 * (uniqueCnt1 + uniqueCnt2)로 둔 이유
최악의 경우 d1, d2가 모두 2인 경우다.
이 경우 arr1, arr2에 모두 홀수만 넣을 수 있고 그러면 u1 + u2개의 홀수가 필요하다.
d1, d2가 모두 짝수이므로 모든 홀수가 가능하여 2 * (u1 + u2) 이내에서 해결된다.
d1, d2가 커지면 같은 바운드 내에서 사용 가능한 수가 더 많아지므로 2 * (u1 + u2)가 한계.
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
