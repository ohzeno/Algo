# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(ss):
    num_dic = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    new_s = ''  # 리턴할 문자열
    tmp = ''  # 단어 저장할 문자열
    for s in ss:
        if s.isdigit():  # 숫자면 그대로 정답에 추가
            new_s += s
        else:
            tmp += s  # 알파벳이면 일단 단어에 추가하고
            if tmp in num_dic:  # 단어가 완성됐으면
                # (숫자쪽에서 확인하면 영단어 + 영단어 경계를 건너뛰게 된다.)
                new_s += str(num_dic[tmp])  # 정답에 추가하고
                tmp = ''  # 임시 문자열 초기화.
    return int(new_s)  # 정답은 숫자로 출력

inputdatas = [
    'one4seveneight',
    '23four5six7',
    '2three45sixseven',
    '123'
]

"""
2021 카카오 채용연계형 인턴십 기출.
Lv.1이고 입력데이터 IDE로 옮기고 문제 읽는 것 부터 최종 제출까지 끝내니 9분 55초였다.
간단한 문제라 딱히 적을 내용이 없다. 브루트포스로 풀면 된다.
"""

for t in inputdatas:
    print(solution(t))
