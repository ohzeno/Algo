# https://leetcode.com/problems/bulb-switcher/
from typing import Optional, List
"""
constraints:
0 <= n <= 10^9
"""
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


inputdatas = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

"""
LeetCode Medium.
제출 381k 정답률 52.6%
사람들의 평가는 '면접에서 이 질문을 받는다면 당신을 채용하기 싫다는 뜻이다'ㅋㅋ

10^9이니 for문으로는 불가하다.
하지만 작은 수는 가능하니 직접 배열을 만들어서 시뮬레이션 해보면서 규칙을 찾았다.
n을 1씩 키우면서 출력. 출력되는 수가 x라고 하면 x는 2x + 1회 출력된다.
출력값이 증가하는 부분들의 입력값을 모아보면 1, 4, 9, 16...
즉, 제곱수이다.
그냥 루트 씌워서 리턴하면 끝나는 문제.
규칙을 찾기까지 시간이 좀 걸릴 것이다.

아이큐 테스트에서 많이 다루는 문제고, 익숙하지만
그런 테스트는 일반항이 아니라 입력값 하나에 대해서 출력값을 구하는 것이고
이 문제는 일반항을 구해야한다.
면접에서 손코딩으로 해야한다고 하면 수열 공부한지 오래돼서 좀 헤맬 것 같다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
# counter = {}
# for i in range(1, 200):
#     counter.setdefault(my_func(i), 0)
#     counter[my_func(i)] += 1
# print(counter)