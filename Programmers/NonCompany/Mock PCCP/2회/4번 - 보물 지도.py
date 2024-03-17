# https://school.programmers.co.kr/learn/courses/15009/lessons/121690
"""
nxm 보드.
상하좌우 이동 가능. 1칸 이동에 시간 1
n, m에 보물. 함정도 있음.
딱 한 번 2칸을 한 번에 이동할 수 있음.
보물이 있는 칸으로 이동하는 데 필요한 최소 시간 리턴.
불가능한 경우 -1 리턴.
1 ≤ n, m ≤ 1,000
    단, n * m이 3 이상인 경우만 입력으로 주어집니다.
1 ≤ hole의 길이 ≤ n * m - 2
    hole[i]는 [a, b]의 형태이며, (a, b) 칸에 함정이 존재한다는 의미이며,
        1 ≤ a ≤ n, 1 ≤ b ≤ m을 만족합니다.
    같은 함정에 대한 정보가 중복해서 들어있지 않습니다.
(1, 1) 칸과 (n, m) 칸은 항상 함정이 없습니다.
"""
from collections import deque


def solution(n, m, holes):
    holes = set((x - 1, y - 1) for x, y in holes)
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([(0, 0, 0, False)])  # x, y, time, jumped
    visited[0][0][0] = True  # x, y, jumped
    while q:
        x, y, t, jumped = q.popleft()
        steps = [1, 2] if not jumped else [1]
        for step in steps:
            njumped = jumped or step == 2
            for dx, dy in dirs:
                nx, ny = x + dx * step, y + dy * step
                if (
                    not (0 <= nx < n and 0 <= ny < m)
                    or (nx, ny) in holes
                    or visited[nx][ny][njumped]
                ):
                    continue
                if nx == n - 1 and ny == m - 1:
                    return t + 1
                visited[nx][ny][njumped] = True
                q.append((nx, ny, t + 1, njumped))
    return -1


inputdatas = [
    {"data": [4, 4, [[2, 3], [3, 3]]], "answer": 5},
    {"data": [4, 4, [[2, 3], [3, 3], [1, 3], [4, 3]]], "answer": 5},
    {
        "data": [
            5,
            4,
            [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]],
        ],
        "answer": -1,
    },
]

"""
[PCCP 모의고사 #2] 4번 - 보물 지도
다른 사람들이 4번을 제일 어렵다고 평가해서 bfs로 안풀릴 줄 알았는데, 단순 bfs다... 
기초 알고리즘이라 bfs를 모르는게 아니면 어려울 수가 없다.
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
