# https://leetcode.com/problems/frog-jump/
from typing import Optional, List
"""
constraints:
2 <= stones.length <= 2000
0 <= stones[i] <= 2^31 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.
개구리가 강을 건너려 한다. 마지막 돌에 도착하면 성공.
개구리는 첫 돌에서 출발하고, 첫 점프는 1 단위라고 가정.
k단위 점프 후에는 k-1 또는 k+1단위 점프 가능.
앞으로만 점프 가능
돌 리스트가 주어지면, 개구리가 강을 건널 수 있는지 여부를 리턴하라.
"""
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dfs(cur, prek):
            nonlocal success
            if cur == stones[-1]:
                success = True
                return
            visited.add((cur, prek))
            for k in range(prek - 1, prek + 2):
                if k < 1:
                    continue
                nxt = cur + k
                if nxt in stone_set and (nxt, k) not in visited:
                    dfs(nxt, k)
        stone_set = set(stones)
        visited = set()
        success = False
        dfs(0, 0)
        return success


inputdatas = [
    [0, 1, 3, 5, 6, 8, 12, 17],
    [0, 1, 2, 3, 4, 8, 9, 11],
]

"""
LeetCode Hard.
제출 230.2K, 정답률 51.6%
Hard이고 stone이 2^31-1까지 커지길래 
dfs 하다보면 시간초과 나지 않을까 했는데
그냥 통과해서 맥빠졌다.
Editorial은 dp인데 dfs랑 다를게 없는 재귀라서 의미가 없어보인다.
가장 빠른 풀이는 bfs다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
