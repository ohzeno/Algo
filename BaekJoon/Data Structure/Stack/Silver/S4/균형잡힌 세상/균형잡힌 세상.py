# https://www.acmicpc.net/problem/4949
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
소괄호, 대괄호는 짝을 이뤄야 함.
모든 오른쪽 괄호는 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재.
모든 괄호들은 1:1 매칭만 가능.
짝을 이후는 두 괄호 사이 문자열도 균형이 잡혀야 한다.
각 문자열은 마지막 글자를 제외하고 알파벳, 소괄호, 대괄호로 이루어지고 온점으로 끝난다.
"""

while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    for s in sentence:
        if s in '([':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()  # 짝 제거
            else:
                """
                짝이 없으면 추가. 
                스택에 넣지 않고 print('no')하고 break한 후 
                아래에서 for-else를 이용해 yes를 출력한다면 
                sentence = ')'일 경우 yes가 되어버린다.
                """
                stack.append(s)
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break
    if stack:
        print('no')
    else:
        print('yes')


"""
현 시점 실버4. 제출 89247, 정답률 32.267%
문제 설명에 나온 규칙은 괄호가 항상 1:1 매칭되며, 사이에 있는 문자열이 '균형 잡혀야 한다'고 되어있다.
그런데 '문자열의 균형'에 대한 정의가 없어 혼란스러웠다.
예시 입출력을 보니 문자열은 아무런 쓸모가 없다. 
문제에서 의도한 '짝을 이루다'는 순서가 맞는 매칭이 아니라 문장 내에 반대 방향 괄호가 있다는 의미이다.
문제에서 의도한 '문자열의 균형'은 사실 '짝이 되는 괄호 사이의 괄호들'도 균형이 잡혀야 한다는 의미이다.
설명이 더러운데 그냥 평범한 괄호 유효성 검사 문제다.
"""