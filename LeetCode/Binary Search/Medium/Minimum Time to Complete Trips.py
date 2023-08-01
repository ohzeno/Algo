# https://leetcode.com/problems/minimum-time-to-complete-trips/
from typing import Optional, List
"""
constraints:
1 <= time.length <= 10^5
1 <= time[i], totalTrips <= 10^7
"""
from bisect import bisect_left
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # ll, rr = 1, min(time) * totalTrips
        # while ll < rr:
        #     mid = (ll + rr) // 2
        #     cnt = sum(map(lambda x: mid//x, time))
        #     if cnt < totalTrips:
        #         ll = mid + 1
        #     else:
        #         rr = mid
        # return ll
        return bisect_left(
            range(1, min(time) * totalTrips),
            totalTrips,
            key=lambda t: sum(t//x for x in time)
        ) + 1


inputdatas = [
    [[1, 2, 3], 5],
    [[2], 1],
    [[5, 10, 10], 9],
]

"""
LeetCode Medium.
이분탐색을 푼지 너무 오래됐는지
이분탐색을 적용한다는 생각을 하지 못했다.
bisect_left에 key가 있다는 것도 처음 알았다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(*t))
