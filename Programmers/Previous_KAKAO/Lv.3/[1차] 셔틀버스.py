# https://school.programmers.co.kr/learn/courses/30/lessons/17678
def solution(n, t, m, timetable):
    def min_to_str(minit):
        return str(minit // 60).zfill(2) + ":" + str(minit % 60).zfill(2)
    st = "00:00"
    remain = []
    for i in range(n):
        ed_s = min_to_str(9 * 60 + i * t)  # 이번 버스 도착시간
        # 이번 버스 대기인원들 = 앞 차 못타고 남은 사람 + 버스 도착까지 온 대기인원
        tmp_table = remain + list(filter(lambda x: st < x <= ed_s, timetable))
        if len(tmp_table) >= m:  # 인원 다 찼으면
            tmp_table = sorted(tmp_table)  # 시간순 정렬
            remain = tmp_table[m:]  # 탑승하고 남은 사람 다음 버스로. m 딱맞으면 초기화됨.
            tmp_table = tmp_table[:m]  # 탑승한 사람
        st = ed_s  # 범위 수정
        if len(tmp_table) >= m:  # 인원 다 찼으면 마지막 인원 - 1분
            tmp_t = sorted(tmp_table)[m - 1].split(':')
            ans = min_to_str(int(tmp_t[0]) * 60 + int(tmp_t[1]) - 1)
        else:  # 인원 다 못채웠으면 최대한 늦게 버스 도착시간
            ans = ed_s
    return ans

inputdatas = [
    [1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]],
    [2, 10, 2, ["09:10", "09:09", "08:00"]],
    [2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]],
    [1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]],
    [1, 1, 1, ["23:59"]],
    [10, 60, 45, ["23:59", "23:59", "23:59",
                  "23:59", "23:59", "23:59",
                  "23:59", "23:59", "23:59",
                  "23:59", "23:59", "23:59",
                  "23:59", "23:59", "23:59",
                  "23:59"]],
    [1, 1, 1, ["09:00", "09:10", "09:10", "09:10", "09:12", "09:12", "09:12"]],
    [3, 1, 2, ["06:00", "23:59", "05:48", "00:01", "00:01"]]
]

"""
2018 카카오 공채 기출. 1시간 걸려서 95.8점 만들었다. 마지막 예외를 찾지 못하여 풀이를 찾아봤다.
과정은 조금 다르지만 핵심 알고리즘은 내 풀이와 똑같았다. 
디버깅해보니 내 풀이에서 첫 if len(tmp_table) >= m: 부분에서 '='이 빠져서
remain의 인원이 모두 탑승한 후에도 remain이 그대로 유지되어 문제가 생긴 것이었다.
베스트 풀이도 찾아봤으나 내 풀이가 더 직관적으로 느껴져서 연습해보진 않았다.
매번 timetable에서 filter하는데, timetable을 처음에 정렬 후 이미 탑승한 인원들을 timetable에서 제거(없는 인원들 제외하고 인덱싱 이용해서 timetable에 새로 할당)하면 시간이 좀 줄어들지 않을까 싶다. 내 풀이의 시간이 느리지 않았고, 시간 효율성이 있는 문제가 아니라서 그냥 넘어갔다.
"""

# 풀이 찾아본 후 연습해본 풀이
def solution2(n, t, m, timetable):
    # 9시부터 n회 t분 간격.
    # 모든 크루는 23:59에 집에 돌아감.
    # 크루 도착 시각 리스트
    people = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    nop = len(people)
    people.sort()
    bustimes = [9 * 60 + i * t for i in range(n)]
    cnt_person = 0
    for bustime in bustimes:
        acc = 0
        # 버스 정원 안채워졌고 전체인원수 초과 안했고 현재 인원이 버스 탈 수 있으면
        while acc < m and cnt_person < nop and people[cnt_person] <= bustime:
            acc += 1  # 탑승시키고
            cnt_person += 1  # 다음 인원 체크
        if acc < m:  # 인원 다 못채웠으면 최대한 늦게 버스 도착시간
            ans = bustime
        else:  # 인원 다 찼으면 마지막 인원 - 1분
            ans = people[cnt_person - 1] - 1
    return str(ans // 60).zfill(2) + ":" + str(ans % 60).zfill(2)

for t in inputdatas:
    print(solution(t[0], t[1], t[2], t[3]))
