# https://school.programmers.co.kr/learn/courses/30/lessons/92344
def solution(board, skill):
    # 숫자는 내구도. 공격/회복은 직사각형.
    # 0 이하는 파괴지만 회복 가능.
    # 게임 끝난 뒤 파괴되지 않은 건물 개수 리턴
    # skill의 각 행은 [type, r1, c1, r2, c2, degree]
    # type 1: 적의 공격, 2: 회복
    # (r1, c1)부터 (r2, c2)까지 직사각형 degree만큼 스킬적용.
    height, width = len(board), len(board[0])
    acc = [[0] * (width + 1) for _ in range(height + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        # 범위 다음 줄을 0으로 처리하기 위해 마지막 행, 열 다음 줄에 기록을 해줘야 한다.
        acc[r1][c1] += degree
        acc[r2 + 1][c1] -= degree
        acc[r1][c2 + 1] -= degree
        acc[r2 + 1][c2 + 1] += degree
    # 오른쪽, 아래방향 누적합 시행
    for i in range(height):
        for j in range(1, width):  # 0열은 처리 필요X
            acc[i][j] += acc[i][j - 1]
        if i != 0:  # 첫 행은 처리 필요 X
            for j in range(width):
                acc[i][j] += acc[i - 1][j]
    ans = 0
    # 순회하며 스킬 누적값을 원래 건물에 더해서 파괴되지 않은 경우 += 1
    for i in range(height):
        for j in range(width):
            if acc[i][j] + board[i][j] > 0:
                ans += 1
    return ans

inputdatas = [
    [
        [
            [5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5],
        ],
        [
            [1, 0, 0, 3, 4, 4],
            [1, 2, 0, 2, 3, 2],
            [2, 1, 0, 3, 1, 2],
            [1, 0, 1, 3, 3, 1]
        ]
    ],
    [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [1, 1, 1, 2, 2, 4],
            [1, 0, 0, 1, 1, 2],
            [2, 2, 0, 2, 0, 100]
        ]
    ]
]

"""
2022 카카오 공채 기출. Lv.3. 옮겨적기에만 4분 소모. 문제 읽고 주석 작성에 6분 소모.
초안 14분 30초에 완성. 정확성 테스트 통과, 효율성 테스트 전부 실패.
공격, 회복을 매번 순회하기에 당연한 결과. 스킬들 사용 누적값을 기록할 수 있다면 좋겠다고 생각했지만 방법이 떠오르지 않음.
오래 고민해도 답이 나올 문제가 아니라고 판단해서 질문들을 살펴봄. 누적합을 사용한다는 말들이 많음.
누적합을 사용한다는 아이디어는 이미 알고있었기에 도움이 되지 않음. 결국 해설을 살펴봤다.
해설에서 대략적인 아이디어를 얻은 후 1시간동안 구현, 통과.
구체적인 내용을 얻은게 아니었기에 초기에는 누적합 배열의 벽면에서는 케이스를 나눠 처리해줬다.
케이스가 많다보니 꼬였는데 그냥 밑, 오른쪽에 벽 하나를 더 세워주면 해결되는 문제였다.
참신한 케이스이긴 한데 현장에서 만나면 못풀었을 듯 하다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))

def solution1(board, skill):
    # 숫자는 내구도. 공격/회복은 직사각형.
    # 0 이하는 파괴지만 회복 가능.
    # 게임 끝난 뒤 파괴되지 않은 건물 개수 리턴
    # skill의 각 행은 [type, r1, c1, r2, c2, degree]
    # type 1: 적의 공격, 2: 회복
    # (r1, c1)부터 (r2, c2)까지 직사각형 degree만큼 스킬적용.
    for ski in skill:
        r1, c1, r2, c2, degree = ski[1], ski[2], ski[3], ski[4], ski[5]
        if ski[0] == 1:
            degree = -degree
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                board[r][c] += degree
    height, width = len(board), len(board[0])
    ans = 0
    for i in range(height):
        for j in range(width):
            if board[i][j] > 0:
                ans += 1
    return ans