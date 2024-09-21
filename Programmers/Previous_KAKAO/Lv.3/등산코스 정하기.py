# https://school.programmers.co.kr/learn/courses/30/lessons/118669
import sys
from heapq import heappush
sys.setrecursionlimit(10**5)
def solution(n, paths, gates, summits):
    # n개 지점. 각 1~n 번호 붙어있음. 출입구/쉼터/산봉우리 중 하나
    # 양방향 통행 가능한 등산로. 등산로마다 이동시간 있음
    # 등산코스 중 쉼터/산봉우리 방문 때마다 휴식 가능.
    # 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 코스의 intensity라 부름.
    # 출입구 중 한 곳에서 출발, 산봉우리 중 한 곳만 방문 후 돌아오는 등산코스
    # 이런 규칙 하에 intensity 최소 되도록 등산코스 정하기.
    # gates: 출입구들,    summits: 산봉우리들
    # intensity가 최소인 등산코스 중 산봉우리 번호가 가장 낮은 등산코스
    # 의 [산봉우리 번호, 강도 최소값] 리턴
    # n은 2~5만,    paths 길이: (n-1)~20만
    # paths 원소 [i, j, w] i에서 j로 통하는 등산로 시간 w.
    # 1 <= i < j <= n,    w: 1~1천만
    # gates 길이: 1~n    gates원소: 1~n
    # summits 길이: 1~n    summits원소: 1~n
    # gates, summits에 등장하지 않은 모든 지점은 쉼터.
    # 임의의 두 지점 사이 이동 가능한 경로 항상 존재.
    def dfs(cur, cw):  # 현재 노드, 현재 코스 강도
        if cur in set_summits:  # 봉우리 도착하면
            if cw < max_w[0]:  # 최저강도 갱신 후 리턴
                max_w[0] = cw
            return
        for tw, ncur in connect[cur]:  # 연결 노드 순회
            if not visited[ncur]:  # 방문한 적 없는 노드만
                nw = max(cw, tw)  # 코스강도 갱신
                # 기록된 노드 최소강도보다 낮고, 코스 최저강도보다 낮거나 같은 경우만
                # 코스 최저강도가 같아도 낮은 봉우리가 우선이므로 = 넣어서 다 찾아야함.
                if nw < min_w[ncur] and nw <= max_w[0]:
                    min_w[ncur] = nw  # 노드 최저강도 갱신
                    visited[ncur] = 1  # 방문처리
                    dfs(ncur, nw)  # 재귀
                    visited[ncur] = 0  # 비방문처리
    max_w = [float('inf')]  # 코스의 최대 강도들 중 최소인 값 기록
    min_w = [float('inf') for _ in range(n + 1)]  # 현 노드까지 오는 코스들 중 최소 강도
    connect = [[] for _ in range(n + 1)]  # 연결노드 기록
    set_gate, set_summits = map(set, (gates, summits))  # in연산 시간단축 위해 set사용
    for i, j, w in paths:  # 게이트로 돌아오는 길은 기록X
        # 봉우리에서 내려오는 길은 안없애도 됨. dfs에서 봉우리 도착하면 끝이라.
        if j not in set_gate:
            heappush(connect[i], (w, j))  # min_w 최적화 빠르게 가중치 낮은 순로 정렬
        if i not in set_gate:
            heappush(connect[j], (w, i))
    visited = [0] * (n + 1)
    for gate in gates:  # 게이트로 향하는 길 기록 안해놔서 게이트 방문처리 안해도 됨.
        min_w[gate] = 0  # 게이트들은 비용 0
        dfs(gate, 0)  # 모든 게이트에서 dfs
    min_top = -1  # 강도 최저인 봉우리
    t_cost = float('inf')  # 그 코스 강도
    for summit in sorted(summits):  # 강도 같으면 낮은 봉우리가 우선이므로 오름차순
        if min_w[summit] < t_cost:  # 강도 최저인 봉우리 기록
            min_top = summit
            t_cost = min_w[summit]
    return [min_top, t_cost]

inputdatas = [
    [6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]],
    [7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]],
    [7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]],
    [5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]],
]

"""
2022 카카오 테크 인턴십 기출. Lv.3. 현 시점 완료한 사람 1155명, 정답률 22%
42분 dfs 초안 제출, 테케 13~25 시간초과
52분 개선안 제출, 테케 22 추가 통과
53분 수정안 제출, 테케 20 추가 통과
54분 수정안 제출, 테케 13, 14 추가 통과, 22 다시 시간초과
55분 수정안 제출, 13, 14, 22 다시 시간초과
56분 수정안 제출, 변화X
bfs 풀이는 통과하고 dfs는 통과하지 못하는 이유를 고민해봤다.
둘 다 모든 케이스들을 순회하지만 가지치기에서 차이가 나고 있었고
bfs의 경우는 summit마다 gate를 다시 보지 않았다.
gate는 한 번만 하고 산봉우리에 도착하면 체크하도록 수정했다.
bfs 경우는 코스와 상관없이 같은 노드에서는 현 코스 가중치가 최소인 경우만 통과시켰다.
dfs에도 적용해봤다.
86분 해당 코드 제출. 테케 19만 시간초과.
bfs와 차이가 날만한 부분이 
set(gates), visited = [0] * (n + 1), 방문처리, 비방문처리, if문 2개
정도밖에 없다. 고작해야 n 1차계수 정도라 시간복잡도에 영향을 줄만한 부분은 아니다.
bfs의 경우 min_w가 빠르게 최적화되는 편이고, dfs의 경우에는 max_w가 빠르게 최적화된다.
가중치 중 높은 값이 gate쪽에 몰려있다면 max_w가 별 의미가 없기에 dfs가 bfs에 비해 효율이 안좋을 것이고
summit쪽에 몰려있다면 dfs의 효율이 올라갈 것이다.
gate의 수가 많을 경우 t_cost가 빠르게 최적화되는 bfs의 효율이 올라간다.
실제 bfs 실행시간과 dfs 실행시간에 큰 차이가 없다. 
가중치 중 높은 값이 gate쪽에 몰려있어 max_w가 힘을 쓰지 못하는 케이스라고 생각된다.
connect에서 가중치 낮은 순으로 정렬하고 제출. 테케 19 통과, 21 시간초과
테케 19   n: 400      len(paths): 79799   len(gates): 1   len(summits): 1
테케 21   n: 50000    len(paths): 149985  len(gates): 1   len(summits): 1
정렬에 시간이 소모된 것 같아 sort 대신 heappush 사용. 통과.

결론: 
dfs로는 못 푼다는 말이 많았는데 역시나 그냥 그 사람들이 못 푼 거였다.
찾아보면 대부분이 다익스트라/BFS 풀이이다. 그마저도 풀이가 비슷하고 해설도 똑같기에 대부분은 그냥 복붙일 것이다. 
프로그래머스 풀이 목록에서 dfs가 사용된 풀이를 둘 찾았는데, 한 명은 이분탐색을 사용했고, 한 명은 유니온파인드를 사용했다. 
이분탐색의 경우 코스 최저강도를 이분탐색으로 임의 지정해가며 dfs로 탐색하여 시간을 단축했고
유니온 파인드의 경우 dfs 전에 부모를 통일시킨다. 
양방향 그래프에서 부모라는게 무슨 의미인지 이해가 안돼서 원리 파악은 못했다. 
게이트나 봉우리가 부모인 것도 아니어서 임의로 부모를 정하고 통일시켰는데 어떻게 최저강도가 찾아지는지는 모르겠다...
카카오 해설에서는 다익스트라를 사용하라고 했고, 모든 gate에 대해 다익스트라를 사용하면 시간초과가 발생한다고 했다.
여러 방법으로 최적화하고 모든 gate에 대해 dfs를 사용하는 풀이로 통과했다.
프로그래머스 풀이 전체를 둘러봤지만 순수한 dfs로 푼 사람은 내가 유일하다.
다음날 마저 풀어 통과했기에 실제 코테에서는 못 풀었을 듯싶다.
p.s. Lv.4가 맞지 않나...
"""

for t in inputdatas:
    print(solution(t[0], t[1], t[2], t[3]))
