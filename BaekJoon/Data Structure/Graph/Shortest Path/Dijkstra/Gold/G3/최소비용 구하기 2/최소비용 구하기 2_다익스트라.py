# https://www.acmicpc.net/problem/11779
import sys

# sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
n(1≤n≤1,000)개의 도시. 한 도시에서 출발, 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스. 
A에서 B까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
A에서 B 까지 가는데 드는 최소비용과 경로를 출력하여라. 
항상 시작점에서 도착점으로의 경로가 존재한다.

첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 
셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 
    출발 도시, 도착 도시, 비용 
    0 ≤ 버스 비용 < 100,000
m+3째 줄에는 구하고자 하는 구간 출발점과 도착점이 주어진다.

첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력.
둘째 줄에는 최소 비용 경로에 포함되어있는 도시의 개수를 출력. 출발 도시와 도착 도시도 포함.
셋째 줄에는 최소 비용 경로를 방문하는 도시 순서대로 출력.
"""

n, m = int(input()), int(input())
INF = 1e9
mat = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    mat[a][b] = min(mat[a][b], c)
st, fin = map(int, input().split())
visited = [0] * (n+1)
visited[st] = 1
for _ in range(n-1):
    min_cost = INF
    min_idx = 0
    for mid in range(1, n + 1):
        if not visited[mid] and mat[st][mid] < min_cost:
            min_cost = mat[st][mid]
            min_idx = mid
    visited[min_idx] = 1
    for ed in range(1, n+1):
        new_cost = mat[st][min_idx] + mat[min_idx][ed]
        if new_cost < mat[st][ed]:
            mat[st][ed] = new_cost

def find(st, fin):
    if st == fin:
        return [st]
    for mid in range(1, n+1):
        if mid == st or mid == fin:
            continue
        if mat[st][fin] == mat[st][mid] + mat[mid][fin]:
            front = find(st, mid)
            back = find(mid, fin)
            if front[-1] == back[0]:
                front.pop()
            return front + back
    return [st, fin]

print(mat[st][fin])
paths = find(st, fin)
print(len(paths))
print(*paths)


"""
현 시점 골드 3. 제출 34644. 정답률 36.587 %
경로 찾는게 좀 귀찮았다.
풀고보니 다른 사람들은 전부 우선순위 큐를 이용해 풀었다.
python 사이에서 혼자 pypy로 같은 시간대에 랭크된게 아이러니.
"""
