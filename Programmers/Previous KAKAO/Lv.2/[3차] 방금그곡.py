# https://school.programmers.co.kr/learn/courses/30/lessons/17683
def solution(m, musicinfos):
    # 네오가 기억한 멜로디, 악보에 사용되는 음은
    # C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개다.
    # 각 음은 1분에 1개씩 재생됨. 음악은 반드시 처음부터 재생.
    # 음악 길이보다 재생시간이 길면 끊김없이 반복재생.
    # 음악 길이보다 재생시간이 짧으면 끊김.
    # 음악이 00:00 넘겨서까지 재생되진 않음.
    # m: 네오가 기억한 멜로디. 1~1439 길이
    # musicinfos는 100개 이하 곡 정보.
    # 시작 시각, 종료 시각, 음악 제목, 악보 정보가 ','로 구분되어 들어있음.
    # 시각: 24시간 HH:MM 형식. 제목은 ',' 이외 문자 1~64 길이 문자열.
    # 악보 정보는 1~1439 길이
    def time_to_min(datas):
        hour, minute = datas.split(':')
        return int(hour) * 60 + int(minute)
    def remove_sharp(datas):  # '#' 처리
        datas = datas.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        return datas
    m = remove_sharp(m)
    logs = []
    for order, music in enumerate(musicinfos):
        st, ed, title, score = music.split(',')
        score = remove_sharp(score)
        len_music = len(score)
        tmp_st, tmp_ed = map(time_to_min, (st, ed))
        if tmp_ed < tmp_st:  # 종료 시각이 00:00이면
            tmp_ed = time_to_min('24:00')
        elif tmp_ed == tmp_st:  # 방송 시간이 0이면 체크X
            continue
        on_air_time = tmp_ed - tmp_st
        if on_air_time < len_music:  # 방송 시간이 곡 길이보다 짧으면 끊기
            # 방송시간을 마이너스로 넣어서 sort()하면 방송시간 긴 순, 들어간 순서로 정렬됨.
            logs.append([-on_air_time, order, title, score[:on_air_time]])
        else:  # 방송 시간이 곡 길이보다 길면 반복재생
            tmp_score = score * (on_air_time // len_music + 1)
            logs.append([-on_air_time, order, title, tmp_score[:on_air_time]])
    involve = []
    for datas in logs:
        if m in datas[3]:  # 들은 멜로디가 포함되면 involve에 넣기
            involve.append(datas)
    # 조건이 일치하는 음악이 없을 때는 "(None)"를 반환
    if not involve:
        return "(None)"
    else:
        # 조건이 일치하는 음악이 여럿이면 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환.
        # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환.
        if len(involve) > 1:
            involve.sort()
        return involve[0][2]


inputdatas = [
    ["ABCDEFG",
     ["12:00,12:14,HELLO,CDEFGAB",
      "13:00,13:05,WORLD,ABCDEF"]],
    ["CC#BCC#BCC#BCC#B",
     ["03:00,03:30,FOO,CC#B",
      "04:00,04:08,BAR,CC#BCC#BCC#B"]],
    ["ABC",
     ["12:00,12:14,HELLO,C#DEFGAB",
      "13:00,13:05,WORLD,ABCDEF"]],
]

"""
2018 카카오 공채 기출. Lv.2. 
옮겨적기, 읽기에만 9분 20초 걸렸다.
30분에 초안을 제출했는데 테케 30번에 실패했다. 조건에서 '00:00'를 넘기는 경우는 없다. 라는 말을 보고
종료시각이 00:00인 경우를 가정해서 다시 제출했으나 또 틀렸다.
한참을 고생했다. 테케 30번의 m은 'DED'이다.
나는 기존에 악보를 처리할 때 #을 없애지 않았다. #을 앞으로 빼서 'D_E'가 'D_E#'에 포함될 여지를 없앴다.
하지만 '#D_E'에 포함되어 오류가 생겼다. #을 처리해줘 통과했다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
