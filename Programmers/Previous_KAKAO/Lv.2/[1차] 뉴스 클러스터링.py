# https://school.programmers.co.kr/learn/courses/30/lessons/17677
"""
constraints:

"""


def solution(str1, str2):
    """
    J(A, B) = |A ∩ B| / |A ∪ B|
    둘 다 공집합이면 1
    중복 허용하는 다중집합에서도 가능.
    A가 1 3개, B가 5개 갖고있으면
    |A ∩ B|가 갖는 1은 min(3, 5) = 3
    |A ∪ B|가 갖는 1은 max(3, 5) = 5
    각 문자열은 2~1000자
    두 글자씩 끊어서 다중집합 원소로. ex) FRANCE -> [FR, RA, AN, NC, CE]
    영문자만 유효. 공백 숫자 특수문자 버림. ex) ab+ -> [ab]
    자카드 유사도에 65536 곱하고 소수점 아래 버리고 출력.
    """
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
Lv.2. 현 시점 완료한 사람 20,987명, 정답률 63%
이전엔 1차 35분, 2차 25분 걸렸었는데 이번엔 15분 걸렸다.
풀고 나서 풀이를 좀 간결하게 바꿨다.
4차 8분. 코드 달라진 건 거의 없다.
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
