# https://www.acmicpc.net/problem/11047
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n종류 동전으로 k원을 만들기 위해 필요한 동전 개수의 최솟값을 구하라
"""

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = reversed(coins)
cnt = 0
for coin in coins:
    cnt += k // coin
    k %= coin
print(cnt)

"""
현 시점 실버4. 제출 111598, 정답률 51.929%
처음에 bfs, dfs를 사용하지 않고 이걸 어떻게 제한시간 안에 푸나 고민했다.
실버4치고는 조건이 까다롭다 생각했다.
그런데 조건에 Ai = 1이고 i가 2 이상이면 ai가 ai-1의 배수라는 조건이 있었다.
그렇게 되면 무조건 큰 동전부터 세는, 흔한 동전세기 예제문제와 같다.
"""