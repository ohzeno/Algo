# https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""
constraints:

"""


def solution(s):
    """
    문자열을 n개 단위로 잘라서 반복 표시
    aabbaccc -> 2a2ba3c
    ababcdcdababcdcd -> 2ababcdcd (8단위)
    가장 짧은 압축 문자열 길이 리턴.
    """
    len_s = len(s)
    min_len = len_s
    for unit in range(1, len_s // 2 + 1):
        compressed = ""
        pre = s[:unit]
        count = 1
        for i in range(unit, len_s - unit + 1, unit):
            cur = s[i:i + unit]
            if pre == cur:
                count += 1
            else:
                compressed += f'{count}{pre}' if count > 1 else pre
                pre = cur
                count = 1
        compressed += f'{count}{pre}' if count > 1 else pre
        compressed += s[i + unit:]
        min_len = min(min_len, len(compressed))
    return min_len


inputdatas = [
    {"data": ["aabbaccc"], "answer": 7},
    {"data": ["ababcdcdababcdcd"], "answer": 9},
    {"data": ["abcabcdede"], "answer": 8},
    {"data": ["abcabcabcabcdededededede"], "answer": 14},
    {"data": ["xababcdcdababcdcd"], "answer": 17},
    {"data": ["aababa"], "answer": 5},
    {"data": ["xxxxxxxxxxyyy"], "answer": 5},
    {"data": ["aaaaaaaaaabbbbbbbbbb"], "answer": 6},
    {"data": ["aaaaa"], "answer": 2},
    {"data": ["aaaaaaaaaa"], "answer": 3},
    {"data": ["werwerwsdgsdfsdfsdf"], "answer": 15},
    {"data": ["xababcdcdababcdcd"], "answer": 17},
]

"""
2020 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 31,525명, 정답률 44%
43분 첫 제출. 52점.
조건에 '제일 앞부터 정해진 길이만큼 잘라야 한다'가 없지만, 입출력 예시 5번에서 해당 조건을 언급한다.
47분 개선 후 제출. 60점.
'제일 앞부터 정해진 길이만큼 잘라야 한다'가 단축된 부분 제외하고도 길이단위로 슬라이딩 하며 살펴야 한다.
abab acd efef라면 중간 acd가 3이라 단축X 2ab ac de fe f로 살펴야한다.
51분 개선 후 제출. 82점.
aa bc bc라면 aa2bc가 되어야 하는데, 첫 aa가 단축이 불가하면 검사를 중단했었다.
67분 개선 후 제출. 통과.

조건 설명이 부족하여 이해가 힘든 문제였다. 
lv.2지만 문제 이해 못하면 이 문제에 1시간 이상 쓰고 결국 못풀고 코테 망할듯.
나는 혹시 모를 시간초과를 고려하여 index를 사용하여 문자열에 접근하며 실시간으로 문자열을 갱신했다.
다른 풀이들을 보니 매 unit마다 unit단위로 단어를 분할한 리스트를 순회하며 작업했다.
분할해놓으면 디버깅이 편하다는 것 외에 딱히 장점이 없을 듯 하여 풀이를 시도해보진 않았다.

2회차. 11분. 과거와 달리 unit단위로 분할했고, 이번엔 조건을 오해하지 않고 문제의 의도대로 이해했다.
덕분에 코드도 훨씬 간결해졌다.
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
