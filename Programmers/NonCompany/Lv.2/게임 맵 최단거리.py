# https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""
constraints:
  • maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
    ◦ n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
  • maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
  • 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.
"""
from collections import deque
def solution(maps):
    lr, lc = len(maps), len(maps[0])
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque([(lr-1, lc-1, 1)])
    visited = {(lr - 1, lc - 1)}
    while q:
        r, c, dist = q.popleft()
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < lr and 0 <= nc < lc and (nr, nc) not in visited and maps[nr][nc] == 1:
                if nr == 0 and nc == 0:
                    return dist + 1
                q.append((nr, nc, dist + 1))
                visited.add((nr, nc))
    return -1


inputdatas = [
    {"data": [[[1,0,1,1,1],
               [1,0,1,0,1],
               [1,0,1,1,1],
               [1,1,1,0,1],
               [0,0,0,0,1]]], "answer": 11},
    {"data": [[[1,0,1,1,1],
               [1,0,1,0,1],
               [1,0,1,1,1],
               [1,1,1,0,0],
               [0,0,0,0,1]]], "answer": -1}
]


"""
깊이/너비 우선 탐색(DFS/BFS)
Lv.2. 현 시점 완료한 사람 37,888명, 정답률 64%
dfs로 풀었는데 효율성 테스트를 통과 못해서 bfs로 다시 풀었다...
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
