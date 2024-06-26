# https://www.acmicpc.net/problem/15824
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
메뉴들의 스코빌 지수가 있을 때 그 최댓값과 최솟값의 차이를 "주헌고통지수"라고 정의한다.
주헌이는 까다로워서 한 번 먹어본 조합은 다시 먹지 않는다.
음식점의 모든 조합을 먹어 볼 때 주헌이가 즐길 수 있는 주헌고통지수의 합을 구해보자.
0 <= 스코빌 지수 <= 2^31-1
1 <= n <= 3 * 10^5
모든 조합의 주헌고통지수 합을 1e9+7로 나눈 나머지를 출력한다.
"""
from functools import cache
n = int(input())
menus = sorted(map(int, input().split()))
MOD = 10**9 + 7
ans = 0
# @cache
# def pow2(x, y):  # O(log n)인데 856ms ?
#     if y == 0:
#         return 1
#     if y % 2:
#         return pow2(x, y-1) * x % MOD
#     return pow2(x, y//2) ** 2 % MOD
# for i in range(n-1, -1, -1):  # 큰 제곱수부터 계산해서 미리 작은 값 캐싱
#     ans += menus[i] * (pow2(2, i) - pow2(2, n-i-1))
#     ans %= MOD
pow2 = [0] * n
pow2[0] = 1
for i in range(1, n):  # O(n)인데 260ms ??
    pow2[i] = pow2[i-1] * 2 % MOD
for i in range(n):
    ans += menus[i] * (pow2[i] - pow2[n-i-1])
    ans %= MOD
print(ans)


"""
현 시점 골드 2. 제출 6856. 정답률 27.850 %
좀 많이 까다로운 문제. 최적화 두 번을 거쳐야 한다.

첫 번째 최적화는 주헌고통지수 합을 구하는 과정이다.
스코빌지수를 S배열이라고 하고, 모든 i에 대해 
S[i]가 최대값인 경우의 수를 M[i],
S[i]가 최소값인 경우의 수를 m[i]이라고 하자.
최대값 인덱스를 j, 최소값 인덱스를 i라고 하면 전체 합은
모든 j, i에 대해 S[j] * M[j] - S[i] * m[i]이다.
S[i]가 최대값인 경우의 수가 0이면 M[i]가 0이고, 최소인 경우도 마찬가지다. 
그럼 각 i에 대해 정리할 수 있다.
sigma S[i]M[i] - S[i]m[i] = sigma S[i](M[i] - m[i])
이 경우의 수는 2진수나 2의 제곱수를 이용할 수 있다. 이를 위해 S를 정렬했다.
인덱스 i인 원소가 최대값인 경우의 수는, 선택된 원소의 범위가 i까지인 경우다.
i는 무조건 선택되어야 하므로, 
0~i-1까지의 원소들(i개)을 선택하거나, 선택하지 않는 경우의 수를 합해야 한다.
즉, M[i] = 2^i이다.
인덱스 i인 원소가 최소값인 경우의 수는, 
반대로 i+1~n-1까지의 원소들을 선택하거나, 선택하지 않는 경우의 수를 합해야 한다.
즉, m[i] = 2^(n-1 - (i+1) + 1) = 2^(n-i-1)이다.
따라서, 모든 i에 대해
sigma S[i](M[i] - m[i]) = sigma S[i](2^i - 2^(n-i-1))
여기까지가 첫 번째 최적화다.

두 번째 최적화는 2의 제곱수 계산을 최적화 하는 것이다.
이 부분이 좀 요상한데,
나는 처음에 분할정복을 이용한 거듭제곱을 이용한 재귀함수를 만들고 캐싱했다.
그리고 큰 제곱수부터 계산해서 나머지는 전부 캐싱으로 해결되게 만들었다.
이론상 O(log n)이다.
그런데, O(n)인 제곱수 배열 만들기가 3배 이상 빨랐다.
이론상으로는 n이 크면 클수록 재귀함수가 압도적으로 더 빨라야 한다.
아무래도 함수 호출 오버헤드가 좀 심한가 보다. 스택 생성 때문일까? 모르겠다.
"""