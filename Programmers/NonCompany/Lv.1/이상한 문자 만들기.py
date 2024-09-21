# https://school.programmers.co.kr/learn/courses/30/lessons/12930
"""
문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로,
홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수,
solution을 완성하세요.
"""


def split(s, sep):
    """
    s.split(sep)의 동작을 구현한 함수
    """
    words = []
    word = ""
    for c in s:
        if c == sep:
            words.append(word)
            word = ""
        else:
            word += c
    words.append(word)
    return words


def solution(s):
    # words = split(s, ' ')
    # 공백이 연속되면 그 사이에 빈 문자열이 있는 것으로 취급.
    # 양 끝이 공백이면 거기도 빈 문자열이 있는 것으로 취급.
    # 덕분에 공백 갯수를 직접 처리할 필요 없다.
    words = s.split(" ")
    result = []
    for word in words:  # 빈 문자열은 대소문자 변환 대상이 아니라서 따로 처리 안해도 된다.
        new_word = ""
        for i, c in enumerate(word):
            if i % 2 == 0:
                new_word += c.upper()
            else:
                new_word += c.lower()
        result.append(new_word)
    return " ".join(result)


inputdatas = [
    {"data": ["try hello world"], "answer": "TrY HeLlO WoRlD"},
    {"data": ["  abc de   fghi   "], "answer": "  AbC De   FgHi   "},
]

"""
연습문제
Lv.1. 현 시점 완료한 사람 43,286명, 정답률 75%
정답률이랑 레벨 보고 1분안에 풀겠다 싶었고, split()써서 풀었는데
문제가 개편되면서 오답이 됐다. 옛날에 푼 사람들 때문에 75%인듯.
while로 공백 찾아서 처리해서 통과했고
split(' ')를 써서 간략화했다.
split의 구분자 처리 방식을 처음 알았고, 좀 덜 직관적이라 직접 함수로 구현해봤다.
정답률 높은 Lv.1로 공부하게 될 줄은 몰랐다.
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
            summary += f"    {content}\n"
            summary = summary.rstrip()
        print(summary)
