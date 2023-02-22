# https://www.acmicpc.net/problem/1277
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
최소 전선 길이 추가하여 1번 n번 발전소를 연결하라.
안정성 문제로 어떠한 두 발전소 사이 전선 길이가 m을 초과할 수는 없다.
연결에 필요한 최소 전설 길이 * 1000, 버림 후 출력
"""

def get_dist(p1, p2):
    return (abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2) ** 0.5

# n: 발전소 수,  w: 남아있는 전선 수
n, w = map(int, input().split())
m = float(input())  # m: 제한 길이
pos = {}  # 발전소 위치
mat = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    x, y = map(int, input().split())
    pos[i] = (x, y)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):  # 1부터 하면 중복됨. 그냥 dist 한번 구하고 대칭 저장.
        dist = get_dist(pos[i], pos[j])
        if dist <= m:  # 제한길이 넘지 않으면 기록
            mat[i][j] = dist
            mat[j][i] = dist
for _ in range(w):  # 추가 길이만 구하면 되므로, 이미 연결된 전선은 가중치 0으로 둔다.
    a, b = map(int, input().split())
    mat[a][b] = 0
    mat[b][a] = 0
# 다익스트라
visited = [0] * (n + 1)
visited[1] = 1  # 시작점 방문처리
# 시작노드 제외한 n-1개의 다른 노드들 처리
for _ in range(n - 1):
    min_value = float('inf')
    # 방문한 적 없는 발전소 중 가중치가 가장 낮은 발전소 찾기
    min_idx = 0  # 발전소 인덱스 기록할 변수
    for mid in range(1, n + 1):
        if not visited[mid] and mat[1][mid] < min_value:
            min_value = mat[1][mid]
            min_idx = mid
    visited[min_idx] = 1        # 해당 노드 방문처리
    # 해당 도시를 경유하여 가중치 갱신
    for ed in range(1, n + 1):
        new_dist = mat[1][min_idx] + mat[min_idx][ed]
        if not visited[ed] and new_dist < mat[1][ed]:
            mat[1][ed] = new_dist
print(int(mat[1][n] * 1000))

"""
현 시점 골드4. 제출 838, 정답률 29.383%
문제 설명에 문제가 있어 이해에 시간이 좀 걸렸다.
전선의 길이를 구하는 문제인데, 전선 길이를 어떻게 구하는지 나와있지 않다.
2차원 격자 좌표 상에서 전선을 잇는데, 직선 거리 한 칸이 거리 몇인지,
대각선 한 칸은 거리 몇인지 나와있지 않다.
미국 올림피아드 문제라는데 설명이 지나치게 부족하기에 좋은 문제는 아니다.
제한길이가 float인 점을 고려해 피타고라스 정리로 거리를 구했다.

오랜만에 다익스트라를 사용했는데, 알고리즘을 거의 잊고 있었다.
"""



