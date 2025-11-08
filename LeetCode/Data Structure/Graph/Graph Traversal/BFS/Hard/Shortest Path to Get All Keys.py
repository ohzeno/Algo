# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
from typing import Optional, List

"""
constraints:
  • m == grid.length
  • n == grid[i].length
  • 1 <= m, n <= 30
  • grid[i][j] is either an English letter, '.', '#', or '@'.&nbsp;
  • There is exactly one&nbsp;'@'&nbsp;in the grid.
  • The number of keys in the grid is in the range [1, 6].
  • Each key in the grid is unique.
  • Each key in the grid has a matching lock.
"""
from collections import deque


class Solution:
    """
    '.': 빈 칸
    '#': 벽
    '@': 시작 지점
    소문자: 열쇠
    대문자: 자물쇠
    모든 열쇠 획득 필요 이동 횟수?
    불가능하면 -1 반환
    """
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def get_st():
            for r in range(lr):
                for c in range(lc):
                    if grid[r][c] == '@':
                        return r, c
        lr, lc = len(grid), len(grid[0])
        k = sum(1 for row in grid for ch in row if 'a' <= ch <= 'z')
        sr, sc = get_st()
        q = deque([(sr, sc, frozenset(), 0)])  # r, c, keys, 이동 횟수
        visited = {(sr, sc, frozenset())}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c, keys, step = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < lr and 0 <= nc < lc and (cell := grid[nr][nc]) != '#':
                    nkeys = keys
                    if 'a' <= cell <= 'z':  # 열쇠 획득
                        nkeys = keys | {cell}
                        if len(nkeys) == k:  # 모든 열쇠 획득
                            return step + 1
                    elif 'A' <= cell <= 'Z':  # 자물쇠
                        if cell.lower() not in keys:  # 열쇠 없으면 못 지나감
                            continue
                    nstate = (nr, nc, nkeys)
                    if nstate not in visited:
                        visited.add(nstate)
                        q.append((nr, nc, nkeys, step + 1))
        return -1


inputdatas = [
    {"data": [["@.a..", "###.#", "b.A.B"]], "answer": 8},
    {"data": [["@..aA", "..B#.", "....b"]], "answer": 6},
    {"data": [["@Aa"]], "answer": -1}
]

"""
LeetCode Hard.
제출 166K, 정답률 54.1%

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
