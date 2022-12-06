# https://school.programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations
def solution(expression):
    # 숫자, [+, -, *] 로 이루어진 연산 수식.
    # 연산자 우선순위 재정의해서 만들 수 있는 가장 큰 숫자 만들기.
    # 같은 순위의 연산자는 없어야 함.
    # 음수는 절대값으로 제출. 제출 숫자를 우승 상금으로 지급함.
    operators = []
    # 식에 포함된 오퍼레이터만 저장
    for operator in ['-', '+', '*']:
        if operator in expression:
            operators.append(operator)
    cases = permutations(operators)  # 연산자 우선순위 경우의 수
    datas = []
    s = ''
    for exp in expression:
        if exp.isdigit():  # 숫자
            s += exp
        else:  # 연산자 나오면 리스트에 숫자, 연산자 넣고 s초기화.
            datas += [int(s), exp]
            s = ''
    datas.append(int(s))  # 마지막 숫자
    max_num = 0
    for case in cases:  # 연산자 우선순위별로
        tmp_datas = datas  # 원본 복사.
        stack = []
        for op in case:  # 연산자 순회
            cur = 0
            while cur < len(tmp_datas):  # 범위 초과하지 않는 동안
                if tmp_datas[cur] == op:  # 우선연산자면
                    stack.append(eval(f'{stack.pop()}{op}{tmp_datas[cur + 1]}'))  # 스택에 계산결과 추가
                    cur += 2  # 연산 끝난 숫자 통과
                else:  # 우선 연산자 아니면 그냥 넣고 다음으로
                    stack.append(tmp_datas[cur])
                    cur += 1
            tmp_datas = stack  # 남은 식
            stack = []  # 스택 초기화
        if abs(tmp_datas[0]) > max_num:  # 최종 연산 결과 절대값이 최대값보다 높으면 갱신
            max_num = abs(tmp_datas[0])
    return max_num

inputdatas = [
    "100-200*300-500+20",
    "50*6-3*2"
]

"""
2020 카카오 인턴십 기출. Lv.2. 옮겨적기부터 채점까지 36분 소모했다.
처음엔 우선순위에 따라 스택을 이용해 한 번의 순회로 계산하는 방법을 생각했는데
규칙을 생각해내기가 힘들어 그냥 무식하게 연산자마다 순회를 돌며 계산했다.
베스트 풀이를 보니 엄청나게 효율적이고 짧게 작성됐다. split과 join을 이용해 ()로 우선순위를 만든 식을 eval로 계산했다.
훌륭하긴 하지만 내가 시험 중에 생각해내긴 힘들 것 같아 넘어간다.
"""

for t in inputdatas:
    print(solution(t))
