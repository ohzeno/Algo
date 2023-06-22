# https://www.acmicpc.net/problem/16225
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline()

"""
a[i]는 내가 i번 문제를 푸는 데 자신있는 정도.
b[i]는 상대가 i번 문제를 푸는 데 자신있는 정도.
내가 2문제를 고르면 상대가 그 중 b[i]가 높은 문제를 가져가고 나머지는 내 것이 된다.
이런 전제 하에 a값 합을 최대값을 출력하라.
a와 b 각각은 원소가 모두 다르다.
"""

from heapq import heappop as hpop, heappush as hpush
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted(zip(a, b), key=lambda x: x[1])  # b를 기준으로 정렬
ans = c[0][0]  # 가장 왼쪽은 b 최소값이므로 무조건 a가 가져가게 된다.
hq = []
for i in range(1, n-1, 2):
    hpush(hq, -c[i][0])
    hpush(hq, -c[i+1][0])
    ans += -hpop(hq)
print(ans)

"""
현 시점 다이아 5. 제출 1002. 정답률 37.896%
b 점수를 기준으로 선택되므로 b를 기준으로 정렬한다.
b를 기준으로 오름차순 정렬이 되면 
가장 왼쪽은 b 최소값이므로 무조건 a가 가져가게 된다. ans를 가장 왼쪽 값으로 초기화한다.
왼쪽부터 i+2k번째까지 a가 최소한 k개를 가져가야 한다.
예를 들어 3번째까지에서 a가 0, b가 1,2를 가져가면 1, 2보다 작은 문제가 없으므로 5:5분배가 불가하다.
그러므로 i=1부터 시작해서 a값을 2개씩 큐에 넣고, a값이 높은 것 하나를 빼내서 ans에 더해준다.
이것을 반복하면 된다.

다이아 치고는 쉬운 문제. 
i+2k번째까지 a가 최소한 k개를 가져가야 한다는 규칙을 생각해내는 것이 제일 어려운 부분이다.
"""