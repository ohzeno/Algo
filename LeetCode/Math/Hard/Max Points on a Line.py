# https://leetcode.com/problems/max-points-on-a-line/
from typing import Optional, List
"""
constraints:
1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
"""
# def ccw(a, b, c):
#     # x1, y1 = b[0] - a[0], b[1] - a[1]
#     # x2, y2 = c[0] - a[0], c[1] - a[1]
#     # return x1 * y2 - y1 * x2
#     return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        max_cnt = 2
        for i in range(n-1):
            p1 = points[i]
            # for j in range(i+1, n):
            #     p2 = points[j]
            #     cnt = 0
            #     for k in range(j+1, n):
            #         # if ccw(points[i], points[j], points[k]) == 0:
            #         if ccw(p1, p2, points[k]) == 0:
            #             cnt += 1
            #     max_cnt = max(max_cnt, cnt)
            slopes = {}
            for j in range(i+1, n):
                p2 = points[j]
                slope = (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2[0] != p1[0] else 'INF'
                slopes.setdefault(slope, 0)
                slopes[slope] += 1
            max_cnt = max(max_cnt, max(slopes.values()) + 1)  # +1은 시작점 추가
        return max_cnt

inputdatas = [
    [[1, 1], [2, 2], [3, 3]],
    [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
    [[0, 0], [1, 1], [-1, -1]],
    [[0, 0], [1, 0], [-1, 0]]
]

"""
LeetCode Hard.
어떻게 풀어야 할지 생각나지 않아서 몇 초 당황했지만 익숙한 ccw를 이용해서 풀었다. 
하지만 이렇게 풀면 O(n^3)이라 느리다.

2중 for문으로 시작점에 대해 기울기 딕셔너리를 만들고
딕셔너리에 각 점들이 이루는 기울기를 카운팅하여 최대값을 구하면
O(n^2)으로 빠르게 풀 수 있다.
Runtime 66ms Beats 99.30%

p1, p2, p3에서 p1->p2와 p1->p3가 일직선상에 있을 경우 
분모 분자가 동시에 부호가 바뀌므로 p1->p2와 p1->p3의 기울기는 같다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
