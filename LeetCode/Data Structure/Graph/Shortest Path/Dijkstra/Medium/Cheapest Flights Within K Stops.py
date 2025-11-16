# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
from typing import Optional, List

"""
constraints:
  • 1 <= n <= 100
  • 0 <= flights.length <= (n * (n - 1) / 2)
  • flights[i].length == 3
  • 0 <= from_i, to_i < n
  • from_i != to_i
  • 1 <= price_i <= 10^4
  • There will not be any multiple flights between two cities.
  • 0 <= src, dst, k < n
  • src != dst
"""
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = {i: [] for i in range(n)}
        for st, ed, cost in flights:
            g[st].append((ed, cost))
        # (누적비용, 현재 도시, 남은 스텝 횟수)
        pq = [(0, src, k+1)]
        # (도시, 남은 스텝) -> 최소비용
        visited = {}
        while pq:
            acc_cost, mid, steps = heappop(pq)
            if mid == dst:  # 누적 비용 오름차순으로 뽑고 음수 간선 없어서 첫 도착이 최소비용
                return acc_cost
            if steps > 0:
                key = (mid, steps)
                # 기존보다 비용 크면 패스
                if key in visited and visited[key] <= acc_cost:
                    continue
                visited[key] = acc_cost
                for ed, me_cost in g[mid]:
                    heappush(pq, (acc_cost + me_cost, ed, steps - 1))
        return -1


inputdatas = [
    {"data": [4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1], "answer": 700},
    {"data": [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1], "answer": 200},
    {"data": [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0], "answer": 500}
]

"""
LeetCode Medium.
제출 2M, 정답률 40.9%
다익스트라 응용 버전.
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
