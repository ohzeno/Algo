# https://school.programmers.co.kr/learn/courses/30/lessons/43164
"""
constraints:
  • 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
  • 주어진 공항 수는 3개 이상 10,000개 이하입니다.
  • tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
  • 주어진 항공권은 모두 사용해야 합니다.
  • 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
  • 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
"""
from collections import deque

def solution(tickets):
    tickets.sort()
    connects = {}
    for idx, (a, b) in enumerate(tickets):
        connects.setdefault(a, []).append((b, idx))
    n = len(tickets)
    candidates = []
    q = deque([(['ICN'], set())])
    while q:
        path, visited = q.popleft()
        for nxt, ticket_idx in connects.get(path[-1], []):
            if ticket_idx in visited:
                continue
            tmp_path = path + [nxt]
            tmp_visited = visited | {ticket_idx}
            if len(tmp_visited) == n:
                candidates.append(tmp_path)
                continue
            q.append((tmp_path, tmp_visited))
    candidates.sort()
    return candidates[0]


inputdatas = [
    {"data": [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]], "answer": ["ICN", "JFK", "HND", "IAD"]},
    {"data": [[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]], "answer": ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]},
    {"data": [[["ICN", "JFK"], ["ICN", "JFK"], ["JFK", "HND"], ["HND", "ICN"], ["JFK", "ATL"]]], "answer": ["ICN", "JFK", "HND", "ICN", "JFK", "ATL"]},
]


"""
깊이/너비 우선 탐색(DFS/BFS)
Lv.3. 현 시점 완료한 사람 26,285명, 정답률 49%
모든 공항 방문이 아니라 모든 항공권 사용, 중복 티켓 가능성.
LV.3이라고 하기엔 너무 어려운 듯 하다.
'모든 도시를 방문할 수 없는 경우는 주어지지 않습니다'
여기선 bfs로 풀긴 했지만 오일러 경로-히어홀쳐(Hierholzer's algorithm) 알고리즘 문제.
한국에선 알려지지 않은 듯.
"""

for inputdata in inputdatas:
    data, ans = inputdata["data"], inputdata["answer"]
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        summary = "fail"
        for label, content in [("expected:", ans), ("got:", res)]:
            summary += f"\n  {label}\n"
            summary += f"    {content}"
            summary = summary.rstrip()
        print(summary)
