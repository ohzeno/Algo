# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    # 1~n으로 분류되는 개인정보.
    # 약관마다 개인정보 보관 유효기간.
    # 각 정보가 어떤 약관으로 수집됐는지 알고있음.
    # 유효기간 전까지만 보관 가능. 지나면 파기.
    # 2021.01.05에 수집됐고 유효기간 12개월이면 2022.01.04까지 보관. 2022.01.05에 파기.
    # 모든 달은 28일까지 있다고 가정.
    # today: 오늘.  terms: 유효기간들.  privacies: 개인정보 수집된 날짜(today 이전만 주어짐), 약관
    # 오늘 파기해야할 개인정보 번호를 오름차순으로 배열에 담아 리턴.
    # terms 길이 1~20. 약관 종류는 A~Z. 중복없음. 유효기간은 1~100이며 단위는 '달'
    # privacies 길이 1~100. privacies[i]는 i+1번 개인정보의 수집 일자, 약관 종류
    # YYYY는 2000~2022, MM은 1~12, DD는 1~28
    # 파기해야 할 개인정보가 하나 이상 존재하는 입력만 주어짐.
    def str2day(data):
        y, m, d = data.split('.')
        return int(d) + int(m) * 28 + int(y) * 28 * 12
    today = str2day(today)
    inday = {}
    for term in terms:
        type, month = term.split()
        inday[type] = today - int(month) * 28 + 1  # 1을 더해줘야 보관 마지노선이 된다.
    answer = []
    for idx, privacy in enumerate(privacies, 1):
        date, type = privacy.split()
        if str2day(date) < inday[type]:  # 등록일자가 보관 마지노선보다 이르면 파기
            answer.append(idx)
    return answer

inputdatas = [
    ["2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]],
    ["2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]],
]

"""
2023 카카오 공채 기출. Lv.1 현 시점 제출 382, 정답률 24%
옮겨적기부터 제출까지 22분 걸렸다.
str2day, day2str 함수를 다 작성했었는데, 후자는 필요없었다.
공채 당시 풀이를 다시 살펴봤는데, 확실히 지금보다 풀이가 더러웠다.
몇 개월 지나지도 않았는데 그 사이 실력이 많이 는 것이 느껴진다.
"""

for t in inputdatas:
    print(solution(t[0], t[1], t[2]))
