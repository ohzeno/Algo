# https://school.programmers.co.kr/learn/courses/30/lessons/150369
def solution(cap, n, deliveries, pickups):
    """
    1렬로 나열된 n개 집에 배달.
    택배는 상자에 담아 배달하며,
    배달 다니면서 빈 상자들 수거.
    i번째 집은 물류창고에서 거리 i
    트럭에 상자 최대 cap개 실을 수 있음
    각 집마다 배달할 택배 수와 수거할 상자 개수를 알고있음.
    트럭 하나로 모든 배달과 수거를 마치고 돌아올 수 있는 최소 이동거리?
    각 집에 배달/수거할 때 원하는 개수만큼 배달/수거 가능.

    1 ≤ cap ≤ 50
    1 ≤ n ≤ 100,000
    deliveries의 길이 = pickups의 길이 = n
    deliveries[i]는 i+1번째 집에 배달할 택배 개수를 나타냅니다.
    pickups[i]는 i+1번째 집에서 수거할 상자의 개수를 나타냅니다.
    0 ≤ deliveries의 원소 ≤ 50
    0 ≤ pickups의 원소 ≤ 50
    트럭의 초기 위치는 물류창고입니다.
    """
    d = p = dist = 0
    for i in reversed(range(n)):  # 가장 먼 집부터
        d += deliveries[i]
        p += pickups[i]
        while d > 0 or p > 0:  # 배달할 택배나 수거할 상자가 있으면
            d -= cap  # 1회치 배달. 음수되면 미리 배달한(실제로는 오는 길에 앞집 배달한) 효과.
            p -= cap  # 1회치 수거
            dist += (i + 1) * 2  # 왕복거리 더해주기
    return dist

inputdatas = [
    [4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]],
    [2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]]
]

"""
2023 카카오 공채 기출. 
현 시점 Lv.2. 제출 3102. 정답률 29%
공채 당시 bfs로 풀려다 실패했었다.
다시 풀 때도 bfs로 풀려다 실패했고, 카카오 해설을 보고 다시 풀었다.
greedy를 너무 오래 안풀어서 감각을 잊은 것 같다.
다이아 구현 문제보다 이게 더 어렵게 느껴졌다.
"""

for t in inputdatas:
    print(solution(*t))
