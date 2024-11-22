# https://school.programmers.co.kr/learn/courses/30/lessons/17683
"""
constraints:

"""


def solution(m, musicinfos):
    # 조건 일치하는 음악이 여럿이면 (-재생 시간, 입력된 순서)로 정렬해서 첫 음악 제목 반환
    def remove_sharp(melody):
        for i in range(ord('A'), ord('G')+1):
            melody = melody.replace(chr(i)+'#', chr(i).lower())
        return melody

    def time_to_min(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m

    def get_on_air_melody(on_air_time, melody):
        return (melody * (on_air_time // len(melody) + 1))[:on_air_time]

    m = remove_sharp(m)
    matches = []
    for idx, musicinfo in enumerate(musicinfos):
        st, ed, title, melody = musicinfo.split(',')
        st, ed = map(time_to_min, (st, ed))
        on_air_time = ed - st
        if on_air_time == 0:
            continue
        melody = remove_sharp(melody)
        on_air_melody = get_on_air_melody(on_air_time, melody)
        if m in on_air_melody:
            matches.append((-on_air_time, idx, title))
    matches.sort()
    return matches[0][2] if matches else "(None)"



inputdatas = [
    {"data": ["ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]], "answer": "HELLO"},
    {"data": ["CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]], "answer": "FOO"},
    {"data": ["ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]], "answer": "WORLD"}
]


"""
2018 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 9,758명, 정답률 49%
예전에 풀었을 때와 달리 B#이 추가됐는데, 문제 지문에는 적혀있지 않다.
이번엔 replace 체이닝하지 않고 ord, chr을 이용해 대체해줬다.
사실 for문 내에서 이전 답보다 on_air_time이 긴 음악으로 정답을 대체하기만 하면
정렬은 필요 없다. 하지만 문제 조건을 보면 정렬이 직관적이라서 정렬을 사용했다.
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
