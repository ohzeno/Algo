# https://leetcode.com/problems/flood-fill/?envType=study-plan&id=level-1
from typing import Optional, List
"""
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2^16
0 <= sr < m
0 <= sc < n
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r, c):
            image[r][c] = color
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < lr and 0 <= nc < lc and image[nr][nc] == origin_color:
                    dfs(nr, nc)
        lr, lc = len(image), len(image[0])
        origin_color = image[sr][sc]
        if origin_color == color:  # 오리진과 인접한 같은 색을 변경할 예정이므로 이미 같으면 순회 의미가 없음.
            return image
        dfs(sr, sc)
        return image

inputdatas = [
    [[[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2],
    [[[0,0,0],[0,0,0]], 0, 0, 0]
]

"""
LeetCode Easy
전형적인 dfs문제.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t[0], t[1], t[2], t[3]))
