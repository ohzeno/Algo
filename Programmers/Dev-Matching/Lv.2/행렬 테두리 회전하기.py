# https://school.programmers.co.kr/learn/courses/30/lessons/77485
"""
constraints:
  • rows는 2 이상 100 이하인 자연수입니다.
  • columns는 2 이상 100 이하인 자연수입니다.
  • 처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
    ◦ 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
  • queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
  • queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
    ◦ x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
    ◦ 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
    ◦ 모든 회전은 순서대로 이루어집니다.
    ◦ 예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.
"""

from collections import deque


def solution(rows, columns, queries):
    def rotate_edges(x1, y1, x2, y2):
        to_rotate = deque()
        x1, y1, x2, y2 = map(lambda x: x - 1, (x1, y1, x2, y2))
        to_rotate.extend(mat[x1][y1:y2 + 1])
        to_rotate.extend(mat[r][y2] for r in range(x1 + 1, x2 + 1))
        to_rotate.extend(reversed(mat[x2][y1:y2]))
        to_rotate.extend(mat[r][y1] for r in reversed(range(x1 + 1, x2)))
        to_rotate.rotate(1)
        min_num = min(to_rotate)
        for c in range(y1, y2 + 1):
            mat[x1][c] = to_rotate.popleft()
        for r in range(x1 + 1, x2 + 1):
            mat[r][y2] = to_rotate.popleft()
        for c in reversed(range(y1, y2)):
            mat[x2][c] = to_rotate.popleft()
        for r in reversed(range(x1 + 1, x2)):
            mat[r][y1] = to_rotate.popleft()
        return min_num

    mat = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    return [rotate_edges(*query) for query in queries]


inputdatas = [
    {"data": [6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]], "answer": [8, 10, 25]},
    {"data": [3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]], "answer": [1, 1, 5, 3]},
    {"data": [100, 97, [[1, 1, 100, 97]]], "answer": [1]}
]

"""
2021 Dev-Matching: 웹 백엔드 개발자(상반기)
Lv.2. 현 시점 완료한 사람 12,846명, 정답률 48%
이전 풀이에서 for문 일부를 extend로 변경하고 reversed를 이용해 직관성을 높였다.
rotate_edges 함수를 만들어서 코드를 분리했다.
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
