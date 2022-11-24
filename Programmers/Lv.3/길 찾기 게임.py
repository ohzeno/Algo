# https://school.programmers.co.kr/learn/courses/30/lessons/42892
import sys
sys.setrecursionlimit(10**4)  # 깊이 1000 이하이므로 1만이면 충분
def solution(nodeinfo):
    # 트리를 구성하는 모든 노드의 x, y 좌표 값은 정수
    # 모든 노드는 서로 다른 x값을 가짐
    # 같은 레벨에 있는 노드는 같은 y좌표를 가짐
    # 자식 노드의 y값은 항상 부모 노드보다 작다.
    # 임의의 노드 V의 왼쪽 서브트리에 있는 모든 x값은 V의 x값보다 작다
    # 오른쪽 서브트리는 큼
    # 한 팀은 전위순회 다른 팀은 후위순회
    # 전위, 후위 순회 결과를 2차원 배열에 순서대로 담아 리턴
    # nodeinfo는 1~1만 길이. nodeinfo[i]는 i + 1번 노드.
    # [x, y] 각 노드 좌표값은 0~10만
    # 트리 깊이는 1000 이하
    node_len = len(nodeinfo)
    # 노드 번호 기록
    node_num = [[nodeinfo[i][0], nodeinfo[i][1], i + 1] for i in range(node_len)]
    # 최고 높이 찾기 위해 정렬
    node_num = sorted(node_num, key=lambda x: x[1], reverse=True)
    parent = [-1] * (node_len + 1)
    lchild = [-1] * (node_len + 1)
    rchild = [-1] * (node_len + 1)

    def sub(nodes):  # 서브트리로 부모/자식 기록하는 함수
        mid = nodes[0]  # 이미 정렬 돼있으니 루트노드임.
        l_tree = sorted(
            list(filter(lambda x: x[0] < mid[0], nodes)),
            key=lambda x: x[1], reverse=True
        )  # 왼쪽 서브트리
        if l_tree:  # 서브트리가 존재하면 좌자식, 부모 기록 후 재귀
            lchild[mid[2]] = l_tree[0][2]
            parent[l_tree[0][2]] = mid[2]
            sub(l_tree)
        r_tree = sorted(
            list(filter(lambda x: x[0] > mid[0], nodes)),
            key=lambda x: x[1], reverse=True
        )  # 오른쪽 서브트리
        if r_tree:  # 서브트리가 존재하면 우자식, 부모 기록 후 재귀
            rchild[mid[2]] = r_tree[0][2]
            parent[r_tree[0][2]] = mid[2]
            sub(r_tree)

    sub(node_num)  # 부모/자식 기록

    def pre_order(node):  # 전위 순회
        # V -> L -> R
        answer[0].append(node)  # V
        if lchild[node] != -1:  # L
            pre_order(lchild[node])
        if rchild[node] != -1:  # R
            pre_order(rchild[node])

    def post_order(node):  # 후위 순회
        if lchild[node] != -1:  # L
            post_order(lchild[node])
        if rchild[node] != -1:  # R
            post_order(rchild[node])
        answer[1].append(node)  # V

    answer = [[], []]
    pre_order(node_num[0][2])
    post_order(node_num[0][2])
    return answer

inputdatas = [
    [[5, 3], [11, 5], [13, 3],
     [3, 5], [6, 1], [1, 3],
     [8, 6], [7, 2], [2, 2]],
]

"""
2019 카카오 공채 기출. Lv.3. 옮겨적기부터 채점까지 1시간 39분 걸렸다.
무작위 노드를 받아서 부모/자식 기록하는 방식을 기억해둬야 할 듯 하다.
1시간 37분 걸려서 초기 제출안을 만들었다.
처음에는 노드를 순회하면서 부모, 좌자식, 우자식을 기록하는 방법을 찾다가 까다로워서
왼쪽, 오른쪽 서브트리를 따로 만들어 순회하는 것을 시도했고, 
다행히 메모리, 시간 초과 없이 부모/자식 배열을 기록했다.
(sorted, filter 남발했는데 통과하니까 오히려 어색하다...)
그 후 전위, 후위 순회를 시도했는데 테케 6, 7에서 런타임 에러가 발생했다.
알고보니 재귀 제한 해제 코드를 제출하지 않았었다...
"""
for t in inputdatas:
    print(solution(t))
