# https://school.programmers.co.kr/learn/courses/30/lessons/84512
"""
constraints:
  • word의 길이는 1 이상 5 이하입니다.
  • word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
"""
from itertools import product

def solution(target):
    vowels = 'AEIOU'
    dictionary = []
    for i in range(1, 6):
        for case in product(vowels, repeat=i):
            dictionary.append("".join(case))
    dictionary.sort()
    return dictionary.index(target) + 1


inputdatas = [
    {"data": ["AAAAE"], "answer": 6},
    {"data": ["AAAE"], "answer": 10},
    {"data": ["I"], "answer": 1563},
    {"data": ["EIO"], "answer": 1189}
]


"""
완전탐색
Lv.2. 현 시점 완료한 사람 25,052명, 정답률 63%
정렬 로직이 적혀있지 않다. 굉장히 불친절한 문제.
sort로 해결되긴 하지만 지문이 '예시 읽고 규칙 찾아라'같은 느낌이다.
코테에서 만났으면 건너뛰었을 것 같다.
예시가 부족한데 정렬 규칙을 찾아야 해서 lv.2에 있을 문제는 아닌듯.
n-1글자의 하위트리가 n글자를 AEIOU순으로 추가하는 식이다.
자신 이전까지의 서브트리 노드 수를 구해서 일반항을 만들어 계산할 수도 있고
dfs로 탐색할 수도 있다.
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
