# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    # RT CF JM AN
    # choices 1~7은 매우 비동의 ~ 매우 동의
    # 1~3은 왼쪽 유형 3~1점, 4는 통과, 5~7은 오른쪽 유형 1~3점
    answer = ''
    orders = ["RT", "CF", "JM", "AN"]
    mbti = {}
    for order in orders:
        mbti[order[0]] = 0
        mbti[order[1]] = 0

    def pointing(question, answer):
        if answer == 1:
            mbti[question[0]] += 3
        elif answer == 2:
            mbti[question[0]] += 2
        elif answer == 3:
            mbti[question[0]] += 1
        elif answer == 5:
            mbti[question[1]] += 1
        elif answer == 6:
            mbti[question[1]] += 2
        elif answer == 7:
            mbti[question[1]] += 3

    for i, choice in enumerate(choices):
        pointing(survey[i], choice)
    for order in orders:
        left, right = order[0], order[1]
        if mbti[left] >= mbti[right]:  # 지표는 이미 정렬돼있음. 같은 값이면 왼쪽.
            answer += left
        else:
            answer += right
    return answer

inputdatas = [
    [["AN", "CF", "MJ", "RT", "NA"],
     [5, 3, 2, 7, 5]],
    [["TR", "RT", "TR"],
     [7, 1, 3]]
]

"""
2022 카카오 테크 인턴십 기출. Lv.1. 옮겨적기부터 채점까지 18분 걸렸다.
지표번호를 읽고 입력데이터를 보니 성격유형이 매 테케에 따로 주어지는 줄 알고
지표번호를 찾기 위해 한참 시간을 낭비했다. 그 외에는 어려울 것 없는 문제.
"""
for t in inputdatas:
    print(solution(t[0], t[1]))
