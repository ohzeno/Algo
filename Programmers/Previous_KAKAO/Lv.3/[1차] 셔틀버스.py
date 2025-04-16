# https://school.programmers.co.kr/learn/courses/30/lessons/17678
"""
constraints:

"""


def solution(n, t, m, timetable):
    """
    셔틀은 09:00부터 n회 t분 간격으로 역에 도착
    한 셔틀 최대 m명 탑승
    도착한 순간에 대기열 선 크루(9시에 버스 도착하면 9시에 도착한 승객도 태울 수 있음)까지 포함
    콘이 셔틀 타고 사무실 갈 수 있는 정류장 도착 시각 중 제일 늦은 시각 구하라.
    콘은 같은 시각 도착한 크루 중 대기열 제일 뒤에 선다.
    모든 크루는 23:59에 집에 돌아가니 다음날 셔틀을 타는 일은 없음
    크루 도착 시각은 HH:MM은 00:01~23:59
    콘은 00:00 가능
    """

    def str_to_min(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m

    def min_to_str(min):
        h, m = divmod(min, 60)
        return f"{str(h):>02}:{str(m):>02}"

    crew_times = sorted(map(str_to_min, timetable))
    first_bus_time = 9 * 60
    last_boarded_crew_time = 0
    for i in range(n):
        cur_bus_time = first_bus_time + i * t

        # 현재 버스에 탈 수 있는 크루 수
        cur_boarded = 0

        # 현재 버스 시간까지 도착한 크루 중 탑승 가능한 크루 선별
        for crew_time in crew_times:
            if cur_boarded == m:
                break
            if crew_time <= cur_bus_time:
                last_boarded_crew_time = crew_time  # 마지막으로 탑승한 크루 시간
                cur_boarded += 1

        # 크루 목록에서 이미 탑승한 크루 제거
        crew_times = crew_times[cur_boarded:]

        # 콘이 탈 수 있는 시간 결정
        if i == n - 1:  # 마지막 버스인 경우
            if cur_boarded < m:  # 자리가 남았다면 버스 도착 시간에 탑승
                return min_to_str(cur_bus_time)
            # 자리가 없다면 마지막으로 탑승한 크루보다 1분 일찍 도착
            return min_to_str(last_boarded_crew_time - 1)


inputdatas = [
    {"data": [1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]], "answer": "09:00"},
    {"data": [2, 10, 2, ["09:10", "09:09", "08:00"]], "answer": "09:09"},
    {"data": [2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]], "answer": "08:59"},
    {"data": [1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]], "answer": "00:00"},
    {"data": [1, 1, 1, ["23:59"]], "answer": "09:00"},
    {"data": [10, 60, 45,
              ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
               "23:59", "23:59", "23:59", "23:59", "23:59"]], "answer": "18:00"},
    {"data": [1, 1, 1, ["09:00", "09:10", "09:10", "09:10", "09:12", "09:12", "09:12"]], "answer": "08:59"},
    {"data": [3, 1, 2, ["06:00", "23:59", "05:48", "00:01", "00:01"]], "answer": "09:02"},
]

"""
2018 KAKAO BLIND RECRUITMENT
Lv.3. 현 시점 완료한 사람 7,517명, 정답률 44%
1시간 걸려서 95.8점 만들었다. 마지막 예외를 찾지 못하여 풀이를 찾아봤다.
과정은 조금 다르지만 핵심 알고리즘은 내 풀이와 똑같았다. 
디버깅해보니 내 풀이에서 첫 if len(tmp_table) >= m: 부분에서 '='이 빠져서
remain의 인원이 모두 탑승한 후에도 remain이 그대로 유지되어 문제가 생긴 것이었다.
베스트 풀이도 찾아봤으나 내 풀이가 더 직관적으로 느껴져서 연습해보진 않았다.
매번 timetable에서 filter하는데, timetable을 처음에 정렬 후 이미 탑승한 인원들을 timetable에서 제거(없는 인원들 제외하고 인덱싱 이용해서 timetable에 새로 할당)하면 시간이 좀 줄어들지 않을까 싶다. 내 풀이의 시간이 느리지 않았고, 시간 효율성이 있는 문제가 아니라서 그냥 넘어갔다.

2회차. 1시간 이상 걸렸다. 베스트 풀이는 여전히 직관적이지 않다.
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
