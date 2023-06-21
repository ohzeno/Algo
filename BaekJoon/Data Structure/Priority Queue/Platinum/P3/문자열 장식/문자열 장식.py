# https://www.acmicpc.net/problem/1294
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
단어 N개를 이용해 문자열 W를 만들려 한다. 
각 단어를 적절히 쪼갠 후 이어붙인다. 
단, 한 문자열을 쪼개서 나온 조각의 순서는 유지한다.
만들 수 있는 문자열 중 가장 앞서는 것을 출력하시오.
"""
from heapq import heappop as hpop, heappush as hpush, heapify
hq = [input() + '[' for _ in range(int(input()))]
heapify(hq)
while hq:
    cur = hpop(hq)
    print(cur[0], end='')
    if cur[1] != '[':
        hpush(hq, cur[1:])

"""
현 시점 플래 3. 제출 1730. 정답률 20.403%
보자 마자 우선순위 큐를 사용한 풀이를 5분도 안되어 작성하고 제출했으나 틀렸다.
예외를 찾아봤다.
BC, CB에서 BC의 B가 뽑히고, 이후 C가 CB보다 빨라서 CB 순으로 뽑힌다.
BCBC가 되어야 한다.
BAA, BA에서 BA가 큐 앞쪽에 와서 BABAA가 된다.
BAABA가 되어야 빠르다. 
어느 문제인지는 기억나지 않는데 비슷한 예외가 기억나서 비슷한 방법을 사용했다.
문자 뒤에 chr(ord('Z')+1)인 '['를 붙여서 BA가 BAA보다 뒤로 오게 했다.

분류 태그에 우선순위큐가 왜 빠졌는지 모르겠다.

그리고 최적화를 해보니 이 문제의 경우 단어가 최대 1000자라
list(input()), cur.pop(0)을 사용하지 않고 
문자열을 그대로 사용하고 push 때는 슬라이싱을 사용했다.
슬라이싱이 들어갔음에도 훨씬 빨라져서 

파이썬 풀이 시간순 2등과 20ms의 차이를 벌리며 1위가 됐다.
숏코딩은 4위인데, 내 위의 코드들은 다 난독화 한 코드라
가독성을 유지하는 코드 중 내 코드가 가장 짧다.
"""