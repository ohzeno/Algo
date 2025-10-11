# https://school.programmers.co.kr/learn/courses/30/lessons/118669
"""
constraints:
  • 2 ≤ n ≤ 50,000
  • n - 1 ≤ paths의 길이 ≤ 200,000
  • paths의 원소는 [i, j, w] 형태입니다.
    ◦ i번 지점과 j번 지점을 연결하는 등산로가 있다는 뜻입니다.
    ◦ w는 두 지점 사이를 이동하는 데 걸리는 시간입니다.
    ◦ 1 ≤ i < j ≤ n
    ◦ 1 ≤ w ≤ 10,000,000
    ◦ 서로 다른 두 지점을 직접 연결하는 등산로는 최대 1개입니다.
  • 1 ≤ gates의 길이 ≤ n
    ◦ 1 ≤ gates의 원소 ≤ n
    ◦ gates의 원소는 해당 지점이 출입구임을 나타냅니다.
  • 1 ≤ summits의 길이 ≤ n
    ◦ 1 ≤ summits의 원소 ≤ n
    ◦ summits의 원소는 해당 지점이 산봉우리임을 나타냅니다.
  • 출입구이면서 동시에 산봉우리인 지점은 없습니다.
  • gates와 summits에 등장하지 않은 지점은 모두 쉼터입니다.
  • 임의의 두 지점 사이에 이동 가능한 경로가 항상 존재합니다.
  • return 하는 배열은 [산봉우리의 번호, intensity의 최솟값] 순서여야 합니다.
"""
from collections import deque

def solution(n, paths, gates, summits):
    """
    n개 지점. 1~n번호. 출입구, 쉼터, 산봉우리
    각 지점은 양방향 통행 가능한 등산로로 연결됨
    등산로별로 시간 소요.
    등산코스의 intensity: 휴식 없이 이동해야 하는 시간 중 가장 긴 시간
    한 출입구에서 봉우리 하나 찍고 같은 출입구로 돌아오기.
    다른 출입구 방문X, 산봉우리 여럿 방문 X
    summits: 산봉우리
    paths 원소: [i, j, w] i에서 j로 통하는 등산로 시간 w.
    최소 intensity 등산코스에 포함된 [산봉우리, intensity] 반환
    코스가 여럿이면 산봉우리 번호가 가장 낮은 등산코스.
    """
    graph = {i: [] for i in range(1, n + 1)}
    getes_set = set(gates)
    summits_set = set(summits)
    for st, ed, w in paths:
        if ed not in getes_set:
            graph[st].append((ed, w))
        if st not in getes_set:
            graph[ed].append((st, w))
    for i in range(1, n + 1):
        graph[i].sort(key=lambda x: x[1])
    intensity_to = [float('inf')] * (n + 1)
    q = deque()
    for gate in gates:
        q.append((gate, 0))
        intensity_to[gate] = 0
    while q:
        cur, intensity = q.popleft()
        if intensity > intensity_to[cur]:
            continue
        if cur in summits_set:
            continue
        for nxt, w in graph[cur]:
            new_intensity = max(intensity, w)
            if new_intensity < intensity_to[nxt]:
                intensity_to[nxt] = new_intensity
                q.append((nxt, new_intensity))
    min_top = -1
    min_intensity = float('inf')
    for summit in sorted(summits_set):
        if intensity_to[summit] < min_intensity:
            min_top = summit
            min_intensity = intensity_to[summit]
    return [min_top, min_intensity]


inputdatas = [
    {"data": [6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]],
     "answer": [5, 3]},
    {"data": [7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]], "answer": [3, 4]},
    {"data": [7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]],
     "answer": [5, 1]},
    {"data": [5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]], "answer": [5, 6]},
    {"data": [5, [[5, 4, 1], [5, 3, 1], [3, 2, 2], [4, 2, 1], [2, 1, 1]], [1], [5]], "answer": [5, 1]},
    {"data": [4, [[1, 3, 1], [1, 4, 1], [4, 2, 1]], [1], [2, 3, 4]], "answer": [3, 1]},
]

"""
2022 KAKAO TECH INTERNSHIP
Lv.3. 현 시점 완료한 사람 3,483명, 정답률 29%
2회차.
bfs로 풀어보려다 한시간 넘게 썼다. 
예전에도 lv.4급이라고 생각했는데 이번에도 어려웠다.
이전에는 정답률 22%였는데 그 사이 2300여명이 블로그 복붙을 했는지 정답률이 29%로 올라와 있다.
정답률 30% 문제 하나 풀려다가 22% 문제에 낚인 샘.
다익스트라는 sm, me cost를 더해준다는 인상이 강했고 
이건 max(sm cost, me cost)라 다익스트라로 어떻게 푸는건지 상상하지 못했다.
물론 저번에 dfs로 풀었으니 이번엔 bfs로 풀어보겠다고 다익스트라 없이 하려 했다.
결과적으론 사실상 다익스트라와 유사한 결과가 나왔다.
다음엔 다익스트라로 풀어봐야겠다.
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
