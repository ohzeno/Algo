# https://www.acmicpc.net/problem/1325
from collections import deque
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
A가 B를 신뢰하면, B를 해킹하면 A도 해킹할 수 있다.
컴퓨터들의 신뢰관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터를 출력하라.
"""
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)  # b를 해킹하면 a도 해킹할 수 있다. 역전.
ans = []
max_group = 1
for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    q = deque([i])
    group = 0  # i 해킹 시 해킹할 수 있는 총 컴퓨터 수
    while q:
        cur = q.popleft()
        group += 1
        for child in graph[cur]:
            if not visited[child]:
                """
                안에서 방문처리 해줘야 시간초과 안난다. 입력값에 중복이 있어야 성립하는 얘기고, 
                그러면 바깥에서 처리할 경우 중복때문에 group 카운팅에 오류가 생기니 틀려야 하는데...
                c++로는 바깥에서 처리해줘도 문제가 없다. 왜 안에서 해줘야 시간이 줄어드는지 모르겠다.
                """
                visited[child] = 1
                q.append(child)
    if group > max_group:
        max_group = group
        ans = [i]
    elif group == max_group:
        ans.append(i)
print(*ans)


"""
현 시점 실버1. 제출 56356. 정답률 19.697%
결론) ~~신뢰관계 입력에 중복이 있다. 이를 해결하기 위해 for문 순회 도중 방문처리를 해야한다.~~
c++ 풀이는 for문 바깥에서 방문처리를 해도 틀리지 않았다. 이제 시간 차이나는 원인을 모르겠다...
bfs, pypy3로 제출해야 통과한다. 파이썬으로는 순수 dfs로는 불가능할 확률이 매우 높다.
bfs도 for문 안쪽에서 방문처리를 해야한다. 원인은 불명.

python3: dfs, bfs 모두 시간초과
pypy3: dfs 메모리초과, bfs 통과
dfs만으로는 불가능 한 듯 하다. dfs풀이라고 주장하는 것들은 죄다 bfs였고,
python3 풀이들은 dfs와 bfs가 섞여있다.

백준의 시간/메모리제한은 언어를 많이 타던데 도대체 뭔 기준인지 모르겠다...

pypy3에서 bfs로 풀어도 시간초과가 발생했다.
정답풀이와 로직을 비교해보니, 
정답풀이는 시작지점을 popleft 이후가 아니라 while q 이전에 방문처리 했다.
BigO 상에서 시간차이가 없다. 방문처리를 하는 횟수가 똑같다.

질문탭이든 블로그든 아무도 이 점을 지적하지 않는다는게 좀 황당한데,
신뢰관계에 중복이 있을 경우 for문 내에서 방문처리를 하면 
순회 도중 visited의 효과를 받기에 더 빠를 수 있다.
그런 경우 for문 이전에 방문처리를 하면 자식노드 중복을 처리하지 못해 오류가 발생한다.
다만, '틀렸습니다'가 뜨지 않고 시간초과가 발생하기에 확신은 할 수 없다.
틀려야 할 첫 케이스에서 시간초과가 발생했다면 중복이 엄청나게 많다는 건데...
해당 경우가 아니라면 BigO가 같으므로 아주 미세한 차이로 시간초과가 발생했을 수 밖에 없다.
> c++로는 for문 바깥에서 방문처리 해도 틀리지 않았다. 
해당 로직 차이로 왜 시간차이가 발생했는지 알 수 없게 됐다.

이걸 노리고 만든거라면 실버1인 이유는 대충 때려맞춘 사람들 때문인듯.
항상 하는 말이지만 푼 사람 중 이 부분을 생각하고 푼 사람이 얼마나 있을지 심히 의심스럽다.

bfs로 풀었고, 같은 로직의 dfs는 시간초과가 발생했다.
중복에 대한 시간을 줄이기 위해 bfs, dfs에서 그래프를 만들 때 set를 사용해봤으나 효과가 없었다.
통과한 bfs코드에서 그래프를 set로 만들어도 시간초과가 발생했다. set를 만드는 데 시간이 걸렸을듯.
set를 하나만 만들고 입력값의 중복을 처리해준 경우, 
dfs는 시간/메모리 초과(python3 시간초과, pypy3 메모리초과), bfs는 pypy3로 통과했다.
재귀 과정에서 메모리를 많이 잡아먹는 듯.
"""