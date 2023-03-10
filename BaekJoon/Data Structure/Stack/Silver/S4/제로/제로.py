# https://www.acmicpc.net/problem/10773
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
정수가 주어진다. 0인 경우 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
정수가 0일 경우, 지울 수 있는 수가 항상 존재한다.
최종적으로 적어 낸 수의 합을 출력하라.
"""

datas = []
for _ in range(int(input())):
    n = int(input())
    if not n:
        datas.pop()
    else:
        datas.append(n)
print(sum(datas))

"""
현 시점 실버4. 제출 64123, 정답률 67.545%
분류가 스택이라는걸 보고나서야 스택이라는걸 눈치챘다.
딱히 복잡한 과정이 없어서 스택인 줄도 몰랐다.
"""