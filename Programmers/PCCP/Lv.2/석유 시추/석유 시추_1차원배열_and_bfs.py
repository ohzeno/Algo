# https://school.programmers.co.kr/learn/courses/30/lessons/250136
"""
nxm 땅. 시추관을 수직으로 단 하나만 뚫어서 뽑을 수 있는 가장 많은 석유량을 리턴하라.
가로지르기만 하면 뽑을 수 있음.

1 ≤ len(land) = 땅 세로길이 = n ≤ 500
    1 ≤ len(land[i]) = 땅 가로길이 = m ≤ 500
    land[i][j]는 i+1행 j+1열 땅의 정보를 나타냅니다.
    0은 빈 땅, 1은 석유.
"""
from collections import deque
def solution(land):
    def bfs(r, c):
        cols, size = set(), 0
        q = deque([(r, c)])
        visited.add((r, c))
        while q:
            r, c = q.popleft()
            cols.add(c)
            size += 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and land[nr][nc] and (nr, nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))
        for c in cols:
            sizes[c] += size

    n, m = len(land), len(land[0])
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    visited = set()
    sizes = [0] * m
    for i in range(n):
        for j in range(m):
            if land[i][j] and (i, j) not in visited:
                bfs(i, j)
    return max(sizes)



inputdatas = [
    {
        "data": [
            [
                [0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0],
                [1, 1, 0, 0, 0, 1, 1, 0],
                [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1],
            ]
        ],
        "answer": 9,
    },
    {
        "data": [
            [
                [1, 0, 1, 0, 1, 1],
                [1, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 1],
                [1, 0, 0, 1, 0, 0],
                [1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1],
            ]
        ],
        "answer": 16,
    },
]

"""
[PCCP 기출문제] 2번 / 석유 시추
Lv.2. 현 시점 완료한 사람 2204명, 정답률 30%
어째 pccp는 레벨에 비해 정답률이 낮은 문제들만 기출에 올라와 있는듯.
기출들 보면 lv.3중에 정답률 낮은 편이거나 lv.4 정답률 상위 사이에 pccp lv.1, lv.2가 끼어있다.

백준인지 SWEA인지 예전에 비슷한 문제를 푼 것 같은데 못찾겠다.
처음에는 스위핑으로 구현해서 코드가 길었다.
다른 풀이들을 보니 열별 석유량 배열을 사용했다. 이전에 비슷한 문제를 풀 때 나도 사용했던 것 같다.
간단한 방법 두고 괜히 어렵게 푼듯.

bfs로 풀어봤다.
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
