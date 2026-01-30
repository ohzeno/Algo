# https://leetcode.com/problems/valid-sudoku/
from typing import Optional, List

"""
constraints:
  • board.length == 9
  • board[i].length == 9
  • board[i][j] is a digit 1-9 or '.'.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_block(r, c):
            seen = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = board[i][j]
                    if val != '.':
                        if val in seen:
                            return False
                        seen.add(val)
            return True

        def row_check(r, c):
            seen = set()
            for i in range(9):
                val = board[r][i]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
            return True

        def col_check(r, c):
            seen = set()
            for i in range(9):
                val = board[i][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
            return True

        for r in range(9):
            for c in range(9):
                if r % 3 == 0 and c % 3 == 0:
                    if not check_block(r, c):
                        return False
                if c == 0:
                    if not row_check(r, c):
                        return False
                if r == 0:
                    if not col_check(r, c):
                        return False
        return True


inputdatas = [
    {"data": [[["5", "3", ".", ".", "7", ".", ".", ".", "."]
                  , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                  , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                  , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                  , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                  , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                  , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                  , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                  , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]], "answer": True},
    {"data": [[["8", "3", ".", ".", "7", ".", ".", ".", "."]
                  , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                  , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                  , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                  , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                  , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                  , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                  , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                  , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]], "answer": False},
    {"data": [[[".", ".", "4", ".", ".", ".", "6", "3", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."],
               ["5", ".", ".", ".", ".", ".", ".", "9", "."],
               [".", ".", ".", "5", "6", ".", ".", ".", "."],
               ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
               [".", ".", ".", "7", ".", ".", ".", ".", "."],
               [".", ".", ".", "5", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."]]], "answer": False}
]

"""
LeetCode Medium.
제출 3.7M, 정답률 64.0%
노가다.
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
