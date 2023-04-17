# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    """
    1: RT, 2: CF, 3: JM, 4: AN
    총 n개 질문, 7개 선택지.
    1~7 예시 1번지표면 R3~0~T3 점수
    RT가 아니라 TR처럼 뒤집어져 나올 수도 있음.
    하나의 지표에서 양쪽 점수가 같으면 사전순으로 빠른 성격 유형을 선택.
    질문별 지표가 담긴 survey, 질문별 선택지가 담긴 choices가 주어질 때,
    성격 유형을 지표 번호 순서대로 return
    """
    mbti = {}
    for cha, chose in zip(survey, choices):
        a, b = cha
        mbti.setdefault(a, 0)
        mbti.setdefault(b, 0)
        if chose == 1:
            mbti[a] += 3
        elif chose == 2:
            mbti[a] += 2
        elif chose == 3:
            mbti[a] += 1
        elif chose == 5:
            mbti[b] += 1
        elif chose == 6:
            mbti[b] += 2
        elif chose == 7:
            mbti[b] += 3
    ans = ''
    for a, b in ["RT", "CF", "MJ", "AN"]:
        pa, pb = mbti.get(a, 0), mbti.get(b, 0)
        if pa > pb:
            ans += a
        elif pa < pb:
            ans += b
        else:  # min이 글자도 사전순 정렬해줌.
            ans += min(a, b)
    return ans

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

2차 시도. 12분 걸렸다. JM을 미리 정렬하지 않고 min을 사용했다.
setdefault, get, zip을 사용해 몇 줄 짧아졌다.
"""
for t in inputdatas:
    print(solution(t[0], t[1]))
