# https://www.acmicpc.net/problem/16953
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
- 2를 곱한다.
- 1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더해 출력하라.
만들 수 없는 경우 -1 출력
"""
from collections import deque
a, b = map(int, input().split())
q = deque()
q.append((a, 0))
suc = 0
while q:
    cur, cnt = q.popleft()
    if cur == b:
        print(cnt + 1)
        suc = 1
        break
    if cur * 2 <= b:
        q.append((cur * 2, cnt + 1))
    tmp = int(str(cur) + '1')
    if tmp <= b:
        q.append((tmp, cnt + 1))
if not suc:
    print(-1)



"""
현 시점 실버2. 제출 33425, 정답률 40.014%
설명 보고 이전에 dp로 풀었던 비슷한 문제가 생각났다(1만들기).
하지만 여러 케이스가 주어지는 경우가 아니라 그냥 bfs가 편해보여 bfs로 풀었다.
"""