# https://school.programmers.co.kr/learn/courses/30/lessons/118666
"""
constraints:
  • 1 ≤ survey의 길이 ( = n) ≤ 1,000
    ◦ survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나입니다.
    ◦ survey[i]의 첫 번째 캐릭터는 i+1번 질문의 비동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
    ◦ survey[i]의 두 번째 캐릭터는 i+1번 질문의 동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
  • choices의 길이 = survey의 길이
    ◦ choices[i]는 검사자가 선택한 i+1번째 질문의 선택지를 의미합니다.
    ◦ 1 ≤ choices의 원소 ≤ 7
"""
from collections import defaultdict

def solution(survey, choices):
    points = defaultdict(int)
    for mbti, choice in zip(survey, choices):
        if choice == 4:
            continue
        l, r = mbti
        if choice < 4:
            points[l] += 4 - choice
        else:
            points[r] += choice - 4
    ans = ''
    for pset in ["RT", "CF", "JM", "AN"]:
        l, r = pset
        if points[l] >= points[r]:
            ans += l
        else:
            ans += r
    return ans

inputdatas = [
    {"data": [["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]], "answer": "TCMA"},
    {"data": [["TR", "RT", "TR"], [7, 1, 3]], "answer": "RCJA"}
]

"""
2022 카카오 테크 인턴십 기출. Lv.1. 옮겨적기부터 채점까지 18분 걸렸다.
지표번호를 읽고 입력데이터를 보니 성격유형이 매 테케에 따로 주어지는 줄 알고
지표번호를 찾기 위해 한참 시간을 낭비했다. 그 외에는 어려울 것 없는 문제.

2차 시도. 12분 걸렸다. JM을 미리 정렬하지 않고 min을 사용했다.
setdefault, get, zip을 사용해 몇 줄 짧아졌다.

3차 시도. 
포인트를 if문이 아니라 계산 방식으로 바꿨고 
setdefault 대신 defaultdict를 사용해
훨씬 짧아졌다.
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
