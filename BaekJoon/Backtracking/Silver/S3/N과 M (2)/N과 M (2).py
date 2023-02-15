# https://www.acmicpc.net/problem/15650
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

# 1~n 자연수 중 중복없이 m개 고른 모든 오름차순 수열을 오름차순으로 한 줄에 수열 하나씩 출력
# 각 수열의 원소는 공백으로 구분
def dfs(count, data):
    if count == m:
        ans.append(data)
        return
    st = 1 if not data else data[-1] + 1  # 수열을 오름차순으로 유지시키기 위함.
    for i in range(st, n + 1):
        if not visited[i]:
            visited[i] = 1
            dfs(count + 1, data + [i])
            visited[i] = 0

n, m = map(int, input().split())
visited = [0] * (n+1)
ans = []
dfs(0, [])
for an in ans:
    print(*an)

"""
현 시점 실버3. 제출 54696.  정답률 74.148 %
처음에 대충 코딩하고 제출했는데 틀려서 의아했는데
'고른 수열은 오름차순이어야 한다'가 '수열들을 오름차순으로 출력이 아니라 
'수열 자체가 오름차순인 것만 골라야 한다'였다.
"""