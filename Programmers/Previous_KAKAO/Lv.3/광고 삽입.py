# https://school.programmers.co.kr/learn/courses/30/lessons/72414
"""
constraints:

"""


def solution(play_time, adv_time, logs):
    """
    죠르디 영상에서 시청자들의 누적 재생 시간이 가장 큰 구간에 광고 삽입
    광고 시작 시각 리턴.
    조건 만족 구간 많으면 가장 빠른 시각 리턴
    play_time: 죠르디 영상 길이
    adv_time: 광고 영상 길이
    logs: 시청자들 재생 위치
    HH:MM:SS 형식
    """
    if play_time == adv_time:
        return "00:00:00"

    def time_to_sec(time_str):
        h, m, s = map(int, time_str.split(":"))
        return h * 3600 + m * 60 + s

    def sec_to_time(sec):
        h, sec = divmod(sec, 3600)
        m, sec = divmod(sec, 60)
        return f"{h:02d}:{m:02d}:{sec:02d}"

    play_time, adv_time = map(time_to_sec, [play_time, adv_time])
    viewers = [0] * (play_time + 1)
    for log in logs:
        st, ed = map(time_to_sec, log.split("-"))
        viewers[st] += 1
        viewers[ed] -= 1
    for i in range(1, play_time + 1):  # 누적합 하면 각 시각 시청자수 됨
        viewers[i] = viewers[i - 1] + viewers[i]
    time_acc = [0] * (play_time + 1)
    time_acc[0] = viewers[0]
    for i in range(1, play_time + 1):
        time_acc[i] = time_acc[i - 1] + viewers[i]
    max_acc_time = time_acc[adv_time]  # 첫 위치는 [i-1]을 뺄 수 없으니 1부터 순회
    ans_time = 0
    for i in range(1, play_time - adv_time + 1):
        # i + adv -1 <= play_time - 1
        # i <= play_time - adv
        # i < play_time - adv + 1
        # i부터 adv_time 영상 배치하면 adv-1까지 재생됨.
        # 0초에 3초 광고 배치하면 0, 1, 2 3초.
        # 4~6 3초 시간 확인하려면 6초 누적에서 3초 누적 빼야함.
        # time_acc[i]는 i.999초까지의 누적임. 2에선 2.999 즉, 3초짜리 누적.
        acc_time = time_acc[i + adv_time - 1] - time_acc[i - 1]
        if acc_time > max_acc_time:
            max_acc_time = acc_time
            ans_time = i
    return sec_to_time(ans_time)


inputdatas = [
    {"data": ["02:03:55", "00:14:15",
              ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
               "01:37:44-02:02:30"]], "answer": "01:30:59"},
    {"data": ["99:59:59", "25:00:00",
              ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]],
     "answer": "01:00:00"},
    {"data": ["50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]],
     "answer": "00:00:00"}
]

"""
2021 KAKAO BLIND RECRUITMENT
Lv.3. 현 시점 완료한 사람 4,677명, 정답률 35%
옮겨적기만 5분 30초 걸렸다. 
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

2회차. 스위핑과 슬라이딩 윈도우로 풀려다 실패, 내 풀이 누적합 아이디어 다시 보고 풀었다.
그래도 오래걸렸다. 인덱스의 정의를 처리하기가 까다롭다.
0초면 0초 이상 1초 미만의 값을 누적하게 된다거나.
누적합 아이디어 자체도 생각 안난거 보니 너무 오랫동안 알고리즘을 안푼 듯 하다.
"""

for t in inputdatas:
    print(solution(t[0], t[1], t[2]))
