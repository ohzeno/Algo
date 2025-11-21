# https://www.acmicpc.net/problem/2458
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

# n: 학생 수, m: 키 비교 횟수
n, m = map(int, input().split())
win_lose = [[0] * (n+1) for _ in range(n+1)]
for _ in range(1, m+1):
    a, b = map(int, input().split())
    win_lose[a][b] = -1
    win_lose[b][a] = 1
for mid in range(1, n+1):
    for st in range(1, n+1):
        for ed in range(1, n+1):
            if win_lose[st][mid] and win_lose[st][mid] == win_lose[mid][ed]:
                win_lose[st][ed] = win_lose[st][mid]
                win_lose[ed][st] = -win_lose[st][mid]
confirmed = 0
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if a == b:
            continue
        if win_lose[a][b]:
            cnt += 1
    if cnt == n-1:
        confirmed += 1
print(confirmed)


"""
현 시점 Gold IV. 제출 22928. 정답률 54.267 %
플로이드-워셜 응용 연습하려고 풀었다.
그래프 이미지가 있어서 그런지 dfs사용하는 사람도 있고 그래서 정답률이 높은듯.
"""
