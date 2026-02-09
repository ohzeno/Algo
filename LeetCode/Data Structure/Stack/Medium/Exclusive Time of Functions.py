# https://leetcode.com/problems/exclusive-time-of-functions/
from typing import Optional, List

"""
constraints:
  • 1 <= n <= 100
  • 2 <= logs.length <= 500
  • 0 <= function_id < n
  • 0 <= timestamp <= 10^9
  • No two start events will happen at the same timestamp.
  • No two end events will happen at the same timestamp.
  • Each function has an "end" log for each "start" log.
"""


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exc_time = [0] * n
        for log in logs:
            idx, typ, time = log.split(":")
            idx, time = int(idx), int(time)
            if typ == "start":
                if stack:
                    p_idx, p_st = stack[-1]
                    duration = time - p_st
                    exc_time[p_idx] += duration
                stack.append([idx, time])
            else:
                p_idx, p_st = stack.pop()
                duration = time + 1 - p_st
                exc_time[p_idx] += duration
                if stack:
                    stack[-1] = [stack[-1][0], time + 1]
        return exc_time


inputdatas = [
    {"data": [2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]], "answer": [3, 4]},
    {"data": [1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]], "answer": [8]},
    {"data": [2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]], "answer": [7, 1]}
]

"""
LeetCode Medium.
제출 507K, 정답률 66.1%
정답률은 높은데 start, end 시간 사용 방식이 달라서 까다로웠다.
재귀호출에서 꽤 애먹음
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
