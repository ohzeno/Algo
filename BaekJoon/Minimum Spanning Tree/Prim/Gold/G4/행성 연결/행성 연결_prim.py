# https://www.acmicpc.net/problem/16398
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def prim():
    total_cost = 0
    mst = [0] * n_stars  # mst 포함여부
    dist = [float('inf')] * n_stars  # 각 노드에서 mst로 이어지는 최소 비용
    dist[0] = 0
    for _ in range(n_stars):  # 노드 n_stars만큼 선택
        min_cost = float('inf')
        idx = -1
        for i in range(n_stars):  # mst 포함 안된 노드 중 최소비용 노드 찾기
            if not mst[i] and dist[i] < min_cost:
                min_cost = dist[i]
                idx = i
        total_cost += min_cost
        mst[idx] = 1
        for i in range(n_stars):  # dist: 각 노드에서 mst로 이어지는 최소 비용
            # mst에 새로 추가된 노드와 각 노드의 연결비용이, 기존 mst와의 연결비용보다 낮으면 갱신
            if not mst[i] and mat[idx][i] < dist[i]:
                dist[i] = mat[idx][i]
    return total_cost

"""
크루스칼이 소모시간이 크길래 프림을 테스트해봤다.
처음에 mst를 set로 구현하고 각 연결노드를 heapq를 사용하여 최소비용순으로 정보를 넣었다.
최소비용을 for문으로 찾는 시간복잡도를 줄이기 위해 heapq를 사용한 것이나,
연결 노드 정보들을 일일이 heappush로 넣다보니 (n-1)n^2 logn이 되어 n^3 이상의 시간복잡도가 되었다.
그런 이유로 오히려 크루스칼보다 시간초과가 심하여 여러 변형을 거쳤다.
현 방법 직전에는 mat은 그대로 받은 후 mst를 set로, 최소값 찾기는 for문을 사용했다.
현 방법에서는 mst 연결비용 리스트를 따로 두고 갱신을 추가된 노드에 대해서만 하므로 for문 안은 2n이지만
직전 방법에서는 mst 노드들마다 연결비용을 매번 체크했으므로 mst에 노드가 늘어나면 while문 안이 n(n-1)이 되었다. 
현 방법의 for문과 직전 방법의 while문 모두 n번 반복하게 되어있으므로 안쪽의 시간복잡도가 문제였던 듯 하다.
"""

n_stars = int(input())
mat = [list(map(int, input().split())) for _ in range(n_stars)]
print(prim())

