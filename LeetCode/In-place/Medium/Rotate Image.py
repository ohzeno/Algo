# https://leetcode.com/problems/rotate-image/
from typing import Optional, List

"""
constraints:
  • n == matrix.length == matrix[i].length
  • 1 <= n <= 20
  • -1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(n):
            matrix[r].reverse()


inputdatas = [
    {"data": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "answer": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]},
    {"data": [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]],
     "answer": [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]}
]

"""
LeetCode Medium.
제출 2.9M, 정답률 77.5%
예전에 풀었던 simulation/Spiral Matrix와 비슷한 문제다.
차이점은 그 당시에는 zip(*matrix)[::-1]으로 반시계 회전을 구현했고
이번 문제는 in-place가 요구되어 for문을 사용했다.
베스트 풀이를 보니 A[:] = zip(*A[::-1])로 in-place를 구현한 풀이가 있었다.
[::-1]은 새 객체를 생성하지만 [:]으로 할당하여 A는 in-place로 바뀌게 된다.
zip, [::-1] 모두 새 객체를 생성하니 엄격한 의미에서는 in-place는 아니다.
한국에선 거의 못 본 행렬 회전 문제들이지만 
난이도가 Medium인 것과 반응들을 보니 미국에선 꽤 알려진 듯.
"""
import inspect

functions = [value for value in Solution.__dict__.values() if inspect.isfunction(value)]
my_func = functions[0]
sol = Solution()
for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = my_func(sol, *data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
