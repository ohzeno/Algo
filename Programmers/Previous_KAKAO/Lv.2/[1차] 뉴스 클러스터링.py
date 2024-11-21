# https://school.programmers.co.kr/learn/courses/30/lessons/17677
"""
constraints:

"""


def solution(str1, str2):
    def str2d(s):
        d = {}
        for i in range(len(s) - 1):
            part = s[i:i+2].lower()
            if part.isalpha():
                d[part] = d.get(part, 0) + 1
        return d
    d1, d2 = str2d(str1), str2d(str2)
    set1, set2 = set(d1), set(d2)
    inter_cnt = sum(min(d1[part], d2[part]) for part in set1 & set2)
    union_cnt = sum(max(d1.get(part, 0), d2.get(part, 0)) for part in set1 | set2)
    return int(inter_cnt / union_cnt * 65536) if union_cnt else 65536


inputdatas = [
    {"data": ["FRANCE", "french"], "answer": 16384},
    {"data": ["handshake", "shake hands"], "answer": 65536},
    {"data": ["aa1+aa2", "AAAA12"], "answer": 43690},
    {"data": ["E=M*C^2", "e=m*c^2"], "answer": 65536}
]


"""
2018 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 19,842명, 정답률 62%
이전엔 1차 35분, 2차 25분 걸렸었는데 이번엔 15분 걸렸다.
풀고 나서 풀이를 좀 간결하게 바꿨다.
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
