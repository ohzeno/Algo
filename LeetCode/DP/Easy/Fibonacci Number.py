# https://leetcode.com/problems/fibonacci-number/?envType=study-plan&id=level-1
from typing import Optional, List
"""
0 <= n <= 30
"""
from functools import cache
class Solution:
    @cache  # 파이썬 3.9부터 가능함. fib 밖에 둬야 매번 새로 생성 안하니 캐시됨.
    def dp(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.dp(n - 1) + self.dp(n - 2)
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        # a, b = 0, 1  # swap 이용한 dp.
        # for _ in range(n):
        #     a, b = b, a+b
        # return a
        return self.dp(n)


inputdatas = [
    2, 3, 4
]

"""
LeetCode Easy.
피보나치. 전형적인 dp 문제

다른 풀이를 보다보니 @cache가 보여서 알아봤다.
파이썬 3.9부터 functools에 추가된 데코레이터로,
함수의 결과를 캐싱해놓고, 같은 인자로 호출되면 캐싱된 값을 반환한다.
여러 알고리즘에서 메모이제이션을 간단하게 할 수 있어서 상당히 유용해보인다.
코테에서 사용이 가능할지는 모르겠다.

다른 풀이에서는 fib 안에 dp함수를 만들고 cache 데코레이터를 달아줬다.
하지만 그렇게 하면 fib가 호출될 때마다 dp함수가 새로 생성되기에 cache를 활용할 수 없다.
그래서 solution 클래스의 메서드로 dp를 만들고 cache를 달아줬다.

그 밖에도 a, b = b, a+b 처럼 자주 쓰이던 피보나치 기법도 다시 연습해봤다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
