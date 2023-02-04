# https://www.acmicpc.net/problem/15721
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
뻔-데기-뻔-데기-뻔-뻔-데기-데기 가 1회차
2회차는 뒤쪽 뻔, 데기가 3번씩.
a명이 원형으로 앉음. 일구가 0번째. t번째 뻔 또는 데기를 외치는 사람은 원에서 몇번인가 구하라.
반시계 방향으로 번호 증가, 게임 진행.
"""

def sol():
    def check(s):
        idx[0] = (idx[0] + 1) % a  # 사람 갱신
        if s == target:  # 타겟이면
            nth[0] += 1  # 타겟 갯수 갱신
            if nth[0] == t:  # 목표 도달했으면 True
                return True
    cycle = 1  # 몇회차?
    nth = [0]  # 몇 번째 타겟인가
    idx = [-1]  # 현재 사람
    while True:
        for s in ['뻔', '데기'] * 2:
            if check(s):  # 목표면 사람 번호 반환
                return idx[0]
        for s in ['뻔'] * (cycle + 1):
            if check(s):
                return idx[0]
        for s in ['데기'] * (cycle + 1):
            if check(s):
                return idx[0]
        cycle += 1

a, t = int(input()), int(input())
target = '데기' if int(input()) else '뻔'
print(sol())

"""
현 시점 실버5. 제출 1364, 정답률 45.744 %
브루트포스인데 좀 귀찮다. 
인터넷에 돌아다니는 풀이들을 보니 같은 풀이들이고,
모두 뻔/데기를 0, 1로 표기했는데 그러면 코드 가독성이 끔찍하다.
"""
