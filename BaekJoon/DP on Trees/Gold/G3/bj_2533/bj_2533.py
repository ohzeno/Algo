# https://www.acmicpc.net/problem/2533
import sys
sys.stdin = open('input.txt')
# 최대 10^6개의 노드가 주어지므로 그래프의 최대깊이도 그만큼이다.
# count_node는 리프노드에서 한 번 더 들어가므로 +1이 필요하다.
sys.setrecursionlimit(10**6 + 1)
def input():
    return sys.stdin.readline().rstrip()

n_node = int(input())
# 딕셔너리를 사용하면 메모리초과가 떠서 리스트를 사용했다.
"""
딕셔너리는 모든 키값에 대한 포인터를 저장하고 있고
~~리스트는 인덱스 0에 대한 포인터만 저장하고 있다.
리스트는 미리 메모리를 할당해놓아 메모리낭비가 있긴 하지만 이 경우
딕셔너리의 포인터의 용량으로 인한 오버헤드가 더 컸던 것으로 추정한다.~~
"""
# 그렇게 추정했었으나 포인터 하나만 저장하는건 array의 경우고
# 파이썬 리스트는 다양한 자료형을 넣을 수 있기에 랜덤엑세스가 불가하다.
# 파이썬 리스트는 모든 인덱스의 포인터를 따로 저장하고 있다.
# 결국 딕셔너리가 메모리를 더 많이 필요로 하는 명확한 이유는 찾지 못했다.
connect = [[] for _ in range(n_node + 1)]
# connect = {}
# for i in range(1, n_node + 1):
#     connect[i] = []
for _ in range(n_node - 1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)
visited = [0] * (n_node + 1)
# 각 [0, 0]의 앞쪽은 해당 인덱스가 얼리어답터가 아닐 경우의 서브트리 전체의 얼리어답터 수
# 뒤쪽은 해당 인덱스가 얼리어답터일 경우의 서브트리 전체의 얼리어답터 수
dp = [[0, 0] for _ in range(n_node + 1)]

def solution(parent):
    # connect는 부모자식 상관없이 연결된 노드를 다 표시한다.
    # 그러므로 visited를 이용해 부모 노드를 다시 탐색하지 않도록 한다.
    visited[parent] = 1
    dp[parent][0] = 0  # parent(현재 노드)가 얼리어답터가 아니면 0개로 시작
    dp[parent][1] = 1  # parent(현재 노드)가 얼리어답터이면 얼리어답터 수는 1개로 시작
    # 리프노드의 connect[parent]에는 부모노드만 기록되어 있다.
    # 부모노드는 방문처리 되어있으므로 dp[parent][1] = 1로 고정되고 부모노드쪽의 재귀로 돌아간다.
    # 그렇게 부모노드측 재귀에서 리프노드측의 얼리어답터수를 더하게 된다.
    for child in connect[parent]:  # 현재 노드와 연결된 노드들 탐색
        if not visited[child]:  # 부모노드 제외하고 자식노드만 탐색
            solution(child)  # 리프노드까지 들어가게 될 것이다.
            # 현재 노드가 얼리어답터가 아니라면 자식노드가 얼리어답터여야 하므로
            # 자식 노드가 얼리어답터일 경우의 서브트리 얼리어답터 수를 더해준다.
            dp[parent][0] += dp[child][1]
            # 현재 노드가 얼리어답터인 경우 자식 노드는 어느쪽이든 상관없다.
            # 최소값을 더해준다.
            dp[parent][1] += min(dp[child][0], dp[child][1])
solution(1)
# solution 함수를 거친 후
# dp[1][0]에는 1번 노드가 얼리어답터가 아닌 경우
# dp[1][1]에는 1번 노드가 얼리어답터인 경우의
# 전체 트리 얼리어답터 수가 기록된다. 그 중 작은 값을 출력한다.
print(min(dp[1][0], dp[1][1]))


