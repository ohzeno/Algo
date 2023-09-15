# https://school.programmers.co.kr/learn/courses/30/lessons/12978
"""
1번 마을에 있는 음식점에서 k시간 이하인 곳들 주문 받아서 배달.
1번 마을도 포함.
주문 받을 수 있는 마을 갯수 리턴.
1 <= n <= 50
1 <= len(road) <= 2000
두 마을을 연결하는 도로가 여럿 있을 수 있음.
1 <= k <= 500,000
임의의 두 마을 간 항상 이동 가능한 경로가 존재.
"""


def solution(N, road, K):
    INF = float('inf')
    mat = [[INF] * N for _ in range(N)]
    for st, ed, cost in road:
        min_cost = min(mat[st - 1][ed - 1], cost)
        mat[st - 1][ed - 1] = min_cost
        mat[ed - 1][st - 1] = min_cost
    for mid in range(N):
        for st in range(N):
            for ed in range(N):
                if st != mid != ed and st != ed:
                    mat[st][ed] = min(mat[st][ed], mat[st][mid] + mat[mid][ed])
    return 1 + sum(1 for i in range(N) if mat[0][i] <= K)


inputdatas = [
    [5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3],
    [
        6,
        [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]],
        4,
    ],
]

"""
Summer/Winter Coding(~2018) 기출. 
Lv.2. 현 시점 완료한 사람 7,979명, 정답률 46%

다익스트라는 왠지 모르게 귀찮아서 플로이드 워셜로 풀었다.
통과는 했지만 
플로이드 워셜은 모든 정점에서 모든 정점으로의 최단 경로를 구하고
다익스트라는 하나의 정점에서 모든 정점으로의 최단 경로를 구하므로
이 문제에는 다익스트라가 더 적합하다.
"""

for t in inputdatas:
    print(solution(*t))
