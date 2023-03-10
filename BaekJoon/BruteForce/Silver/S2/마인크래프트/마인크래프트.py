# https://www.acmicpc.net/problem/18111
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
세로 n, 가로 m. 좌상단 0, 0. 땅 고르기를 위해 두 작업을 할 수 있음.
    1. 좌표 i, j의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. 2초
    2. 인벤토리에 있는 블록을 좌표 i, j의 가장 위에 있는 블록 위에 놓는다. 1초
땅 고르기에 걸리는 최소 시간, 그 경우 땅의 높이를 출력하라.
단, 집터 아래 빈 공간은 존재X. 집터 바깥에서 블록을 가져올 수 없음. 
작업 시작시 인벤토리에 B개의 블록이 들어있음. 
땅의 높이는 256을 초과하지 않고 음수가 될 수 없음.
i+2 째 줄의 j+1 수가 i, j의 땅(?)
"""
from collections import Counter
n, m, b = map(int, input().split())
land = []
for _ in range(n):  # 블럭 위치가 중요하지 않기에 1차원 리스트로 변환하여 min, max, sum 시간절약
    land.extend(map(int, input().split()))
min_h, max_h = min(land), max(land)
total = sum(land)
land = Counter(land)  # take, use 구할 때 시간 절약 위해 Counter 사용
min_t, h = float('inf'), 0
for target_h in range(min_h, max_h + 1):
    if total + b < n * m * target_h:  # 총 블럭 갯수보다 필요한 블럭 갯수가 많으면 의미없음.
        continue
    take, use = 0, 0
    for key in land:
        if key > target_h:
            take += (key - target_h) * land[key]
        elif key < target_h:
            use += (target_h - key) * land[key]
    t = take * 2 + use
    # 시간이 같을 때 높이가 높은 것을 출력해야 함.
    # for문에서 높이가 계속 증가하므로 h를 따로 비교할 필요는 없음.
    if t <= min_t:
        min_t, h = t, target_h
print(min_t, h)

"""
현 시점 실버2. 제출 40721, 정답률 24.361%
구현, 브루트포스라고 나와있어서 처음에 시뮬레이션으로 풀려고 했다.
하지만 높은 쪽을 깎을지, 낮은 쪽을 깎을지 결정하는 과정을 다 구현하려니 상당히 복잡해졌고, 
시간제한 1초를 맞추지 못할거라 생각했다.
다른 풀이에서 높이를 순회한다는 아이디어를 얻어 테스트해봤으나 시간초과가 발생했다.
초기 맵의 최소 높이 ~ 최대높이만 확인하도록 수정했고, 시간초과 발생.
블럭 개수를 미리 구하기 위해 sum 사용, 해당 높이의 블럭 개수와 비교하여 시간을 줄였다.
그래도 시간초과 발생. min, max, sum을 사용할 때 sum(map(sum, land))식으로 사용했기에 
land를 1차원 리스트로 바꿔 시간을 줄였다. 블럭의 위치는 중요하지 않은 문제이기에 가능한 방법.
list로 변환하여 이어붙이지 않아도 extend를 사용하면 
map이 리스트로 변환되어 이어진다는 것을 처음 알았다.
pypy3만 통과.
처음에 land 전체에 Counter를 사용하여, take, use를 계산할 때 n*m 순회를 하지 않도록 했다.
python3에서도 통과.
실버 2라기엔 시간제한 때문에 많이 어려웠다. 골드 2 푼 기분.
평가들을 보니 다른 언어에서는 시간제한이 딱히 문제되지 않아서, 
높이를 순회한다는 아이디어만 얻으면 끝인듯.
"""