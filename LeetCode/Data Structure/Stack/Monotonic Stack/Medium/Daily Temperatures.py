# https://leetcode.com/problems/daily-temperatures/
from typing import Optional, List

"""
constraints:
  • 1 <= temperatures.length <= 10^5
  • 30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # (온도, 인덱스)
        for i in range(n - 1, -1, -1):
            cur_temp = temperatures[i]
            # 현재 온도보다 작거나 같은 온도들은 모두 제거
            while stack and stack[-1][0] <= cur_temp:
                stack.pop()
            if stack:  # 현재 온도보다 큰 온도가 남아있으면
                answer[i] = stack[-1][1] - i
            stack.append((cur_temp, i))
        return answer


inputdatas = [
    {"data": [[73, 74, 75, 71, 69, 72, 76, 73]], "answer": [1, 1, 4, 2, 1, 1, 0, 0]},
    {"data": [[30, 40, 50, 60]], "answer": [1, 1, 1, 0]},
    {"data": [[30, 60, 90]], "answer": [1, 1, 0]}
]

"""
LeetCode Medium.
제출 2.3M, 정답률 68.1%
950문제 이상 풀 동안 Monotonic Stack 개념을 몰랐다.
스택에 저장되는 값들이 단조 증가/감소를 유지하는 기법.
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
