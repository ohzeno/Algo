# https://school.programmers.co.kr/learn/courses/30/lessons/92334
"""
constraints:
  • 2 ≤ id_list의 길이 ≤ 1,000
    ◦ 1 ≤ id_list의 원소 길이 ≤ 10
    ◦ id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
    ◦ id_list에는 같은 아이디가 중복해서 들어있지 않습니다.
  • 1 ≤ report의 길이 ≤ 200,000
    ◦ 3 ≤ report의 원소 길이 ≤ 21
    ◦ report의 원소는 "이용자id 신고한id"형태의 문자열입니다.
    ◦ 예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
    ◦ id는 알파벳 소문자로만 이루어져 있습니다.
    ◦ 이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
    ◦ 자기 자신을 신고하는 경우는 없습니다.
  • 1 ≤ k ≤ 200, k는 자연수입니다.
  • return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.
"""


def solution(id_list, report, k):
    user_d = {
        user: {
            'mailed': 0, 'reported_by': []
        } for user in id_list
    }
    for r in set(report):
        reporter, reported = r.split()
        user_d[reported]['reported_by'].append(reporter)
    for user in user_d.values():
        if len(user['reported_by']) >= k:
            for reporter in user['reported_by']:
                user_d[reporter]['mailed'] += 1
    return [user['mailed'] for user in user_d.values()]

inputdatas = [
    {"data": [["muzi", "frodo", "apeach", "neo"],
              ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2], "answer": [2, 1, 1, 0]},
    {"data": [["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3], "answer": [0, 0]}
]

"""
2022 KAKAO BLIND RECRUITMENT
Lv.1. 현 시점 완료한 사람 34,278명, 정답률 39%
예전에 풀었을 때와 비교하면 answer배열을 사용하지 않고 set을 이용해 중복신고를 제거했다.
딕셔너리 삽입 순서를 이용하는게 불쾌하면 id_list를 순회하면서 key로 사용해도 된다.
이 문제 나온지가 언젠데 아직도 정답률이 39%밖에 안된다는게 신기하다.
베스트 풀이는 여전히 report를 두번 순회하는데, 
report의 길이를 생각하면 상당히 비효율적이다.
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
