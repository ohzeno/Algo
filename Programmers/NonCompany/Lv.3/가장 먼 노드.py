# https://school.programmers.co.kr/learn/courses/30/lessons/49189
"""
constraints:
  • 노드의 개수 n은 2 이상 20,000 이하입니다.
  • 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
  • vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
"""
from heapq import heappush, heappop
from collections import defaultdict, Counter

def solution(n, edge):
    inf = 20000 * 50000 + 1
    connects = defaultdict(list)
    for a, b in edge:
        connects[a].append((b, 1))
        connects[b].append((a, 1))
    dists = [inf] * (n + 1)
    dists[1] = 0
    q = [(0, 1)]
    while q:
        # 빠른 가지치기를 위해 누적 cost가 제일 작은 경우를 뽑음
        sm_cost, mid = heappop(q)
        if dists[mid] < sm_cost:  # 이미 더 작은 값이 있으면 넘어감
            continue
        # 현재 노드 경유하여 비용 갱신
        for ed, me_cost in connects[mid]:
            new_cost = sm_cost + me_cost
            if new_cost < dists[ed]:
                dists[ed] = new_cost
                heappush(q, (new_cost, ed))
    cnts = Counter(dists[2:])
    return cnts.get(max(cnts), 0)


inputdatas = [
    {"data": [6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]], "answer": 3}
]


"""
그래프
Lv.3. 현 시점 완료한 사람 24,586명, 정답률 49%
정석 다익스트라는 시간초과 난다.
오랜만이라 다익스트라 로직을 다시 찾아봤다.
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
