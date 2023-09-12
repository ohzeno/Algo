# https://www.acmicpc.net/problem/13334
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
수평선 상에 n명의 사람들의 집과 사무실이 위치.
위치 겹칠 수 있음.
어느 두 점을 잇는 철로를 건설하여 기차 운영할 것.
철로 길이는 d. 
집, 사무실 위치 모두 철로 선분에 포함되는 사람들의 수가 최대가 되도록.
1 <= n <= 100,000
h, o는 -10^8 이상 10^8 이하의 정수
철로 길이 1 <= d <= 2 * 10^8
"""
from heapq import heappush as hpush, heappop as hpop
n = int(input())
cases = []
for _ in range(n):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    cases.append((h, o))
d = int(input())
cases.sort(key=lambda x: x[1])
max_cnt = 0
inner = []
for st, ed in cases:
    if ed - st > d:
        continue
    while inner and inner[0] < ed - d:
        hpop(inner)
    hpush(inner, st)
    max_cnt = max(max_cnt, len(inner))
print(max_cnt)


"""
현 시점 골드 2. 제출 8088. 정답률 37.153 %
슬라이딩 윈도우처럼 보이지만 모든 점을 순회하는게 불가하고,
내부 선분 갯수를 매번 체크해줘야 한다.
비슷한 문제를 풀었던 기억이 있어서 home 별로 office를 정렬해놓고
home을 순회해봤는데 시간초과가 발생했다.

끝점 기준으로 정렬하고, 철로보다 먼 거리가 아닌 케이스에 한해서
inner에 들어있는 선분 중 가장 왼쪽 케이스들의 출발점이 철로를 벗어나면 pop
hpush로 현재 케이스를 넣어준다.
그러면 매 케이스마다 inner에 들어있는 케이스들은 모두 철로를 벗어나지 않는 케이스들이다.
시작점이 아니라 끝점을 기준으로 체크를 해줬어야 하는 문제.
"""