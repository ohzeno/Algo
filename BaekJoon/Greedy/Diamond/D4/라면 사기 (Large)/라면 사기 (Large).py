# https://www.acmicpc.net/problem/18186
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline()

"""
i번 공장에서 Ai개 라면을 구매하려 한다.
구매 방법은 3가지다.
1. i번 공장에서 라면 하나 구매. b원
2. i, i+1에서 각각 라면 하나씩 구매. b+c원
3. i, i+1, i+2에서 각각 라면 하나씩 구매. b+2c원
최소 비용을 구하라.
"""
def double(i, m):
    global tot
    if not m:
        return
    for j in range(2):
        cost[i + j] -= m
    tot += m * c1

def triple(i, m):
    global tot
    if not m:
        return
    for j in range(3):
        cost[i + j] -= m
    tot += m * c2

n, b, c = map(int, input().split())
cost = list(map(int, input().split())) + [0, 0]
if b <= c:  # b가 c보다 작거나 같으면 싱글로 다 구매하는게 최소값이다.
    print(sum(cost) * b)
else:
    c1, c2 = b + c, b + 2 * c
    tot = 0
    for i in range(n):
        if cost[i+1] > cost[i+2]:
            double(i, min(cost[i], cost[i+1] - cost[i+2]))
            # i+1이 i+2와 같아진 상태이므로 두 값만 비교
            triple(i, min(cost[i], cost[i+1]))
        else:
            # i+1이 i+2보다 작거나 같은 상태이므로 i+1만 비교하면 된다.
            triple(i, min(cost[i], cost[i+1]))
            # 값이 업데이트 됐으므로 다시 계산한다.
            double(i, min(cost[i], cost[i+1]))
        tot += cost[i] * b  # 남은 싱글 구매
    print(tot)


"""
현 시점 다이아 4. 제출 3043. 정답률 30.118%
라면 사기 (Small)에서 가격만 달라졌다.
b == c면 싱글로 다 구매하는 것과 더블/트리플의 가격효율이 같고
b < c면 싱글로 다 구매하는게 최소값이다.
더블로 사면 b+c, 싱글로 두번 사면 2b인데 b<c이면 2b < b+c다.
트리플도 마찬가지. b < c, 2b < 2c, 3b < b + 2c
"""