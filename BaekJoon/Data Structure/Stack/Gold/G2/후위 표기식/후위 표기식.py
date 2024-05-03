# https://www.acmicpc.net/problem/1918
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램을 작성하시오
첫째 줄에 중위 표기식이 주어진다. 
단 이 수식의 피연산자는 알파벳 대문자로 이루어지며 수식에서 한 번씩만 등장한다. 
그리고 -A+B와 같이 -가 가장 앞에 오거나 AB와 같이 *가 생략되는 등의 수식은 주어지지 않는다. 
표기식은 알파벳 대문자와 +, -, *, /, (, )로만 이루어져 있으며, 길이는 100을 넘지 않는다. 
"""
def infix_to_postfix(infix):
    ops = []
    res = ''
    priority = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
    }
    for s in infix:
        if s.isalpha():
            res += s
        elif s == '(':
            ops.append(s)
        elif s == ')':
            while ops and ops[-1] != '(':
                res += ops.pop()
            ops.pop()
        else:
            while ops and priority[ops[-1]] >= priority[s]:
                res += ops.pop()
            ops.append(s)
    while ops:
        res += ops.pop()
    return res

infix = input()
print(infix_to_postfix(infix))


"""
현 시점 골드 2. 제출 48931. 정답률 37.554 %
중위 표기법을 후위 표기법으로 변환하는 Shunting Yard 알고리즘을 사용.
처음에는 알고리즘을 이해해보려 했는데 그냥 외우는게 나을 듯.
"""