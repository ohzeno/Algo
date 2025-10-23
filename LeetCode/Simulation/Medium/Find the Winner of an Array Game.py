# https://leetcode.com/problems/find-the-winner-of-an-array-game/
from typing import Optional, List

"""
constraints:
  • 2 <= arr.length <= 10^5
  • 1 <= arr[i] <= 10^6
  • arr contains distinct integers.
  • 1 <= k <= 10^9
"""
from collections import deque

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) - 1 <= k:
            return max(arr)
        q = deque(arr)
        champion = q.popleft()
        consecutive_wins = 0
        while consecutive_wins != k:
            challenger = q.popleft()
            if champion > challenger:
                winner, loser = champion, challenger
                consecutive_wins += 1
            else:
                winner, loser = challenger, champion
                consecutive_wins = 1
            q.append(loser)
            champion = winner
        return winner


inputdatas = [
    {"data": [[2, 1, 3, 5, 4, 6, 7], 2], "answer": 5},
    {"data": [[3, 2, 1], 10], "answer": 3},
    {"data": [[1,11,22,33,44,55,66,77,88,99], 1000000000], "answer": 99},
]

"""
LeetCode Medium.
제출 216.6K, 정답률 56.8%

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
