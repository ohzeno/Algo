# https://leetcode.com/problems/number-of-islands/
from typing import Optional, List
"""
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            visited[r][c] = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < lr and 0 <= nc < lc and grid[nr][nc] == "1" and not visited[nr][nc]:
                    dfs(nr, nc)
        dirs = [1, 0], [-1, 0], [0, 1], [0, -1]
        lr, lc = len(grid), len(grid[0])
        visited = [[0] * lc for _ in range(lr)]
        cnt = 0
        for r in range(lr):
            for c in range(lc):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    cnt += 1
        return cnt

inputdatas = [
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ],
    [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
]

"""
LeetCode Medium
전형적인 섬 갯수 세기 문제.
문제 읽기, input 값 옮겨적기부터 풀이까지 7분 정도 걸렸다.
visited를 사용했는데, 다른 풀이를 보니 
dfs에서 방문한 땅을 전부 0으로 만들어 진입하지 않도록 했다.
다음에 내키면 시도해 봐야겠다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
for t in inputdatas:
    print(functions[0][1](t))
