# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    """
    0과 1로 이루어진 문자열 x에 대한 이진변환
    1. x의 모든 0을 제거
    2. x의 길이가 c이면 x를 "c를 2진법으로 표현한 문자열"로 변환
    ex) x = "0111010" -> "1111" -> "100"
    s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때,
    이진 변환의 횟수, 제거된 모든 0의 개수를 각각 배열에 담아 return
    1 <= len(s) <= 150_000
    s에는 '1'이 최소 하나 이상 포함
    """
    convert = zero = 0
    while s != "1":
        zero += s.count("0")
        s = bin(s.count("1"))[2:]
        convert += 1
    return [convert, zero]

inputdatas = [
    "110010101001",
    "01110",
    "1111111"
]

"""
월간 코드 챌린지 시즌1 기출
현 시점 Lv.2, 완료한 사람 18082명, 정답률 76%
파이썬 내장함수 쓰면 쉽게 풀리는 문제.
문제 읽고 제출까지 5분도 안걸렸다.
"""

for t in inputdatas:
    print(solution(t))
