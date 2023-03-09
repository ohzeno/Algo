# https://www.acmicpc.net/problem/11651
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
점 n개가 주어진다.
y좌표는 증가하는 순, y좌표가 같으면 x좌표가 증가하는 순으로 정렬하여 출력하라
"""
datas = []
for _ in range(int(input())):
    datas.append(list(map(int, input().split())))
datas.sort(key=lambda x: (x[1], x[0]))
for data in datas:
    print(*data)

"""
현 시점 실버5. 제출 57885, 정답률 67.160%
프로그래머스 문제들 풀면서 익혔던 튜플 정렬. 
확실히 solved.ac의 클래스 문제들도 도움이 되는 듯 하다.
낮은 클래스에서 이런 것들을 익혔다면 고난도 문제 풀 때 더 편했을거라 생각한다.
"""