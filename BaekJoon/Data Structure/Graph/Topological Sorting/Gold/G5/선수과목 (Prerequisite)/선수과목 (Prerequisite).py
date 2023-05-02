# https://www.acmicpc.net/problem/14567
import sys
from collections import deque
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def topological_sorting():
    q = deque()
    for i in range(1, n_course + 1):
        if not enter[i]:  # 진입차수가 0인 노드 넣기
            q.append((i, 1))
    while q:
        node, now_count = q.popleft()
        ans[node] = now_count  # 해당 과목 현재 학기 기록
        for next_node in mat[node]:  # 현재 과목이 선수과목인 과목들 탐색
            enter[next_node] -= 1  # 진입차수 줄여줌
            if enter[next_node] == 0:  # 진입차수가 0이라면 q에 넣는다. 다음 학기니 1 더해줌.
                q.append((next_node, now_count + 1))

n_course, n_pre = map(int, input().split())
mat = [[] for _ in range(n_course + 1)]  # 선수과목 정보 담을 매트릭스
enter = [0] * (n_course + 1)  # 진입차수 기록
ans = [0] * (n_course + 1)  # 몇 학기에 듣는가?
for _ in range(n_pre):
    a, b = map(int, input().split())
    mat[a].append(b)  # a가 b의 선수과목. 연결노드 탐색해야하니 a에 연결된 노드들 기록하는 형태.
    enter[b] += 1  # b 진입차수 업데이트
topological_sorting()
print(*ans[1:])



