# https://school.programmers.co.kr/learn/courses/30/lessons/118670
"""
ShiftRow
    모든 행이 아래쪽으로 한 칸씩 밀림. 마지막 행은 첫 번째 행이 됨.
Rotate
    행렬의 테두리 원소들을 시계 방향으로 한 칸 회전.

행렬의 초기 상태가 담긴 2차원 정수 배열 rc, 시행할 연산이 담긴 operations가 주어질 때,
연산을 차례대로 시행한 후의 행렬 상태를 return하라.

2 ≤ len(rc[i]) ≤ 50,000
    rc의 모든 행 길이는 동일
2 ≤ len(rc) ≤ 50,000
    rc의 모든 열 길이는 동일
4 ≤ len(rc[i]) x len(rc) ≤ 100,000
rc[i][j] 는 i+1번째 행 j+1번째 열에 있는 원소
    1 ≤ rc[i][j] ≤ 1,000,000
1 ≤ len(operations) ≤ 100,000
    operations의 원소는 "ShiftRow" 혹은 "Rotate"
"""
from collections import deque
from itertools import groupby


class Matrix:
    def __init__(self, mat):
        self.r = len(mat)
        self.c = len(mat[0])
        self.unit = (self.r + self.c) * 2 - 4
        self.left, self.mid, self.right = deque(), deque(), deque()
        for row in mat:
            self.left.append(row[0])
            self.mid.append(deque(row[1:-1]))
            self.right.append(row[-1])

    def shift_row(self, n):
        self.left.rotate(n)
        self.right.rotate(n)
        self.mid.rotate(n)

    def rotate(self, n):
        for _ in range(n % self.unit):
            self.mid[0].appendleft(self.left.popleft())
            self.right.appendleft(self.mid[0].pop())
            self.mid[-1].append(self.right.pop())
            self.left.append(self.mid[-1].popleft())

    def get_mat(self):
        return [
            [self.left[i]] + list(self.mid[i]) + [self.right[i]] for i in range(self.r)
        ]


def solution(rc, cmds):
    mat = Matrix(rc)
    for cmd, group in groupby(cmds):
        cnt = len(list(group))
        if cmd == "ShiftRow":
            mat.shift_row(cnt)
        else:
            mat.rotate(cnt)
    return mat.get_mat()


inputdatas = [
    {
        "data": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]],
        "answer": [[8, 9, 6], [4, 1, 2], [7, 5, 3]],
    },
    {
        "data": [[[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]],
        "answer": [[8, 3, 3], [4, 9, 7], [3, 8, 6]],
    },
    {
        "data": [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            ["ShiftRow", "Rotate", "ShiftRow", "Rotate"],
        ],
        "answer": [[1, 6, 7, 8], [5, 9, 10, 4], [2, 3, 12, 11]],
    },
]

"""
2022 카카오 테크 인턴십 기출. 
Lv.4. 현 시점 완료한 사람 836명, 정답률 11%

항상 그렇지만 난이도와 별개로 어딘가에 풀이 하나만 올라오면 아무나 다 풀이 복붙으로 풀어 올린다.
물론 카카오 해설이 올라오긴 했지만 이건 절대로 836명이나 풀만한 문제가 아니다.

행렬 연산이라길래 변환행렬, 거듭제곱 분할정복 생각하고 들어왔는데 전혀 관련 없어서 좀 아쉬웠다.

ShiftRow는 변환행렬 거듭제곱을 이용한 변환행렬을 사용할 수 있지만 rotate는 불가능하다.
ShiftRow도 변환행렬 거듭제곱 사용한 연산 할 시간에 rotate 사용하는게 빠르다.
rotate때문에 행렬을 deque로 유지해야 해서 numpy도 사용하지 못한다.
처음에는 2차원 deque를 사용하고, rotate는 edges에 테두리를 담아서 n % unit만큼 회전시켜 봤다.
그러나 시간초과가 나서 결국 해설처럼 left, mid, right로 나누어서 관리했다.

사람들이 pop, appendleft를 사용해 ShiftRow를 하던데, 
그러면 매번 pop, append를 해야해서 비효율적이다.

shift는 행 수만큼 하면 제자리이고, rotate는 테두리 길이만큼 회전하면 제자리이므로 
나머지연산으로 남은 수만큼 하면 된다.

다른 풀이들은 unit을 사용한 사람이 없던데, 
효율성 테스트 결과를 보니 이게 필요한 케이스가 딱히 없어서 좀 실망스러웠다.

shift의 경우 deque.rotate가 어련히 최적화 되어 있겠지 싶어서 
n % r을 하지 않고 n을 바로 넣었다.
rotate의 경우 unit으로 나머지 연산한 만큼만 회전시켰다.

연산 자체의 중복도 테케에서 딱히 고려하지 않았던데,
일단 나는 카운팅해줘서 중복연산을 한꺼번에 처리했었다.
나중에 카운팅 부분을 itertools.groupby로 바꿨다.
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
