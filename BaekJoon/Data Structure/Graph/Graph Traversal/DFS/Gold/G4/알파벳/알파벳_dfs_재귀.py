# https://www.acmicpc.net/problem/1987
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
rxc 크기의 보드. 각 칸은 대문자 알파벳.
좌상단에는 말이 놓여있음.
말은 상하좌우로 인접한 네 칸 중 한 칸으로 이동 가능.
같은 알파벳이 적힌 칸을 두 번 지날 수 없음.
최대 몇 칸을 지날 수 있는지 출력하라. 좌상단도 칸 수에 포함.
1 <= r, c <= 20
"""

def dfs(r, c, cnt, used):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] not in used:
            if cnt == 25:
                print(26)
                exit()
            new_s = used + mat[nr][nc]
            if new_s not in visited[nr][nc]:
                visited[nr][nc].add(new_s)
                dfs(nr, nc, cnt + 1, new_s)


R, C = map(int, input().split())
mat = [list(input()) for _ in range(R)]
visited = [[set()] * C for _ in range(R)]
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
max_cnt = 1
dfs(0, 0, 1, mat[0][0])
print(max_cnt)


"""
현 시점 골드 4. 제출 124220. 정답률 28.156 %
dfs로 푸는건 맞는데, 예상 못한 가지치기가 좀 있었다.
경로 상에 중복 문자들이 많아서, 다른 경로로 와도 같은 문자열 경로인 경우가 있다.
그런 경우는 의미 없는 탐색이므로 가지치기를 해야 한다.
시작 지점과 도착지점을 제외한 알파벳의 사용 여부가 똑같은 경우도 의미없으므로 가지치기 하려고
new_s = st + ''.join(sorted(used[1:])) + mat[nr][nc]
이렇게 해봤는데, 이건 시간을 좀 더 썼다.
꼭 더 느리다기 보다는 주어진 테케들이 이 풀이에 안맞았다.

visted로 set()를 쓰지 않고 하나의 경로만 기록하면 더 빠르긴 한데,
이는 테케가 우연히 적합한것이다. 
저렇게 하면 여러 경로 중 하나만 기록해서 중복처리 하므로 다른 경로를 제거할 수 없다. 
예를 들면 ABCD와 ABED는 중간 알파벳 사용이 다르므로 각각 중복처리를 해줘야 한다. 
하지만 제일 빠른 풀이들은 visited[nr][nc]에 하나만 기록하므로, 
ABCD가 기록된 상태로 ABED가 들어오면 ABCD는 사라지기에,
이후에 다른 경로로 ABCD가 들어와도 중복처리가 안된다. 

대부분의 블로그 풀이는 경로중복 처리를 하지 않아서 시간초과가 아슬아슬하다.
"""
