# https://school.programmers.co.kr/learn/courses/30/lessons/92343
def solution(info, edges):
    # 이진트리 모양 초원 노드에 양, 늑대가 있음.
    # 루트 노드(항상 양이 있음)에서 출발하여 양을 모으려 함. 각 노드 방문하면 해당 노드 동물이 따라옴.
    # 늑대는 양을 잡아먹을 기회를 노림. 늑대 수가 양의 수 이상이 되면 모든 양을 잡아먹음.
    # info: 각 노드 동물 정보, edges: 노드 연결 관계
    # 모을 수 있는 양 최대 몇 마리인지 return
    # info는 2~17 길이. 0은 양, 1은 늑대.
    # edges의 원소는 [부모 노드, 자식 노드]
    def dfs(cur_node, sheep, wolves, can_visit):
        if sheep == num_sheep[0]:  # 총 양 수를 달성했으면 더 돌 이유 없음
            return
        if info[cur_node] == 0:  # 현 노드 동물 수집
            sheep += 1
        elif info[cur_node] == 1:
            wolves += 1
        if sheep <= wolves:  # 양 잡아먹히면 리턴
            return
        if sheep > max_sheep[0]:  # 잡아먹히지 않았고, 기존 기록 넘으면 최대 양 갱신
            max_sheep[0] = sheep
        can_visit.remove(cur_node)  # 방문 가능 목록에서 현 노드 제거
        for child in childs[cur_node]:  # 현 노드의 자식 노드 방문 가능 목록에 추가
            can_visit.append(child)
        for node in can_visit:  # 방문 가능한 목록 각각에 dfs
            dfs(node, sheep, wolves, can_visit.copy())  # can_visit을 넘겨주면 같은 주소값을 가리킴.

    max_sheep = [0]  # 최대값 기록
    num_sheep = [info.count(0)]  # 총 양 수
    childs = {i: [] for i in range(len(info))}  # 자식 노드 기록
    for p, c in edges:
        childs[p].append(c)
    dfs(0, 0, 0, [0])
    return max_sheep[0]

inputdatas = [
    [[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
     [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]],
    [[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
     [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]],
]

"""
2022 카카오 공채 기출. Lv.3. 현 시점 프로그래머스 정답률 32%. 옮겨적기부터 채점까지 53분 가량 걸렸다.
처음에는 현 노드에서 부모, 자식 중 이동할 방향을 정하려고 했다. 
하지만 그러면 순환루트가 발생할 것이고, 그걸 해결할 방법이 생각나지 않았다.
다시 생각해보니 굳이 위로 가서 다른 노드로 옮겨갈 필요가 없었다. 
이미 방문한 곳들 중 끝 부분들의 한 단계 내려간 자손만 can_visit에 넣어줬다.
이 아이디어를 생각해낸 후에는 5분도 안돼서 구현과 검증을 끝냈다. 괜히 어렵게 생각하느라 시간을 낭비했다.
5분이나 걸린 이유 중 하나가, 함수의 인자로 리스트를 넘겼는데, 
주소값이 같아서 재귀하며 모든 함수가 같은 리스트를 참조해서 수정해서 문제가 생겼다.
리스트 안쪽에 객체가 더 있는건 아니라 copy로 넘겨줘서 해결했다.
처음에 parent 배열을 만들었었는데 자손만 체크하게 되어 필요없어져 자식dict로 변경했다.
"""

for t in inputdatas:
    print(solution(t[0], t[1]))
