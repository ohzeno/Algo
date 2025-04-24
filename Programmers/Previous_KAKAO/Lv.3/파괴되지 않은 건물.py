# https://school.programmers.co.kr/learn/courses/30/lessons/92344
"""
constraints:
  • 1 ≤ board의 행의 길이 (= N) ≤ 1,000
  • 1 ≤ board의 열의 길이 (= M) ≤ 1,000
  • 1 ≤ board의 원소 (각 건물의 내구도) ≤ 1,000
  • 1 ≤ skill의 행의 길이 ≤ 250,000
  • skill의 열의 길이 = 6
  • skill의 각 행은 [type, r1, c1, r2, c2, degree]형태를 가지고 있습니다.
    ◦ type은 1 혹은 2입니다.
      ▪ type이 1일 경우는 적의 공격을 의미합니다. 건물의 내구도를 낮춥니다.
      ▪ type이 2일 경우는 아군의 회복 스킬을 의미합니다. 건물의 내구도를 높입니다.
    ◦ (r1, c1)부터 (r2, c2)까지 직사각형 모양의 범위 안에 있는 건물의 내구도를 degree 만큼 낮추거나 높인다는 뜻입니다.
      ▪ 0 ≤ r1 ≤ r2 < board의 행의 길이
      ▪ 0 ≤ c1 ≤ c2 < board의 열의 길이
      ▪ 1 ≤ degree ≤ 500
      ▪ type이 1이면 degree만큼 건물의 내구도를 낮춥니다.
      ▪ type이 2이면 degree만큼 건물의 내구도를 높입니다.
  • 건물은 파괴되었다가 회복 스킬을 받아 내구도가 1이상이 되면 파괴되지 않은 상태가 됩니다. 즉, 최종적으로 건물의 내구도가 1이상이면 파괴되지 않은 건물입니다.
"""


def solution(board, skill):
    w, h = len(board[0]), len(board)
    acc = [[0] * (w + 1) for _ in range(h + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        acc[r1][c1] += degree
        acc[r2 + 1][c1] -= degree
        acc[r1][c2 + 1] -= degree
        acc[r2 + 1][c2 + 1] += degree
    for c in range(1, w + 1):
        for r in range(h):
            acc[r][c] += acc[r][c - 1]
    for r in range(1, h + 1):
        for c in range(w + 1):
            acc[r][c] += acc[r - 1][c]
    cnt = 0
    for r in range(h):
        for c in range(w):
            if acc[r][c] + board[r][c] > 0:
                cnt += 1
    return cnt


inputdatas = [
    {"data": [[[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
              [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]], "answer": 10},
    {"data": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]],
     "answer": 6}
]


"""
2022 KAKAO BLIND RECRUITMENT
Lv.3. 현 시점 완료한 사람 5,862명, 정답률 42%
옮겨적기에만 4분 소모. 문제 읽고 주석 작성에 6분 소모.
초안 14분 30초에 완성. 정확성 테스트 통과, 효율성 테스트 전부 실패.
공격, 회복을 매번 순회하기에 당연한 결과. 스킬들 사용 누적값을 기록할 수 있다면 좋겠다고 생각했지만 방법이 떠오르지 않음.
오래 고민해도 답이 나올 문제가 아니라고 판단해서 질문들을 살펴봄. 누적합을 사용한다는 말들이 많음.
누적합을 사용한다는 아이디어는 이미 알고있었기에 도움이 되지 않음. 결국 해설을 살펴봤다.
해설에서 대략적인 아이디어를 얻은 후 1시간동안 구현, 통과.
구체적인 내용을 얻은게 아니었기에 초기에는 누적합 배열의 벽면에서는 케이스를 나눠 처리해줬다.
케이스가 많다보니 꼬였는데 그냥 밑, 오른쪽에 벽 하나를 더 세워주면 해결되는 문제였다.
참신한 케이스이긴 한데 현장에서 만나면 못풀었을 듯 하다.

2차. 이번에도 누적 방법을 못찾아서 다른 사람 풀이를 보다가 imos를 알게됐다.
알고나니 쉬운 문제. 
하지만 알고리즘 800문제 이상 푼 내가 몰랐다는 점에서 코테 준비가 정말 힘들다는 생각이 든다.
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