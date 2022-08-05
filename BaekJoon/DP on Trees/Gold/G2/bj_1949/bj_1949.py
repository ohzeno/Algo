# https://www.acmicpc.net/problem/1949
import sys
sys.stdin = open('input.txt')
# 최대 10^4개의 노드가 주어지므로 그래프의 최대깊이도 그만큼이다.
# count_node는 리프노드에서 한 번 더 들어가므로 +1이 필요하다.
# setrecursionlimit(n)은 첫 함수블럭을 1이라 하면 n - 4깊이까지 들어가므로 4를 더해주는게 좋다.
sys.setrecursionlimit(10**4 + 4)
def input():
    return sys.stdin.readline().rstrip()

n_node = int(input())
people = [0] + list(map(int, input().split()))
connect = [[] for _ in range(n_node + 1)]
visited = [0] * (n_node + 1)
for _ in range(n_node - 1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)
# 각 [0, 0]의 앞쪽은 해당 인덱스가 우수 마을이 아닐 경우의 서브트리 전체의 우수 마을 인구 수
# 뒤쪽은 해당 인덱스가 우수 마을일 경우의 서브트리 전체의 우수 마을 인구 수
dp = [[0, 0] for _ in range(n_node + 1)]
def solution(parent):
    visited[parent] = 1
    dp[parent][0] = 0  # 현재 노드가 우수 마을이 아닐 경우 인구 0
    dp[parent][1] = people[parent]  # 현재 노드가 우수 마을일 경우 현 마을 인구로 시작
    for child in connect[parent]:  # 현재 노드와 연결된 노드들 탐색
        if not visited[child]:  # 부모노드 제외하고 자식노드만 탐색
            solution(child)  # 리프노드까지 들어가게 될 것이다.
            # 현재 노드가 우수 마을이 아니더라도 자식 노드가 반드시 우수 마을일 필요는 없다.
            # 연결 된 하나의 노드만 우수 마을이면 됨.
            """
            물론 이 로직으로 진행할 경우 인구 수를 생각 안하면 모든 노드가 
            우수 마을이 아니게 될 수 있는 것 처럼 보인다
            (최소 하나의 우수 마을이 연결되어야 한다는 부분을 체크하지 않음.).
            하지만 1. '우수 마을'로 선정된 마을 주민 수의 총 합을 최대로 해야 한다.
            에서 생각해보자.
            특정 노드 n이 규칙 3을 위반하여 어느 우수 마을과도 연결되어 있지 않다고 가정해보자.
            그리고 마을 주민 수는 10,000 이하의 자연수이므로 0보다 크다.
            n은 어느 우수 마을과도 연결되어 있지 않으므로 추가로 우수 마을로 선택할 수 있고,
            그러면 무조건 현재보다 우수 마을 인구 수가 커진다.
            그렇다면 n을 선택하는 것이 최적해가 된다.
            즉, 3을 만족하지 않으면서 1을 만족할 수는 없다.
            본 풀이에서는 최소 하나의 우수 마을이 연결되어야 한다는 부분을 체크하지 않지만
            1번 규칙을 만족하도록 작성되어 있으므로 3은 자동으로 만족된다.            
            """
            dp[parent][0] += max(dp[child][0], dp[child][1])
            # 현재 노드가 우수 마을일 경우 자식 노드는 무조건 우수 마을이 아니어야 한다.
            dp[parent][1] += dp[child][0]

solution(1)
print(max(dp[1][0], dp[1][1]))