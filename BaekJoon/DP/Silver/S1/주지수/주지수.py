# https://www.acmicpc.net/problem/15724
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

'''
DP로 풀지 않으면 무조건 시간초과 나는 문제. 범위합 for문 돌거나 리스트 슬라이싱 sum으로 더해도 시간초과.
'''
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
acc = [[0] * (m + 1) for _ in range(n + 1)]  # 범위합 인덱스가 1부터 시작하니 상단, 좌단에 0추가
for i in range(1, n+1):
    for j in range(1, m+1):
        # 현재 칸 누적합 = 상 누적합 + 좌 누적합 + 현재칸 - 좌상단 누적합
        acc[i][j] = acc[i][j - 1] + acc[i - 1][j] + mat[i - 1][j - 1] - acc[i - 1][j - 1]
k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, (input().split()))
    # 범위누적합 = 우하단 누적합 - 좌 범위밖 누적합 - 상 범위 밖 누적합 + 좌상단 누적합
    ans = acc[x2][y2] - acc[x2][y1 - 1] - acc[x1 - 1][y2] + acc[x1 - 1][y1 - 1]
    print(ans)

