# https://leetcode.com/problems/spiral-matrix/
from typing import Optional, List
"""
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # w, h = len(matrix[0]), len(matrix)
        # visited = [[0] * w for _ in range(h)]
        # dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # ans = []
        # def dfs(r, c, d):
        #     visited[r][c] = 1
        #     ans.append(matrix[r][c])
        #     nr, nc = r + dirs[d][0], c + dirs[d][1]
        #     if d == 0 and (nc >= w or visited[nr][nc]):
        #         d = 1
        #         nr, nc = r + dirs[d][0], c + dirs[d][1]
        #     elif d == 1 and (nr >= h or visited[nr][nc]):
        #         d = 2
        #         nr, nc = r + dirs[d][0], c + dirs[d][1]
        #     elif d == 2 and (nc < 0 or visited[nr][nc]):
        #         d = 3
        #         nr, nc = r + dirs[d][0], c + dirs[d][1]
        #     elif d == 3 and (nr < 0 or visited[nr][nc]):
        #         d = 0
        #         nr, nc = r + dirs[d][0], c + dirs[d][1]
        #     if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
        #         dfs(nr, nc, d)
        #     else:
        #         return
        # dfs(0, 0, 0)
        # return ans
        ans = []
        while matrix:
            ans += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return ans


inputdatas = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
]

"""
LeetCode Medium.
처음엔 유사 dfs로 풀었다. 
더 나은 풀이를 찾다보니 zip을 이용한 기가막힌 풀이들이 있어서 연습해봤다.
zip(*matrix)는 matrix의 전치행렬이다.
이를 [::-1]로 뒤집으면 matrix를 반시계방향으로 90도 회전한 행렬이 된다.
제일 윗 줄을 pop으로 제거하므로 visited도 필요없다.

numpy 없이 전치행렬을 저렇게 구현하는 것을 처음 봤다.
그리고 행렬 회전을 저렇게 구현하는 것도 처음 봤다.
"""
import inspect
sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
