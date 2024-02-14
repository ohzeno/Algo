# https://leetcode.com/problems/trapping-rain-water/
from typing import Optional, List
"""
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        #leng = len(height)
        # wall = [0] * leng
        # wall[0] = height[0]
        # for i in range(1, leng):
        #     wall[i] = max(height[i], wall[i-1])
        # wall[-1] = height[-1]
        # for j in range(leng-2, -1, -1):
        #     if wall[j] < wall[j+1]:
        #         break
        #     wall[j] = max(height[j], wall[j+1])
        # cnt = 0
        # for i in range(leng):
        #     cnt += wall[i] - height[i]
        # return cnt
        ll, rr = 0, len(height)-1
        lh, rh = height[0], height[-1]
        ans = 0
        while ll <= rr:
            if lh <= rh:  # 같은 경우는 ll, rr 어느쪽을 갱신하든 상관없다.
                if height[ll] >= lh:
                    lh = height[ll]
                else:  # lh가 height[ll]보다 크면 물이 쌓일 수 있다.
                    ans += lh - height[ll]
                ll += 1
            else:
                if height[rr] >= rh:
                    rh = height[rr]
                else:
                    ans += rh - height[rr]
                rr -= 1
        return ans

inputdatas = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [4,2,0,3,2,5],
]

"""
LeetCode Hard.
15분정도 써서 초기 통과안을 만들었다.
양 방향에서 각각 순회를 돌며 지금까지 나온 최고 높이를 기록한다.
그리고 각 위치별로 두 방향 리스트에서 나온 최소값에 현 위치 벽의 높이를 빼면 물의 높이가 된다.
그걸 다 더해주면 물의 양이 나온다.

runtime beats가 25%정도길래 다른 풀이들을 살펴봤다.
투 포인터를 이용해 실시간으로 양쪽 높이 중 낮은 값에서 현재 높이를 빼서 더해줬다.
그렇게 하면 한 번의 순회만 하면 되고, 
최고높이를 실시간으로 사용하니 left, right 배열도 필요없어서 메모리도 절약된다.
하지만 방법을 떠올리기까지 시간이 걸리고, 각종 조건을 다루는게 귀찮다.

그래서 내가 푼 방법을 조금 더 개선해보았다.
왼쪽부터 순회를 한 번 돌고, 오른쪽부터 순회를 한 번 더 돌면서
오른쪽 최고높이보다 더 작은 벽이 나오면 순회를 중단한다.
그러면 min을 해줄 필요도 없고, 순회를 2n만큼 다 할 필요도 없다.

투포인터 풀이를 작성해봤다. 제출할 때마다 runtime, memory 순위가 달라진다.
서버 상태에 따라 노이즈가 심한 것 같다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
