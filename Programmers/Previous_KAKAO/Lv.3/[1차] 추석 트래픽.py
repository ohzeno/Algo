# https://school.programmers.co.kr/learn/courses/30/lessons/17676?language=python3
"""
constraints:

"""


def solution(lines):
    """
    초당 최대 처리량 리턴
    요청 응답 여부와 무관하게 임의 시간부터 1초간 처리하는 요청의 최대 갯수.
    lines는 최대 길이 2000. 로그 문자열 들어있음
    각 로그 문자열마다
    응답 완료시간 S와
    처리시간 T가 공백으로 구분됨
    응답 완료시간 S는 2016년 9월 15일만 포함. 2016-09-15 hh:mm:ss.sss 형식
    처리시간 T는 0.1s, 0.312s, 2s와 같이 최대 소수점 셋째 자리까지 기록.
    처리 시간은 시작과 끝을 포함한다.
    타임아웃이 3초라 0.001 <= T <= 3.000
    lines 배열은 S를 기준으로 오름차순.
    """
    events = []
    for line in lines:
        _, respone_ed, duration = line.split()
        h, m, s = respone_ed.split(':')
        respone_ed = (int(h) * 3600 + int(m) * 60 + float(s)) * 1000
        duration = float(duration[:-1]) * 1000
        events.append((respone_ed - duration + 1, 1))
        events.append((respone_ed + 1000, -1))
    events.sort()
    max_process = 0
    cur_process = 0
    for time, event_type in events:
        cur_process += event_type
        max_process = max(max_process, cur_process)
    return max_process


inputdatas = [
    {
        "data": [[
            "2016-09-15 01:00:04.001 2.0s",
            "2016-09-15 01:00:07.000 2s"
        ]],
        "answer": 1
    },
    {
        "data": [[
            "2016-09-15 01:00:04.002 2.0s",
            "2016-09-15 01:00:07.000 2s"
        ]],
        "answer": 2},
    {
        "data": [[
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s"
        ]],
        "answer": 7}
]

"""
2018 KAKAO BLIND RECRUITMENT
Lv.3. 현 시점 완료한 사람 8,020명, 정답률 22%
기본적인 스위핑 알고리즘. 
스위핑을 너무 오랜만에 풀어봐서 스위핑 알고리즘 작성에 시간이 좀 걸렸다.
처음엔 그냥 2중 for문으로 해결했다.
역시나 다른 사람 풀이는 추천 많이 받은 풀이도 깔끔한게 없다.
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
