# https://school.programmers.co.kr/learn/courses/30/lessons/60058
"""
constraints:

"""


def solution(p):
    def split_uv(s):
        o = c = 0
        for i, char in enumerate(s):
            if char == "(":
                o += 1
            else:
                c += 1
            if o == c:
                return s[:i + 1], s[i + 1:]
    def is_correct(s):
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if not stack:
                    return False
                stack.pop()
        return True
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p:
        return ""
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    #     단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
    #     v는 빈 문자열이 될 수 있습니다.
    u, v = split_uv(p)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if is_correct(u):
        return u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    #   4-3. ')'를 다시 붙입니다.
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    #   4-5. 생성된 문자열을 반환합니다.
    s = '(' + solution(v) + ')'
    for i in u[1:-1]:
        if i == '(':
            s += ')'
        else:
            s += '('
    return s



inputdatas = [
    {"data": ["(()())()"], "answer": "(()())()"},
    {"data": [")("], "answer": "()"},
    {"data": ["()))((()"], "answer": "()(())()"}
]

"""
2020 KAKAO BLIND RECRUITMENT
Lv.2. 현 시점 완료한 사람 20,257명, 정답률 48%
옮겨적기부터 채점까지 36분 45초가량 걸렸다.
규칙 설명의 문장들이 주술관계가 명확하지 않거나 중의적인 문장이 많아 이해하기 힘들어서 좀 헤맸다.
주석으로 적은 내용은 예시를 보며 이해한 후,
본래 규칙에서 생략된 목적어와 부사를 추가하고 주어가 모호한 문장을 수정하여 작성한 것이다.
2차. 12줄 줄었다.
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