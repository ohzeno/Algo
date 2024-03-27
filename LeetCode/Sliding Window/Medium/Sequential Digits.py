# https://leetcode.com/problems/sequential-digits/description/
from typing import Optional, List

"""
이전 숫자보다 하나 큰 숫자로만 이루어진 숫자를 순차적 숫자라고 함. 
예를 들어, 1234, 5678, 23456789 등
[low, high] 범위의 순차적 숫자를 모두 배열에 담아 정렬하여 return 하라.
constraints:
10 <= low <= high <= 10^9
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        nd = "123456789"
        # 자릿수 설정
        for l in range(len(str(low)), len(str(high)) + 1):
            for st in range(10 - l):  # 시작점 순회
                seq = int(nd[st : st + l])
                if low <= seq <= high:
                    ans.append(seq)
        return ans


inputdatas = [
    {"data": [100, 300], "answer": [123, 234]},
    {"data": [1000, 13000], "answer": [1234, 2345, 3456, 4567, 5678, 6789, 12345]},
    {"data": [90, 300], "answer": [123, 234]},
    {"data": [10, 10], "answer": []},
    {"data": [234, 2314], "answer": [234, 345, 456, 567, 678, 789, 1234]},
]

"""
LeetCode Medium.
제출 321.5K, 정답률 65.4%
처음엔 다음 시퀀스를 구하는 함수를 만들었다. nd를 쓰긴 했지만 경우에 따라 인덱싱을 다르게 했다.
코드가 좀 난잡했었는데 더 간결하게 처리하는 코드를 보고 수정해봤다.
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
