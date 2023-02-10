# https://www.acmicpc.net/problem/22871
from collections import deque
import sys
sys.setrecursionlimit(5005)
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
n개 돌이 일렬로 나열. 1~n번. 1에서 출발하여 n으로 이동
1. 항상 오른쪽으로만 이동 가능
2. i번 돌에서 j번 돌로 이동할 때 (j-i) * (1 + |Ai - Aj|)만큼 힘을 쓴다.
3. 돌을 한 번 건너갈 때마다 쓸 수 있는 힘은 최대 K.
K의 최소값?
"""
# bfs 풀이
def cal_cost(st, ed):
    return (ed - st) * (1 + abs(datas[ed] - datas[st]))
n = int(input())
datas = list(map(int, input().split()))
ll, rr = 0, cal_cost(0, n - 1)
while ll <= rr:
    mid = (ll + rr) // 2
    q = deque([0])
    visited = [0] * n  # 매 이분탐색마다 초기화 해줘야 한다.
    while q:
        st = q.popleft()
        if st == n - 1:
            break
        for ed in range(st + 1, n):
            """
            max_k를 넘지 않는 경우만 방문처리 되므로, 
            다른 경로로 이미 방문한 코스는 다시 방문할 필요가 없다. 
            어떤 경로로든 max_k를 넘지 않고 해당 돌로 이동하면 성공이기에.
            """
            if cal_cost(st, ed) <= mid and not visited[ed]:
                visited[ed] = 1
                q.append(ed)
    if visited[-1]:
        rr = mid - 1
    else:
        ll = mid + 1
print(ll)

# dfs 풀이
# def cal_cost(st, ed):
#     return cost_dic.setdefault((st, ed), (ed - st) * (1 + abs(datas[ed] - datas[st])))
# def dfs(st, max_k):
#     if st == n - 1:
#         return 1
#     for ed in range(st + 1, n):
#         cost = cal_cost(st, ed)
#         if cost <= max_k and not visited[ed]:
#             if dfs(ed, max_k):
#                 return 1
#     return 0
# n = int(input())
# datas = list(map(int, input().split()))
# cost_dic = {}
# ll, rr = 0, cal_cost(0, n - 1)
# while ll <= rr:
#     mid = (ll + rr) // 2
#     visited = [0] * n
#     if dfs(0, mid):  # 통과되면 값 줄여보기. 이렇게 빠져나오면 ll이 마지막 통과한 최소값.
#         rr = mid - 1
#     else:  # 통과 안되면 값 늘려보기. 이렇게 빠져나오면 통과방법 없음. 즉, 이걸로 빠져나갈 일 없음.
#         ll = mid + 1
# print(ll)


"""
현 시점 실버 1. 제출 950. 정답률 31.761 %
문제 설명이 난해하다. 한 번의 이동에서 최대K를 쓸 수 있다고 하는데,
0에서 n-1까지 이동하는 모든 경우 중 k의 최소값을 구하라고 한다.

이 두 문장을 조합하면 0에서 n-1까지 이동하는 모든 경우 중 
'한 번의 이동'에서 사용하는 힘 중 최소값을 구하는게 된다.
예를 들어 코스에서 2, 3, 6을 사용했다면 2를 선택하면 된다.
'최대 K'라는 말이 각 이동에 한정되고, k가 주어지지 않았으므로 '최대'라는 말은 의미가 없다.

'한 번의 이동에서 최대 K를 쓴다'가 아니라 '한 번의 이동에서 쓰는 힘의 최대값은 K다'라고
억지로 끼워맞춰도 임의의 i에서 임의의 j로 이동하는 비용 중 최대값을 구하는게 된다.
그렇게 보면 'k의 최소값을 구해라'라는 말과 충돌한다.

한 번의 결제에 최대 x원을 쓸 수 있다. x의 최소값을 구해라. 하지만 x는 주어지지 않았다. 
이러면 x는 내가 정하는거라 '최소값'이 의미가 없다.

문제 설명이 논리적으로 문제가 있다는 것이다.

한참 헤매다 결국 정답풀이들을 보고 문제의 의도를 도출했다. 
문제에서 의도한 바는, 0에서 n-1까지 이동하는 모든 코스를 살펴보며
각 코스마다, 코스 내에서 발생한 각각의 이동에서 사용한 힘 중 최대값을 구하고,
그 코스별 최대값을 모아서 최소값을 구하는 것이다.

시간 제한 기준이 굉장히 불가사의한데, 본문의 풀이를 함수로 작성하지 않으면 시간초과가 발생한다.
함수 호출과 리턴과정에서 시간을 더 잡아먹을 것 같은데 오히려 그것만 통과하니 이상하다.
약간의 시간차이인가 싶어 여러번 제출해봤으나 결과는 같았다.
맞힌 사람 중 python3로 푼 사람이 한 사람 더 있는데, 
내 로직에서 안쪽 for루프에서 배열에 값을 추가하고
안쪽 루프가 끝나면 min을 해주는 연산을 했다.
내 로직은 안쪽 for루프에서 min연산을 매번 해주지만, 
그 사람은 append를 매번 하고, min은 루프 바깥에서 한 번만 했는데, 그 차이가 아닐까 싶다.
그 사람의 풀이는 함수를 사용하지 않았다.

본래 이분탐색을 위해 찾은 문제인데, 일단 dp가 더 편해보여 dp로 풀었다.
실버1이지만 상당히 힘들었다. 
문제 설명에 논리적 오류가 있어 언어적으로 올바르게 해석하면 오히려 문제를 풀 수 없다.
한참 헤매다가 다른 정답풀이들을 보고 문제의 의도를 도출해냈고,
의도를 알더라도 dp를 어떻게 사용해야 할 지 찾아내기 힘들었다. 골드 문제들보다 더.
처음엔 2차원 dp로 풀려고 시도하며 한참 헤맸다.

--------------------------------------
이분탐색으로도 풀어보았다.
이분탐색의 경우 max_k를 바꿔가며 dfs/bfs로 탐색하기에 시간복잡도가 더 높다.

dfs를 사용하면 python3, pypy3 모두에서 시간초과가 발생한다. 
bfs와 시간복잡도가 같은데 이러는건 여전히 이해하기 힘들다.

bfs를 사용하면 pypy3에서는 통과하나 python3에서는 시간초과가 발생한다.
max_k를 바꿀 때마다 모든 경우의 수의 k값을 다시 계산하기 때문에, 시간을 줄이려
딕셔너리에 k값을 저장해봤다. 그러나, 오히려 이렇게 메모이제이션하면 시간초과가 발생하고, 
그냥 매번 k값을 계산해줘야 시간초과가 발생하지 않는다...(dfs는 딕셔너리 없어도 시간초과)
"""
