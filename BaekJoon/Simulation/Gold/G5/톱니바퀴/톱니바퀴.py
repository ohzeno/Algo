# https://www.acmicpc.net/problem/14891
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
톱니가 8개인 톱니바퀴 4개가 가로로 일렬로 놓여있다. 톱니는 N 또는 S극이다.
톱니바퀴는 왼쪽부터 1~4번이다.
톱니바퀴를 총 k번 회전시키려 한다. 회전은 한 칸이 기준이다.
회전은 시계/반시계 방향이 있다.
서로 맞닿은 극에 따라 옆에 있는 톱니바퀴에 영향이 있을 수 있다.
1번 바퀴가 회전할 때 2번 바퀴와 맞닿은 톱니의 극이 다르면 2번 바퀴는 반대 방향으로 회전한다.
톱니바퀴의 초기 상태와 회전이 주어질 때 최종 상태를 구하라.

range(1, 5)의 i번 줄에 i+1번 톱니바퀴의 상태가 주어진다. 
상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다.
0: N극, 
1: S극

다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 
다음 K개 줄에는 명령이 순서대로 주어진다. 
바퀴 번호, 방향
1: 시계방향
-1: 반시계방향

총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.
    1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
    2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
    3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
    4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
"""
from collections import deque
def connected(g1, g2):
    # 0: 12시, 2: 3시, 6: 9시
    if g1 < g2:
        return gear[g1][2] != gear[g2][6]
    return gear[g1][6] != gear[g2][2]

def get_tgs(g, d):
    tgs = [(g, d)]
    ld = d
    for i in range(max(g-1, 0), 0, -1):  # 왼쪽 연결 탐색
        if not connected(i, i + 1):
            break
        ld *= -1
        tgs.append((i, ld))
    for j in range(min(g+1, 5), 5):  # 오른쪽 연결 탐색
        if not connected(j-1, j):
            break
        d *= -1
        tgs.append((j, d))
    return tgs

gear = {i: deque(map(int, input())) for i in range(1, 5)}
for _ in range(int(input())):
    tg, d = map(int, input().split())
    for tg, d in get_tgs(tg, d):
        gear[tg].rotate(d)
print(sum([2**(i-1) if gear[i][0] else 0 for i in range(1, 5)]))


"""
현 시점 골드 5. 제출 32735. 정답률 54.549%
33분 걸렸다. 문제 읽는데만 4분은 쓴듯.
연결된 바퀴들을 어떻게 찾을지가 관건. 다른 부분은 딱히 어렵지 않은 문제.
rotate를 쓰지 않더라도 pop, append를 쓰면 된다.
"""