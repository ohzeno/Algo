# https://school.programmers.co.kr/learn/courses/30/lessons/150365
"""
nxm 격자가 주어진다. x,y에서 출발해 r,c로 이동해서 탈출해야 한다.
1. 격자 바깥으로는 나갈 수 없음
2. x,y에서 r,c까지 이동 거리가 총 k여야 한다. 같은 격자를 두 번 이상 방문해도 된다.
3. 미로에서 탈출한 경로를 문자열로 나타냈을 때, 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 한다.

이동경로는 lrud로 표현 가능.
경로를 리턴하라. 불가능할 경우 impossible를 리턴.

2 ≤ n (= 미로의 세로 길이) ≤ 50
2 ≤ m (= 미로의 가로 길이) ≤ 50
1 ≤ x ≤ n
1 ≤ y ≤ m
1 ≤ r ≤ n
1 ≤ c ≤ m
(x, y) ≠ (r, c)
1 ≤ k ≤ 2,500
"""
import sys

sys.setrecursionlimit(10**6)


def solution(n, m, x, y, r, c, k):
    m_dist = abs(x - r) + abs(y - c)  # 목표까지 최소 거리
    # 목표까지 최소 거리가 k보다 크거나,
    # k-m_dist가 홀수면 불가능(왕복으로 돌아와야 하는데 홀수면 안됨)
    if m_dist > k or (k - m_dist) % 2:
        return "impossible"
    dirs = {
        "d": (1, 0),
        "l": (0, -1),
        "r": (0, 1),
        "u": (-1, 0),
    }
    min_path = "z"  # 사전순 비교 위한 초기값

    def dfs(i, j, path):
        nonlocal min_path
        l_path = len(path)
        if i == r and j == c and l_path == k:
            min_path = min(min_path, path)
            return
        # 현재까지 이동거리 + 맨해튼거리가 k 넘으면 도달 불가
        if l_path + abs(i - r) + abs(j - c) > k:
            return
        for dir, dif in dirs.items():
            ni, nj = i + dif[0], j + dif[1]
            if not (1 <= ni <= n and 1 <= nj <= m):
                continue
            npath = path + dir
            if npath < min_path:  # 사전순 더 빠른 경우만 탐색
                dfs(ni, nj, npath)

    dfs(x, y, "")
    return min_path


inputdatas = [
    [[3, 4, 2, 3, 3, 1, 5], "dllrl"],
    [[2, 2, 1, 1, 2, 2, 2], "dr"],
    [[3, 3, 1, 2, 3, 3, 4], "impossible"],
]

"""
2023 KAKAO BLIND RECRUITMENT 기출. 
Lv.3. 현 시점 완료한 사람 1,973명, 정답률 29%
맨해튼 거리도 떠올렸고, 경로 반복도 떠올렸지만 풀지 못했다.
현재 위치와 종료점까지의 맨해튼 거리를 체크해줘야 하는데 그걸 안했었다...

사전순으로 더 빠른 경우가 min_path보다 나중에 나올 경우를 고려할 필요는 없다.
dlru순으로 순회하고, dfs로 진행하기 때문.

출발점과 도착점이 다르다는 조건이 없어서 풀 때 신경썼었는데,
종료조건에 이동거리를 넣어서 해결됐다.

원래는 최소거리를 찾은 후에 왕복코스들을 경로 중간에 끼워넣으려고 했었고,
그래서 종료조건에 이동거리가 없어서 출발하자마자 조건에 걸릴 수 있었다.
"""

for data, ans in inputdatas:
    res = solution(*data)
    if res == ans:
        print("pass")
    else:
        print("fail\n", f"expected:{ans}\n", f"got:{res}\n")
