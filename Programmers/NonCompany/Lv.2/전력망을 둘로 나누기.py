# https://school.programmers.co.kr/learn/courses/30/lessons/86971
"""
constraints:
  • n은 2 이상 100 이하인 자연수입니다.
  • wires는 길이가 n-1인 정수형 2차원 배열입니다.
    ◦ wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
    ◦ 1 ≤ v1 < v2 ≤ n 입니다.
    ◦ 전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.
"""
from collections import deque

def solution(n, wires):
    def bfs(st, connects):
        visited = [0] * (n + 1)
        visited[st] = 1
        q = deque([st])
        cnt = 0
        while q:
            cur = q.popleft()
            cnt += 1
            for nxt in connects[cur]:
                if visited[nxt] == 0:
                    visited[nxt] = 1
                    q.append(nxt)
        return cnt
    l_wires = len(wires)
    min_diff = float('inf')
    for i in range(l_wires):
        connects = {i: [] for i in range(1, n+1)}
        for j in range(l_wires):
            if i == j:  # i번째 연결만 제외
                continue
            a, b = wires[j]
            connects[a].append(b)
            connects[b].append(a)
        group_a_cnt = bfs(1, connects)
        group_b_cnt = n - group_a_cnt
        diff = abs(group_a_cnt - group_b_cnt)
        min_diff = min(min_diff, diff)
    return min_diff


inputdatas = [
    {"data": [9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]], "answer": 3},
    {"data": [4, [[1,2],[2,3],[3,4]]], "answer": 0},
    {"data": [7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]], "answer": 1}
]


"""
완전탐색
Lv.2. 현 시점 완료한 사람 20,111명, 정답률 54%
Lv.2에 있을 문제가 아닌듯.
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
