# https://www.acmicpc.net/problem/13334
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

segments = []
for _ in range(int(input())):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    segments.append((h, o))
d = int(input())
events = []
for a, b in segments:
    if b - a > d: # d 넘는건 미리 제외
        continue
    events.append((b, 1))  # b까지 들어와야 카운팅
    events.append((a+d+1, -1))  # a가 철로 밖으로 벗어나면 배출
events.sort()
max_cnt = 0
cur_cnt = 0
for _, event_type in events:
    cur_cnt += event_type
    max_cnt = max(max_cnt, cur_cnt)
print(max_cnt)

"""
현 시점 Gold II. 제출 12233. 정답률 37.479 %
이전엔 inner를 두고 안에 넣고 빼는 작업을 했다.
비효율적으로 보여서 이번엔 단순 이벤트로 해봤는데 오히려 더 느려졌다.
d가 h, o 입력 이후에 와서 for문을 한번 더 돌아줘서 그런듯.
"""
