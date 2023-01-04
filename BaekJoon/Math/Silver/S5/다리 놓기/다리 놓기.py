# https://www.acmicpc.net/problem/1010
from math import factorial
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

# 서쪽 N개 동쪽 M개. N <= M
# 한 지점에 한 다리만 연결 가능. N개 지을거임.
# 다리는 겹쳐질 수 없음. 가능한 경우의 수?

for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = factorial(m) // (factorial(m-n) * factorial(n))  # mCm-n
    print(ans)

"""
현 시점 S5. 정답률 48.462%. 최종 제출까지 8분 걸렸다.
DP문제라고 해서 들어왔는데 DP 사용할 방법은 생각나지 않았고,
겹치지 않게 하면 동쪽에서 m-n개를 고르는 조합과 같았다.
dp풀이를 보니 사람들이 저걸 어떻게 수학적으로 증명 안하고 식을 사용하나 의아했는데
조금 더 살펴보니 결국 nCr을 다 기록한거다. nCr = n-1Cr-1 + n-1Cr 공식 이용한 것.
(그럼 dp가 아니라 결국 조합 문제 아닌가...)
dp 풀이에서 조합에 대한 언급이 있는 경우가 거의 없고 식 설명도 없는 것을 보니 
대부분의 사람은 원리도 모르고 그냥 검색해서 나온 dp식을 사용한듯.
"""