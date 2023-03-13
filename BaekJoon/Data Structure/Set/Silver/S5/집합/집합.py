# https://www.acmicpc.net/problem/11723
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
"""

def add(x):
    s.add(x)

def remove(x):
    s.discard(x)  # 원소가 없어도 오류x. remove는 원소가 없으면 오류 발생.

def check(x):
    if x in s:
        print(1)
    else:
        print(0)

def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)

def all():
    s.update(range(1, 21))

def empty():
    s.clear()

s = set()
for _ in range(int(input())):
    cmd, *n = input().split()  # *n으로 두면 오른쪽 원소가 없더라도 빈 리스트가 할당되어 오류X
    if cmd == 'all':
        all()
    elif cmd == 'empty':
        empty()
    else:
        n = int(n[0])
        if cmd == 'add':
            add(n)
        elif cmd == 'remove':
            remove(n)
        elif cmd == 'check':
            check(n)
        elif cmd == 'toggle':
            toggle(n)


"""
현 시점 실버5. 제출 74469, 정답률 29.250%
집합 문제라 쉽게 풀었다. cmd, *n = input().split() 이런 입력방식은 처음 써봤다.
*n으로 두지 않고 n으로 두면 입력값에 all처럼 공백 기준 둘로 나뉘지 않으면 오류가 발생한다.
*n으로 두면 오른쪽에 아무것도 없으면 n에 빈 리스트가 할당된다.
"""