# https://www.acmicpc.net/problem/21610
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양.
좌상단은 1,1, 우하단은 N,N.
1번 행과 N번 행, 1번 열과 N번 열은 연결됨. 아래로 내려가면 위로 나온다는 뜻.
비바라기를 시전하면 (N,1), (N,2), (N-1,1), (N-1,2)에 비구름이 생긴다.
구름에 M번 이동하라고 명령한다. i번째 이동 명령은 di방향 si칸 이동한다.
1~8 방향은 좌, 좌상단, 상, 우상단, 우, 우하단, 하, 좌하단 순서.
이동을 명령하면
1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 이동한 구름이 있는 칸에 물이 1 증가한다.
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 
    대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 증가한다.
    - 이 때는 경계를 넘어가는 칸은 취급하지 않는다.
5. 물 양이 2 이상인 모든 칸에 구름이 생기고 물이 2 줄어든다. 
    이 때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양 합?
"""

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
clouds = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
dirs = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
for _ in range(m):
    d, s = map(int, input().split())
    visited = set()
    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    for cloud in clouds:  # r, c로 언팩킹해서 받으면 객체가 아니라 숫자를 받기에 원본 수정이 불가함.
        nr = (cloud[0] + dirs[d][0] * s) % n  # 범위 벗어나면 반대편에서 나온다.
        nc = (cloud[1] + dirs[d][1] * s) % n
        cloud[0], cloud[1] = nr, nc  # 구름 위치 수정
        # 2. 이동한 구름이 있는 칸에 물이 1 증가한다.
        mat[nr][nc] += 1
        visited.add((nr, nc))  # 5번에서 사용할 수 있도록 기록
    # 3. 구름이 모두 사라진다.
    clouds = []
    # 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다.
    for r, c in visited:
        count = 0
        for dr, dc in dirs[2::2]:  # 대각선만 순회
            nr = r + dr
            nc = c + dc
            # 범위 내만 탐색.
            if 0 <= nr < n and 0 <= nc < n and mat[nr][nc] > 0:
                count += 1
        mat[r][c] += count
    # 5. 물 양이 2 이상인 모든 칸에 구름이 생기고 물이 2 줄어든다.
    for r in range(n):
        for c in range(n):
            # 이 때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
            if mat[r][c] >= 2 and (r, c) not in visited:
                clouds.append([r, c])
                mat[r][c] -= 2
print(sum(map(sum, mat)))


"""
현 시점 골드5. 제출 9149, 정답률 50.467 %
처음에는 이동한 구름을 변수명만 바꿔서 리스트로 그대로 두고 5에서 in연산을 하였다.
그렇게 하면 시간초과가 발생한다. 그래서 in연산이 O(1)인 set를 사용하여 visited를 만들어 통과했다.
범위를 벗어나면 반대편에서 나오는 경우를 저번에는 if로 처리했던걸로 기억한다.
이번에는 %연산을 사용하여 처리했고, 굉장히 효율적이었다.
2차원 리스트 합을 구하는 방법으로 항상 for문을 사용했었다.
이번에는 map을 사용했고, 앞으로도 이렇게 할 듯 하다.

다른 사람들은 clouds의 원소들을 튜플로 두고, moved_cloud에 새 튜플을 추가하여 해결한 듯 하다.
결국 in연산은 리스트에 대해서 행해지니 시간복잡도는 같을 듯 한데, 
리스트에 리스트를 추가하는가, 튜플을 추가하는가 정도의 시간차이로 통과하지 못한다는게 좀 어이없다.
"""
