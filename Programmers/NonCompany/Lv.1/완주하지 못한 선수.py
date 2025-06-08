# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
"""
constraints:
  • 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
  • completion의 길이는 participant의 길이보다 1 작습니다.
  • 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
  • 참가자 중에는 동명이인이 있을 수 있습니다.
"""
from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    for name in p:
        if c.get(name, 0) != p[name]:
            return name



inputdatas = [
    {"data": [["leo", "kiki", "eden"], ["eden", "kiki"]], "answer": "leo"},
    {"data": [["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]], "answer": "vinko"},
    {"data": [["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]], "answer": "mislav"}
]


"""
해시
Lv.1. 현 시점 완료한 사람 104,687명, 정답률 58%
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
