# https://school.programmers.co.kr/learn/courses/30/lessons/81305
from itertools import combinations

def solution(k, num, links):
    # 시험장 고유 번호는 0 ~ n-1
    # k개의 그룹으로 나눠 가장 큰 그룹의 인원을 최소화 시켜 리턴.
    # num: 각 시험장 응시자 수,  links: 노드 연결 상태
    # 이진트리임. links[i]: i번 노드의 [왼쪽 자식, 오른쪽 자식], 노드가 없는 경우 -1 담겨있음.
    # k는 1~1만, num은 k~1만
    len_node = len(num)
    p_n = [-1] * len_node
    lc_n = [-1] * len_node
    rc_n = [-1] * len_node
    lp = [-1] * len_node
    rp = [-1] * len_node
    tot_p = [-1] * len_node
    connects = []
    for p_idx, [lc_idx, rc_idx] in enumerate(links):
        tmp_connects = []
        if lc_idx != -1:
            p_n[lc_idx] = p_idx
            tmp_connects.append([p_idx, lc_idx])
            lc_n[p_idx] = lc_idx
        if rc_idx != -1:
            p_n[rc_idx] = p_idx
            tmp_connects.append([p_idx, rc_idx])
            rc_n[p_idx] = rc_idx
        connects += tmp_connects
    def post_order(node):
        if lc_n[node] != -1:
            post_order(lc_n[node])
            lp[node] = tot_p[lc_n[node]]
        else:
            lp[node] = 0
        if rc_n[node] != -1:
            post_order(rc_n[node])
            rp[node] = tot_p[rc_n[node]]
        else:
            rp[node] = 0
        tot_p[node] = lp[node] + rp[node] + num[node]
    post_order(p_n.index(-1))
    cases = combinations(connects, k - 1)
    max_groups = []
    def check(datas):
        tmps = []
        logs = []
        for p, c in datas:
            if lc_n[p] == c:
                tot_p[p] -= lp[p]
                logs.append(['tot', p, 'l'])
            else:
                tot_p[p] -= rp[p]
                logs.append(['tot', p, 'r'])
            logs.append(['p_n', c, p_n[c]])
            p_n[c] = -1
        for node in range(len_node):
            if p_n[node] == -1:
                tmps.append(tot_p[node])
        for log in logs:
            if log[0] == 'tot':
                if log[2] == 'l':
                    tot_p[log[1]] += lp[log[1]]
                elif log[2] == 'r':
                    tot_p[log[1]] += rp[log[1]]
            elif log[0] == 'p_n':
                p_n[log[1]] = log[2]
        max_groups.append(max(tmps))

    for case in cases:
        check(case)
    return min(max_groups)

inputdatas = [
    [3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
     [[-1, -1], [-1, -1], [-1, -1], [-1, -1],
      [8, 5], [2, 10], [3, 0], [6, 1],
      [11, -1], [7, 4], [-1, -1], [-1, -1]]],
    [1, [6, 9, 7, 5],
     [[-1, -1], [-1, -1], [-1, 0], [2, 1]]],
    [2, [6, 9, 7, 5],
     [[-1, -1], [-1, -1], [-1, 0], [2, 1]]],
    [4, [6, 9, 7, 5],
     [[-1, -1], [-1, -1], [-1, 0], [2, 1]]],
]

"""
2021 카카오 공채 기출. Lv.5.
처음엔 트라이를 사용하려 했으나 노드의 번호들이 뒤죽박죽이라 insert 작업이 까다로웠다.
그래서 일단 배열로 트리를 만들었다.
왼쪽 서브트리, 오른쪽 서브트리, 노드 자체를 포함하는 트리의 총 인원을 노드에 기록하려 했는데
이걸 어떻게 업데이트해야 꼬이지 않을까 1시간 가량 낭비해서 1시간 13분에 도달했다.
갑자기 후위순회가 생각나서 확인해보니 그냥 후위순회 돌면 꼬이지 않고 업데이트 되길래 허무했다.
1시간 27분 쯤에 초안을 제출했고, 정확성 테스트 1~4만 통과, 실패에는 시간초과도 있었다. 
효율성 테스트는 시간초과와 런타임 에러가 섞여 있었다.
재귀 깊이를 늘려주니 런타임에러는 사라졌다.
연결부위를 체크할 때 자식이 없는 경우를 추가해주고 있던 문제를 수정했다.
정확성 테스트의 시간초과가 사라지고 8번 테케를 통과, 효율성 10번을 통과했다.
효율성은 그렇다치고 정확성은 왜 틀리는지 모르겠다.
풀이들을 살펴보니 파라메트릭 서치라는걸 사용한다. 
고난이도 문제에서만 필요한 알고리즘은 지금 나에게 필요하지 않기에 넘어간다.
"""

for t in inputdatas:
    print(solution(t[0], t[1], t[2]))
