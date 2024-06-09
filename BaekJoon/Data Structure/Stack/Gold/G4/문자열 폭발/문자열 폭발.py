# https://www.acmicpc.net/problem/9935
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
- 폭발 문자열은 모두 함께 터진다. 남은 문자열을 이어붙여 새로운 문자열을 만든다.
- 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수 있다.
- 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
모든 폭발이 끝난 후 남은 문자열을 출력하라.
남아있는 문자열이 없으면 "FRULA"를 출력하라.
폭발 문자열은 같은 문자 중복이 없다.
1 <= len(s) <= 1e6
1 <= len(폭발 문자열) <= 36
두 문자열은 모두 알파벳, 숫자로만 이루어져 있다.
"""

s = input()
bomb = input()
stack = []
len_bomb = len(bomb)
bomb_tail = bomb[-1]
for c in s:
    stack.append(c)
    if c == bomb_tail and ''.join(stack[-len_bomb:]) == bomb:
        for _ in range(len_bomb):
            stack.pop()
print(''.join(stack) if stack else 'FRULA')



"""
현 시점 골드 4. 제출 83100. 정답률 26.269 %
처음엔 while문 돌리면서 사이클마다 폭발 함수를 돌리려고 했다.
스택을 사용하면 여러 사이클을 거칠 필요 없이 한 번의 순회로 해결할 수 있다.
"""