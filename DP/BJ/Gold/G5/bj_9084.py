# https://www.acmicpc.net/problem/9084
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    price = int(input())
    dp = [0] * (price + 1)
    dp[0] = 1  # 0을 만드는 경우의 수는 1
    for coin in coins:
        for i in range(coin, price + 1):
            """
            1. 기존 dp[i]는 현재 코인을 제외하고 i원을 만드는 경우의 수.
            2. 현재 코인을 포함해서 추가된 경우의 수는 dp[i - coin]와 같다. 
            i-coin의 경우의 수에 각각 coin원만 추가한 거니 경우의 수가 달라지지 않음.
            1과 2를 더한 경우의 수가 새로운 최종 경우의 수임.
            """
            dp[i] += dp[i - coin]
    print(dp[price])


