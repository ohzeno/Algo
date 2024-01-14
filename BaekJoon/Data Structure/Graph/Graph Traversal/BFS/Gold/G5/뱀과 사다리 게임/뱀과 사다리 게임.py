# https://www.acmicpc.net/problem/16928
import sys
sys.stdin = open("input.txt")
def input():
    return sys.stdin.readline().rstrip()
"""
1~6이 적힌 평범한 주사위 사용. 10x10 크기 보드판에는 1부터 100까지 수가 순서대로 적혀있다.
플레이어는 주사위를 굴려 나온 수만큼 이동한다. i번 칸에서 4가 나오면 i+4번 칸으로 이동한다.
i+주사위 수가 100을 넘어가면 이동X. 도착한 칸이 사다리면 사다리를 타고 위로 올라감. 
뱀이 있는 칸에 도착하면 뱀을 따라서 내려감. 1번 칸에서 시작. 100번 칸 도착이 목표.
원하는 수가 나오도록 주사위를 조작할 수 있을 때, 
게임판 상태가 주어지면, 주사위를 굴려야 하는 최소 횟수를 구하라.
모든 칸은 최대 하나의 사다리 또는 뱀을 가지며 동시에 두 가지를 모두 가지는 경우는 없다.
항상 100번 칸에 도달할 수 있는 입력만 주어진다.
"""
from collections import deque

n, m = map(int, input().split())
portal = {}
shortcut = {}
for _ in range(n + m):
    s, e = map(int, input().split())
    portal[s] = e
q = deque([(1, 0)])
while q:
    cur, step = q.popleft()
    for i in range(1, 7):
        nxt = cur + i
        # 1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니므로 사다리 타기 전 검사
        if nxt >= 100:
            print(step + 1)
            exit()
        if nxt in portal:
            nxt = portal[nxt]
        # 기존 도달보다 같거나 큰 횟수로 도달했다면 패스
        if nxt in shortcut and step + 1 >= shortcut[nxt]:
            continue
        shortcut[nxt] = step + 1
        q.append((nxt, step + 1))


"""
현 시점 골드 5. 제출 36143. 정답률 33.496 %
간단한 bfs 문제.
"""
