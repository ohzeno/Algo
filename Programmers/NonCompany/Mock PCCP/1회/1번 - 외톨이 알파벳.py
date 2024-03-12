# https://school.programmers.co.kr/learn/courses/15008/lessons/121683
"""
알파벳 소문자로만 이루어진 문자열에서 2회 이상 나타난 알파벳이
2개 이상의 부분으로 나뉘어 있으면 외톨이 알파벳의라 정의한다.
문자열이 주어지면 외톨이 알파벳들을 알파벳순으로 이어붙인 문자열을 리턴하라.
외톨이 알파벳이 없다면 N을 리턴하라.
input_string은 소문자로만 구성되어 있고 1자 이상 2600자 이하다.
"""
def solution(input_string):
    loners = set()
    logs = {}
    for i, c in enumerate(input_string):
        if c in loners:
            continue
        if c in logs and logs[c] + 1 != i:
            loners.add(c)
            continue
        logs[c] = i
    if not loners:
        return 'N'
    return ''.join(sorted(loners))

inputdatas = [
    ["edeaaabbccd", "de"],
    ['eeddee', "e"],
    ['string', 'N'],
    ['zbzbz', 'bz'],
]

"""
PCCP 모의고사 1회 1번
5분만에 풀고 더 좋은 풀이가 있나 찾아봤는데 없었다.
전체적으로 내 풀이보다 한참 긴 것들이 대부분이고, 짧거나 비슷한 경우에는 로직이 조금씩 달랐다.
다른 로직들은 딕셔너리 대신 prev나 알파벳 수 만큼의 배열을 사용하거나 
for 대신 while을 사용하거나 정도.
"""

# for t in inputdatas:
#     print(solution(*t))
for data, ans in inputdatas:
    res = solution(data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")