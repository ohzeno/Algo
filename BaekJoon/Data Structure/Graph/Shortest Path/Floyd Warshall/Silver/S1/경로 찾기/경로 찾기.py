# https://www.acmicpc.net/problem/11403
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def floyd_warshall():
    # 초기 가중치 입력
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                ans[i][j] = 1
    for i in range(n):  # i행을 중간경로로
        for j in range(n):
            for k in range(n):
                if j != i and k != i:  # 중간노드 제외하고 체크
                    # j에서 i를 경유해 k로 가는 비용이 기존 비용보다 싸면 갱신
                    if ans[j][i] + ans[i][k] < ans[j][k]:
                        ans[j][k] = ans[j][i] + ans[i][k]
    # 정답은 0을 사용해야 하므로 inf는 전부 0으로
    # 가중치 존재하면 경로 존재하니 1로 변경
    for i in range(n):
        for j in range(n):
            if ans[i][j] == float('inf'):
                ans[i][j] = 0
            else:
                ans[i][j] = 1

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
ans = [[float('inf')] * n for _ in range(n)]  # 플로이드-워셜 용 가중치 그래프
floyd_warshall()
for sol in ans:
    print(*sol)
"""
처음에 dfs로 풀려고 했는데 뭔가 잘못 짰는지 시간초과가 계속 났다.
그냥 편하게 플로이드-워셜로 비용을 계산했다. inf가 아니라면 경로 존재.
"""