# https://leetcode.com/problems/container-with-most-water/
from typing import Optional, List
"""
constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        water = 0
        while l < r:
            water = max(water, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water

inputdatas = [
    [1,8,6,2,5,4,8,3,7],
    [1,1],
]

"""
LeetCode Medium.
이분탐색 자체는 사람들이 많이 사용했지만
처음 봤을 때 h[l] == h[r]일 때의 탐색에 대한 의구심이 들었다.
아니나 다를까 그에 대한 많은 토론이 있었지만 제대로된 증명은 없었다.
저 많은 사람들이 왜 이 간단한 부분을 증명하지 못할까 의아하다.

결론부터 말하면 h[l] == h[r]일 때는 l+=1, r-=1 어느쪽이든 상관없다.
1. 안쪽 기둥이 바깥보다 낮은 경우 
    76...17같은 경우다. 
    이러면 r-=1을 하면 67 대신 71이 되어 더 작아질 수 있다.
    하지만 이런 경우 안쪽 기둥이 77보다 낮기 때문에 더 큰 면적이 나올 수 없어서 상관없다.
2. 안쪽이 바깥 기둥보다 높은 경우
    37...63 이런 경우 어느쪽을 옮기든 간에 면적은 3*(w-1)이 되므로 차이가 없다.
3. 안쪽기둥이 바깥보다 한쪽은 낮고 한쪽은 높은 경우다.
    43...74 왼쪽을 옮기면 3*(w-1)이 되고 오른쪽을 옮기면 4*(w-1)이 된다. 47...34도 마찬가지다.
    어느 쪽이든 현재 넓이인 4*w보다 작아서 문제가 없다.
    안쪽에서 더 넓은 케이스가 나올 수 있으나, 어느쪽 기둥을 옮기든 안쪽 케이스는 체크할 수 있다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
