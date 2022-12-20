# https://www.acmicpc.net/problem/11866
import sys
from collections import deque
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
요세푸스.
처음엔 인덱스만 회전시키고 리스트에서 매 원소 del연산으로 삭제한다고 고생했는데 
그냥 deque 사용하고 pop한 원소를 다시 append로 넣어서
리스트를 실제 회전 돌리는게 편했다. 분류에 왜 큐가 있나 했었는데...
다른 풀이를 보니 인덱스 회전하면서 pop(i)로 추출하는 방법이 있다고 한다. 
del data[i]나 data.pop(i)나 시간복잡도는 똑같으니
아마 내 풀이에서 조건문이 많았던게 시간초과 원인인 듯 하다.
내가 시도해봤던 인덱스 순회 공식에 포함되는게 정답코드에 있다.
리스트를 0부터 시작하는가 1부터 시작하는가, 인덱스 공식에서 뭘 나눈 나머지를 사용하는가
그런 부분에서 많이 꼬인 듯 함. 
"""
n, k = map(int, input().split())
data = deque()
for i in range(1, n + 1):
    data.append(i)

print('<', end='')
while True:
    remain = len(data)
    if remain == 1:
        print(data.popleft(), end='>')
        break
    else:
        for i in range(k):
            if i == k - 1:
                print(data.popleft(), end=', ')
            else:
                data.append(data.popleft())

