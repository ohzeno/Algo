# https://www.acmicpc.net/problem/18185
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline()

"""
i번 공장에서 Ai개 라면을 구매하려 한다.
구매 방법은 3가지다.
1. i번 공장에서 라면 하나 구매. 3원
2. i, i+1에서 각각 라면 하나씩 구매. 5원
3. i, i+1, i+2에서 각각 라면 하나씩 구매. 7원
최소 비용을 구하라.
"""
def double(i, m):
    global tot
    if not m:
        return
    for j in range(2):
        cost[i + j] -= m
    tot += m * 5

def triple(i, m):
    global tot
    if not m:
        return
    for j in range(3):
        cost[i + j] -= m
    tot += m * 7

n = int(input())
cost = list(map(int, input().split())) + [0, 0]
tot = 0
for i in range(n):
    # 한 번에 많이 구매할 수록 싸다.
    if cost[i+1] > cost[i+2]:
        """
        cost[i+1] > cost[i+2]인 경우 1211라고 하면
        트리플을 진행하면 0101이 되어 7 + 3 + 3원이 들지만
        더블을 진행하면 0111이 되어 5 + 7로 해결 가능하다.
        1210처럼 뒤에 아무것도 없어도
        5 + 5와 7 + 3은 같은 가격이므로 더블부터 진행한다.
        i+1를 다 없애버리면 i+1에서 트리플을 진행할 가능성을 없애버리므로
        dif = cost[i+1] - cost[i+2]만큼만 더블을 진행한다.
        케이스를 나눠보자.
        1. i+2가 비어있는 경우
            510: 더블 진행하면 i+1이 0이 되어 손해가 없다. 전체 min은 0이라 dif를 사용해야한다.
        2. i+2가 비어있지 않은 경우
            dif만큼 진행해야 i+1이 i+2와 같아져서 트리플 가능하다.
            1. i가 i+1보다 작은 경우
                1. dif가 i보다 큰 경우
                    142: i가 min값이라 최소한도 더블 진행. i+1에서 트리플 검토.
                2. dif가 i보다 작은 경우
                    465: dif만큼 진행해야 i+1에서 트리플 많이 가능.
        결국 다 이득이다.
        """
        double(i, min(cost[i], cost[i+1] - cost[i+2]))
        # i+1이 i+2와 같아진 상태이므로 두 값만 비교
        triple(i, min(cost[i], cost[i+1]))
    else:
        """
        i+1이 i+2와 같으면 트리플로 해결되고
        i+1이 i+2보다 작으면 i+2를 남겨놓고 i+2에서 검토
        결국 다 이득이다.
        """
        # i+1이 i+2보다 작거나 같은 상태이므로 i+1만 비교하면 된다.
        triple(i, min(cost[i], cost[i+1]))
        # 값이 업데이트 됐으므로 다시 계산한다.
        double(i, min(cost[i], cost[i+1]))
    tot += cost[i] * 3  # 남은 싱글 구매
print(tot)


"""
현 시점 다이아 5. 제출 6419. 정답률 30.432%
케이스 나누기가 까다로운 문제.
코드는 짧은데 검토할 것이 많아서 주석이 길다.
다이아 치고는 쉽다.
"""