# https://school.programmers.co.kr/learn/courses/30/lessons/60058
def solution(p):
    # (와 )가 개수가 같으면 균형잡힌 괄호 문자열.
    # 짝도 다 맞으면 올바른 괄호 문자열
    def is_correct(datas):
        left_stack = []
        for data in datas:
            if data == '(':
                left_stack.append(data)
            else:
                if left_stack:
                    left_stack.pop()
                else:
                    return False
        return True

    def separator(datas):
        if not datas:
            return ""
        # 단, u는 균형문자열로 더 이상 분리할 수 없어야 하며
        left = right = 0
        for idx, data in enumerate(datas):
            if data == "(":
                left += 1
            else:
                right += 1
            if left == right:
                u = datas[:idx + 1]
                v = datas[idx + 1:]  # v는 빈 문자열이 될 수 있음.
                return u, v

    def check(datas):
        # 1. 입력이 빈 문자열이면 빈 문자열 반환.
        if not datas:
            return ""
        elif is_correct(datas):
            return datas
        # 2. 문자열 w를 두 "균형문자열" u, v로 분리.
        u, v = separator(datas)
        # 3. 문자열 u가 올바른 문자열이라면 v에 대해 1단계부터 다시 수행
        #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환
        if is_correct(u):
            return u + check(v)
        # 4. u가 올바른 문자열이 아니면 다음 수행.
        else:
            # 4-1. 빈 문자열 tmp에 첫 문자로 (를 붙임.
            # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 tmp에 이어붙임.
            # 4-3. tmp에 )를 붙임.
            tmp = '(' + check(v) + ')'
            # 4-4. u의 첫 번째, 마지막 문자 제거하고 남은 문자열의 괄호 방향을 뒤집어서 tmp의 뒤에 붙임.
            tmp_u = u[1:-1]
            rev_tmp_u = ''
            for t in tmp_u:
                if t == "(":
                    rev_tmp_u += ")"
                else:
                    rev_tmp_u += "("
            # 4-5. 생성된 문자열 반환
            return tmp + rev_tmp_u

    return check(p)


inputdatas = [
    "(()())()",
    ")(",
    "()))((()"
]

"""
2020 카카오 공채 기출. Lv.2. 옮겨적기부터 채점까지 36분 45초가량 걸렸다.
규칙 설명의 문장들이 주술관계가 명확하지 않거나 중의적인 문장이 많아 이해하기 힘들어서 좀 헤맸다.
주석으로 적은 내용은 예시를 보며 이해한 후,
본래 규칙에서 생략된 목적어와 부사를 추가하고 주어가 모호한 문장을 수정하여 작성한 것이다.
"""

for t in inputdatas:
    print(solution(t))
