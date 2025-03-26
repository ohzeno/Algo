# https://school.programmers.co.kr/learn/courses/30/lessons/64061
"""
constraints:
  • board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
  • board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
    ◦ 0은 빈 칸을 나타냅니다.
    ◦ 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
  • moves 배열의 크기는 1 이상 1,000 이하입니다.
  • moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
"""


def solution(board, moves):
    """
    nxn격자. 위쪽 크레인. 오른쪽 바구니.
    인형은 아래부터 쌓임. 크레인으로 뽑은 인형은 바구니에 담김
    같은 잉형 둘이 바구니에 연속으로 쌓이면 터짐
    board: 격자.
    moves: 크레인 작동 위치
    모두 작동시킨 후 터진 인형 개수 return
    """
    stack = []
    exploded = 0
    n = len(board)
    for move in moves:
        move -= 1
        for h in range(n):
            if board[h][move] != 0:
                doll = board[h][move]
                if stack and stack[-1] == doll:
                    stack.pop()
                    exploded += 2
                else:
                    stack.append(doll)
                board[h][move] = 0
                break
    return exploded


inputdatas = [
    {"data": [
        [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]],
        [1, 5, 3, 5, 1, 2, 1, 4]
    ],
        "answer": 4}
]

"""
2019 카카오 개발자 겨울 인턴십
Lv.1. 현 시점 완료한 사람 45,230명, 정답률 53%
문제 읽고 인풋데이터 옮겨적기를 포함해 채점까지 12분 50초정도 걸렸다.
간단한 스택문제.
2회차. 6분.
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
