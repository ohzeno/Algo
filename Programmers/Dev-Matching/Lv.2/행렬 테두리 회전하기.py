# https://school.programmers.co.kr/learn/courses/30/lessons/77485
"""
"""
from collections import deque


def solution(rows, columns, queries):
    mat = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    ans = []
    for x1, y1, x2, y2 in queries:
        to_rotate = deque()
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        for c in range(y1, y2 + 1):
            to_rotate.append(mat[x1][c])
        for r in range(x1 + 1, x2 + 1):
            to_rotate.append(mat[r][y2])
        for c in range(y2 - 1, y1 - 1, -1):
            to_rotate.append(mat[x2][c])
        for r in range(x2 - 1, x1, -1):
            to_rotate.append(mat[r][y1])
        ans.append(min(to_rotate))
        to_rotate.rotate(1)
        for c in range(y1, y2 + 1):
            mat[x1][c] = to_rotate.popleft()
        for r in range(x1 + 1, x2 + 1):
            mat[r][y2] = to_rotate.popleft()
        for c in range(y2 - 1, y1 - 1, -1):
            mat[x2][c] = to_rotate.popleft()
        for r in range(x2 - 1, x1, -1):
            mat[r][y1] = to_rotate.popleft()
    return ans


inputdatas = [
    [6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]],
    [3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]],
    [100, 97, [[1, 1, 100, 97]]],
]

"""
2021 Dev-Matching: 웹 백엔드 개발자(상반기) 기출. 
Lv.2. 현 시점 완료한 사람 10,917명, 정답률 46%
옮겨적기부터 제출, 채점까지 8분 걸렸다.
그냥 rotate를 썼다.
prev를 기록해서 순회를 하면서 교체해주는 방법도 있다.
그렇게 하면 deque에 넣지 않기 때문에 매번 min연산을 해줘야하는 번거로움이 있다.
for문 순회는 적어지는데 min연산이 늘고 
prev를 넣는다는 부분이 직관성이 좀 떨어질 수 있다.

테두리 도는 과정이 같아서 함수로 뺄까 했는데 
그러면 if else로 기록과 회전을 나눠야 해서 오히려 라인 수가 늘어난다.
가독성과 기능분리 면에서는 그쪽이 좋긴 하다.
"""

for t in inputdatas:
    print(solution(*t))
