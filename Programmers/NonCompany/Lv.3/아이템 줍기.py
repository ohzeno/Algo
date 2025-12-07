# https://school.programmers.co.kr/learn/courses/30/lessons/87694
"""
constraints:
  • rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
  • rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
    ◦ 직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
    ◦ 서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
    ◦ 문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
  • charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
    ◦ 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
  • itemX, itemY는 1 이상 50 이하인 자연수입니다.
    ◦ 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
  • 캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.
"""
from collections import deque

def solution(rectangles, characterX, characterY, itemX, itemY):
    mat = [[0] * 101 for _ in range(101)]
    for i in range(len(rectangles)):
        rectangles[i] = [x * 2 for x in rectangles[i]]
        x1, y1, x2, y2 = rectangles[i]
        for r in range(x1, x2+1):
            for c in range(y1, y2+1):
                mat[r][c] = 1
    for x1, y1, x2, y2 in rectangles:
        for r in range(x1+1, x2):
            for c in range(y1+1, y2):
                mat[r][c] = 0
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    q = deque([(characterX, characterY, 0)])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = {(characterX, characterY)}
    while q:
        x, y, dist = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            # 사각형좌표가 1 이상임
            if (nx, ny) not in visited and 1 <= nx < 101 and 1 <= ny < 101 and mat[nx][ny] == 1:
                if nx == itemX and ny == itemY:
                    return (dist + 1) // 2
                visited.add((nx, ny))
                q.append((nx, ny, dist + 1))


inputdatas = [
    {"data": [[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8], "answer": 17},
    {"data": [[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1], "answer": 11},
    {"data": [[[1,1,5,7]], 1, 1, 4, 7], "answer": 9},
    {"data": [[[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10], "answer": 15},
    {"data": [[[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3], "answer": 10}
]


"""
깊이/너비 우선 탐색(DFS/BFS)
Lv.3. 현 시점 완료한 사람 8,047명, 정답률 29%
경계선 추출 문제.
Lv.3에 있을 문제가 아니다.
과거에 비슷한 문제를 풀어본 것 같은데 잘 기억 안난다.
2배 해주는 이유는 ㄷ자처럼 경계가 붙어있을경우 bfs에서 끝에서 끝으로 웜홀 통과하듯 움직이기 때문.
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
