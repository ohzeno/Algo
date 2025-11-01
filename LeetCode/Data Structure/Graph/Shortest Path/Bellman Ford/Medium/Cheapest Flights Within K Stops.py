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

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = {i: [] for i in range(n)}
        for st, ed, cost in flights:
            g[st].append((ed, cost))
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k + 1):
            # k노드만 거칠 수 있으므로 이번 라운드에서 갱신된 값이
            # 라운드 내에서 영향을 미치지 않도록 복사본 사용
            tmp_dist = dist[:]
            for mid in g:
                if dist[mid] == INF:
                    continue
                for ed, me_cost in g[mid]:
                    new_cost = dist[mid] + me_cost
                    if new_cost < tmp_dist[ed]:
                        tmp_dist[ed] = new_cost
            dist = tmp_dist
        return dist[dst] if dist[dst] != INF else -1


inputdatas = [
    {"data": [4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1], "answer": 700},
    {"data": [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1], "answer": 200},
    {"data": [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0], "answer": 500}
]

"""
LeetCode Medium.
제출 2M, 정답률 40.9%
밸만포드 응용. 원본과 달리 dist 복사본을 이용하여 k개의 노드만 경유한다.
또한 음수 간선을 검토하지 않음.
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
