# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
from typing import Optional, List

"""
n개의 작업에 대해 시작 시간, 종료 시간, 이익이 주어진다.
각 작업은 시작, 종료 시각 안에 완수해야 한다.
시간 범위가 겹치지 않게 이익을 최대화하라.

constraints:
1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # 작업 종료 시간을 기준으로 정렬
        jobs = sorted(zip(endTime, startTime, profit))
        dp = [0] * (n + 1)  # dp[i] = i번째 작업까지 완료했을 때 최대 이익
        for i, (ed, st, prof) in enumerate(jobs, 1):
            """
            i번째 작업을 추가할 수 있는 가장 늦은 시각을 찾는다.
            종료시각 목록에서 현 작업 시작 시간을 삽입할 수 있는 가장 오른쪽 인덱스를 찾는다.
            bisect_right를 사용했으므로 바로 앞의 종료시각과 중첩될 수 있다.
            [0, 10, 20, 30, 40]에 20을 삽입하면 3이 나온다는 뜻.
            그렇게 작업시간을 최대한 활용할 수 있다.
            lo, hi는 jobs[lo:hi]에서 삽입 위치를 찾는다는 것.
            i번째 작업이나, 1부터 시작했으니 hi는 i-1까지만.
            두번째 작업이면 :1로 둬서 첫 작업을 완료한 케이스까지만 고려한다는 것.
            dp[i-1]은 i번째 작업을 추가하지 않을 때의 최대 이익,
            dp[prev]는 i번째 작업을 추가할 경우의 최대 이익.
            i-1작업이 3~5이고 i번째 작업이 3~6이면,
            dp[prev]는 3까지 끝나는 작업만 고려했을 때의 최대 이익인 것이고
            dp[i-1]은 3~5인 작업까지 고려했을 때의 최대 이익이다.
            dp[prev]는 작업이 겹치지 않아야 하므로 3~5를 빼고 3~6을 더하는 것이다.
            어느 쪽이 이득일지는 모르니 max로 비교한다.
            말로 적으니 복잡한데 지문에 나온 그림을 보면 직관적이다.
            """
            prev = bisect_right(jobs, st, hi=i-1, key=lambda x: x[0])
            dp[i] = max(dp[i-1], dp[prev] + prof)
        return dp[n]


inputdatas = [
    [[[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]], 120],
    [[[1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]], 150],
    [[[1, 1, 1], [2, 3, 4], [5, 6, 4]], 6],
]

"""
LeetCode Hard.
제출 526.2K, 정답률 54.8%
중복 없이 최대한 작업을 밀어넣는 문제는 여럿 풀어봤었지만
'이익'이라는 요소까지 고려해야 하니 어려웠다.
결국 solutions를 보고 공부했다.
작업 스케줄링 문제의 상위 버전인듯.
"""
import inspect

sol = Solution()
functions = inspect.getmembers(sol, predicate=inspect.ismethod)
my_func = functions[0][1]
# for t in inputdatas:
#     print(my_func(*t))
for data, answer in inputdatas:
    res = my_func(*data)
    if res == answer:
        print("pass")
    else:
        print("fail\n", f"expected:{answer}\n", f"got:{res}\n")
