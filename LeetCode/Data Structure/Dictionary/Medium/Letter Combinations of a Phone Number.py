# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import Optional, List

"""
constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
2 ~ 9로 이루어진 숫자 문자열이 주어지면
각 숫자에 해당하는 문자들의 조합을 모두 구하라.
문자열 자판 참고.
https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png
"""


class Solution:
    characters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return self.characters[digits]
        result = []
        for c in self.characters[digits[0]]:
            for s in self.letterCombinations(digits[1:]):
                result.append(c + s)
        return result


inputdatas = [
    "23",
    "",
    "2",
]

"""
LeetCode Medium.
재귀로 풀었다. dfs bfs 다 될듯.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
for t in inputdatas:
    print(my_func(t))
