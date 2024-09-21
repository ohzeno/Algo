# https://school.programmers.co.kr/learn/courses/30/lessons/72413
def solution(n, s, a, b, fares):
    mat = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for fare in fares:  # 비용 갱신
        fs, fe, fc = fare
        mat[fs][fe] = fc
        mat[fe][fs] = fc
    for i in range(1, n + 1):
        mat[i][i] = 0  # 자기 자신으로 가는 비용 0
    # 플로이드 워셜. 경로 최단비용 갱신.
    for tp in range(1, n + 1):  # tp 노드 경유. 출발노드가 아니라 경유노드를 체크.
        for ts in range(1, n + 1):  # ts 노드에서 출발
            for te in range(1, n + 1):  # te 노드로 갈 때
                if ts != tp != te:  # 경유노드가 출발노드나 목적노드와 같으면 안됨.
                    if mat[ts][tp] + mat[tp][te] < mat[ts][te]:  # tp 노드 경유했을 때 더 빠르면 갱신
                        mat[ts][te] = mat[ts][tp] + mat[tp][te]
    # 따로 갈 경우의 비용.
    # 경로가 겹칠 경우 합승구간의 비용이 2배로 책정된다.
    tmp_cost = mat[s][a] + mat[s][b]
    # i2까지 합승 후 나눠갈 때의 비용 체크.
    # i2가 목표지점과 같아도 확인해야 한다.
    # ex) 경로 겹쳐서 중간에 b가 6에서 내렸다고 가정하면,
    # mat[i2][b]가 mat[6][6]이 되어 0이 더해져서 중간에 내린게 반영된다.
    for i2 in range(1, n + 1):
        if i2 == s:
            continue
        cost_pass = mat[s][i2] + mat[i2][a] + mat[i2][b]
        if cost_pass < tmp_cost:
            tmp_cost = cost_pass
    return tmp_cost

inputdatas = [
    [6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]],
    [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]],
    [6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]]
]
"""
2021 카카오 공채 기출. 플로이드 워셜 쓰면 순식간에 해결된다.
다만, 처음 풀 때 플로이드워셜, 크루스칼, 프림 등을 고려하고도 적용이 안될거라 판단했었다.
최소비용은 경로를 포함하지 않기에, 해당 알고리즘들에 경로를 추가해서 계산을 해야한다고 생각했었다.
플로이드워셜 적용 후 체크만 하면 된다는 사실을 알게되면 15분도 안걸릴 문제지만
거기까지 사고가 닿지 않으면 한없이 어려워지던 문제. 다시 풀어 볼 필요가 있다.
"""

for t in inputdatas:
    print(solution(t[0], t[1], t[2], t[3], t[4]))
