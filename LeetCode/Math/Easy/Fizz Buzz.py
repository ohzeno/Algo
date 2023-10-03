# https://leetcode.com/problems/fizz-buzz/
"""
1 <= n <= 104
"""
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []
        for i in range(1, n+1):
            if i % 15 == 0:  # 3, 5로 모두 나누어 떨어지는지 보려면 15로 나누어 보면 된다.
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans

inputdatas = [
    3, 5, 15
]
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))

"""
LeetCode Easy.
2분도 안걸렸다. 더 좋은 풀이가 있나 풀이들을 봤는데 큰 차이는 없었다.
"""
