# https://www.acmicpc.net/problem/15649
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
ans = []
nums = [i_ for i_ in range(1, n+1)]
visited = [0] * n
def dfs(count, visited, acc):  # len(acc)가 시간을 많이 소모할거라 생각해 count변수를 따로 뒀다.
    if count >= m:  # m개 도달했으면 정답에 추가
        ans.append(acc)
        return
    for i in range(n):  # [1, 3]과 [3, 1]은 다른 수열. 그러니 처음부터 체크하도록.
        if not visited[i]:  # 이미 선택한 숫자 제외
            visited[i] = 1
            dfs(count + 1, visited, acc + [nums[i]])
            visited[i] = 0

dfs(0, visited, [])
for sol in ans:
    print(*sol)
