# https://school.programmers.co.kr/learn/courses/30/lessons/42888
"""
constraints:
  • record는 다음과 같은 문자열이 담긴 배열이며, 길이는 1 이상 100,000 이하이다.
  • 다음은 record에 담긴 문자열에 대한 설명이다.
    ◦ 모든 유저는 [유저 아이디]로 구분한다.
    ◦ [유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - "Enter [유저 아이디] [닉네임]" (ex. "Enter uid1234 Muzi")
    ◦ [유저 아이디] 사용자가 채팅방에서 퇴장 - "Leave [유저 아이디]" (ex. "Leave uid1234")
    ◦ [유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - "Change [유저 아이디] [닉네임]" (ex. "Change uid1234 Muzi")
    ◦ 첫 단어는 Enter, Leave, Change 중 하나이다.
    ◦ 각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
    ◦ 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
    ◦ 유저 아이디와 닉네임의 길이는 1 이상 10 이하이다.
    ◦ 채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.
"""


def solution(record):
    nick = {}
    message = []

    def logging(uid, order):
        action = "들어왔습니다" if order == "Enter" else "나갔습니다"
        return f"{nick[uid]}님이 {action}."

    for rec in record:
        order, uid, *nickname = rec.split()
        if nickname:
            nick[uid] = nickname[0]
        if order != "Change":
            message.append((uid, order))
    return [logging(uid, order) for uid, order in message]


inputdatas = [
    {"data": [
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]],
     "answer": ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]}
]

"""
2019 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 33,270명, 정답률 58%
이전엔 31분 걸렸었고, 당시 풀이는 35줄이었는데, 
이번에는 15분 걸리고 13줄이 됐다.
당시 풀이는 로그를 실시간으로 생성하고, 
변경 이벤트시에 uid별 메시지를 순회하면서 갱신하는 방식이었다.
당시에는 그게 개발적인 풀이고, 
uid별 닉네임을 다 변경한 후에 최종 닉네임으로 로그를 생성하는 
지금의 풀이는 문제용이라고 적었었다.
지금 생각해도 지금 방식은 전체 메시지를 일괄로 만드는거라 
이벤트마다 진행하기에는 불필요한 연산이 너무 많다.
이전 방식은 Change 이벤트가 uid별 메시지를 모두 처리하니 채팅이 쌓일 수록 문제가 
생길 수 있는데, 최근 메시지만을 실시간 처리하고 나머지는 요청 시에 업데이트 하는게 나을 것 같다.
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
