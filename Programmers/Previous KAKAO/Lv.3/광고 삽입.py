# https://school.programmers.co.kr/learn/courses/30/lessons/72414
def solution(play_time, adv_time, logs):
    # play_time: 죠르디의 동영상 전체 시간
    # adv_time: 광고영상 시간
    # logs: 시청자들 재생위치
    # 누적 재생시간이 가장 큰 구간에 광고 삽입.
    # 가장 큰 구간이 여럿이면 시간순 가장 빠른 시작 시간 HH:MM:SS 형식으로 리턴.
    # logs 1~30만
    def time_to_sec(datas):  # HH:MM:SS를 sec로 변환하는 함수
        hour, minute, sec = datas.split(":")
        return int(hour) * 3600 + int(minute) * 60 + int(sec)

    def sec_to_time(datas):  # sec를 HH:MM:SS로 변환하는 함수
        hour = datas // 3600
        datas %= 3600
        minute = datas // 60
        datas %= 60
        return ':'.join([str(hour).zfill(2), str(minute).zfill(2), str(datas).zfill(2)])

    len_main, len_adv = map(time_to_sec, [play_time, adv_time])
    if len_main == len_adv:  # 죠르디 영상, 광고 영상 길이 같으면 00:00:00에 배치하는 방법 밖에 없음.
        return '00:00:00'
    len_main += 2  # dp 위해 길이 좀 여유 줌.
    time = [0] * len_main  # sec마다 시청자 수 기록될 배열
    dp = [0] * len_main  # dp[i]: i에 광고영상 배치했을 경우 총 시청시간
    for log in logs:
        st, ed = map(time_to_sec, log.split('-'))
        time[st] += 1  # 누적합
        time[ed] -= 1
    for i in range(1, len_main):
        time[i] += time[i - 1]  # 누적합 시행
    dp[0] = sum(time[:len_adv])  # 첫 위치는 sum 사용
    for i in range(1, len_main - len_adv + 1):  # 다음 위치부터는 끝부분만 빼고 더하며 기록
        dp[i] = dp[i - 1] - time[i - 1] + time[i + len_adv - 1]
    max_acc = 0
    for i in range(len_main - len_adv + 1):  # 광고영상 배치될 수 있는 마지막 시간까지만 순회
        if dp[i] > max_acc:  # 총 시청시간이 기존 기록보다 크면 갱신, 시간 기록
            max_acc = dp[i]
            ans = i
    return sec_to_time(ans)  # 가장 큰 시간 HH:MM:SS 형태로 반환

inputdatas = [
    ["02:03:55", "00:14:15", [
        "01:20:15-01:45:14",
        "00:40:31-01:00:00",
        "00:25:50-00:48:29",
        "01:30:59-01:53:29",
        "01:37:44-02:02:30",
    ]],
    ["99:59:59", "25:00:00", [
        "69:59:59-89:59:59",
        "01:00:00-21:00:00",
        "79:59:59-99:59:59",
        "11:00:00-31:00:00",
    ]],
    ["50:00:00", "50:00:00", [
        "15:36:51-38:21:49",
        "10:14:18-15:36:51",
        "38:21:49-42:51:45",
    ]],
]

"""
2021 카카오 공채 기출. Lv.3. 옮겨적기만 5분 30초 걸렸다. 
53분 걸리긴 했는데 마지막 1분은 질문들을 읽어보다 힌트를 얻었기에 온전히 내 힘으로 푼 케이스는 아니다.
이전에 '파괴되지 않은 건물'에서 사용했던 누적합을 먼저 사용해봤다.

40분쯤 초안 작성 후 실행해봤다. 예시 케이스에서 시간이 오래걸리는걸 보고 5분 정도 고민해서 로직을 수정했다.

각 기록의 시작지점, 종료 지점, 광고영상 길이가 시청기록보다 긴 케이스를 대비해 전체 영상 - 광고영상 길이.
이런 지점들을 리스트에 담아 보관하고, 그 지점들만 순회해봤다. 예시 케이스는 쉽게 통과했으나
테케 31개 중 13개만 통과하고 일부는 시간초과, 일부는 실패했다.

기록들의 종료지점은 별로 필요 없을 것 같아서 제외해봤더니 시간초과였던 2 케이스를 더 통과했다.

매번 sum을 해주는게 시간을 잡아먹는다고 생각하여 3분정도 사용하여
i지점에 광고를 삽입했을 경우의 시청 시간을 기록하는 dp배열을 만들어봤다.
시간초과는 사라졌고, 22개 케이스를 통과했지만 9개 케이스에서 실패가 발생했다.

dp를 했으니 sts만 체크하지 말고 다시 전체순회를 돌았다.
9, 31케이스 제외하면 모두 통과했다.

순회를 0부터 해보라는 말을 보고 이상해서 다시 조건을 살펴봤다.
00:00:01 이상인 것은 시청 시작 시간이 아니라, 죠르디의 동영상과 광고 영상의 길이였다.
그리고 예시 케이스 3번은 00:00:00부터 시작한다.
dp와 순회를 0부터 했더니 모두 통과했다.
"""

for t in inputdatas:
    print(solution(t[0], t[1], t[2]))
