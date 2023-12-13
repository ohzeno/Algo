# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
from typing import Optional, List
"""
constraints:
1 <= tasks.length <= 10^5
1 <= tasks[i] <= 10^9
"""
from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        t = 0
        for v in Counter(tasks).values():
            if v == 1:
                return -1
            n3, d3 = divmod(v, 3)
            if not d3:
                t += n3
            else:
                t += n3 + 1
        return t

inputdatas = [
    # [2, 2, 3, 3, 2, 4, 4, 4, 4, 4],
    # [2, 3, 3],
    [69,65,62,64,70,68,69,67,60,65,69,62,65,65,61,66,68,61,65,63,60,66,68,66,67,65,63,65,70,69,70,62,68,70,60,68,65,61,64,65,63,62,62,62,67,62,62,61,66,69],
    [66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]
]

"""
LeetCode Medium.
엄청 고생했는데 케이스별로 나눠서 풀어야 했다.
같은 난이도를 2, 3개 선택할 수 있으므로
1회 등장한 경우 해결 불가능하다.
나머지는 3k, 3k+1, 3k+2가 있는데
3k인 경우 k라운드
3k+1 = 3(k-1)+3+1 = 3(k-1)+2+2 이므로 k-1+2 = k+1라운드
3k+2인 경우 k+1라운드

여기서 더 축약한 사람은 (v+2)//3으로 식을 통일했다.
(3k+2)//3 = k
(3k+1+2)//3 = k+1
(3k+2+2)//3 = k+1
하지만 이렇게까지 식을 찾을 필요는 없고, 직관적이지 않으므로 위쪽 풀이를 사용했다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
