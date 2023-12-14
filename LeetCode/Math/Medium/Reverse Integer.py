# https://leetcode.com/problems/reverse-integer/
from typing import Optional, List
"""
constraints: -2^31 <= x <= 2^31 - 1
"""
class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = int(str(abs(x))[::-1])
        if neg:
            x = -x
        return x if -2 ** 31 <= x <= 2 ** 31 - 1 else 0

inputdatas = [
    123, -123, 120, -8463847412
]

"""
LeetCode Medium.
%와 //로 풀 수 있을테지만 귀찮아서 스트링을 이용했다.

32비트 정수의 범위를 초과하는 경우 0을 반환하라고 한다.
32비트 범위를 구체적으로는 몰랐는데, 32비트 정수의 범위는 -2^31 ~ 2^31 - 1라고 한다.
64비트 정수를 저장할 수 없다고 가정하라고 한다. 
아마 reverse 이후 64비트 초과하는 경우가 있어서
%와 //로 연산 도중 32비트 초과하면 0 반환하라고 한 것 같은데
아무도 reverse 도중에 32비트 확인은 하지 않았다...

처음에는 들어오는 x에도 범위 검사를 했고, 다른 사람도 그걸 지적했지만
제약 사항에 따라 들어오는 x는 항상 32비트 정수다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
