# https://school.programmers.co.kr/learn/courses/30/lessons/120866
"""
constraints:
  • board는 n * n 배열입니다.
  • 1 ≤ n ≤ 100
  • 지뢰는 1로 표시되어 있습니다.
  • board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
"""


def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = 2
                for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1),
                             (i+1, j), (i+1, j+1)]:
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
                        board[x][y] = 2
    return sum(row.count(0) for row in board)


inputdatas = [
    {"data": [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]], "answer": 16},
    {"data": [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]], "answer": 13},
    {"data": [[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]], "answer": 0}
]


"""
코딩테스트 입문
Lv.0. 현 시점 완료한 사람 12,806명, 정답률 61%
간단한 2차원 배열 문제.
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
