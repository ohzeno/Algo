# https://www.acmicpc.net/problem/2512
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
1. 모든 요청이 배정될 수 있는 경우 요청금액 그대로 배정
2. 불가할 경우 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액 배정.
가능한 최대 예산 배정하고 그 중 최대값 출력.
"""
n = int(input())
datas = list(map(int, input().split()))  # 예산 요청
total = int(input())  # 총 예산
if sum(datas) <= total:  # 총 예산보다 작으면 그대로 배정
    print(max(datas))
else:
    ll, rr = 0, max(datas) - 1  # 최대값보다 줄여야하니 -1
    # ll < rr을 사용할 경우, 마지막에 ll, rr을 증감 여부에 따라 상한액이 어느쪽인지 일관되지 않다.
    while ll <= rr:
        max_p = (ll + rr) // 2  # 상한액
        # 2번 기준대로 계산해서 총합이 총 예산보다 작거나 같으면 상한액을 올리기
        # 같은 경우 상한액을 올리면 예산 초과하여 while문 종료.
        # ll를 증가시키고 종료된 경우, 마지막 계산된 max_p = rr였다는 뜻이다.
        if sum([min(data, max_p) for data in datas]) <= total:
            ll = max_p + 1
        else:  # 초과하면 상한 낮추기
            # rr를 감소시키고 종료된 경우, 마지막 계산된 max_p를 사용하면 예산을 초과한다는 뜻인데
            # ll보다 작아진 rr가 상한액이 된다.
            # 해당 ll는 max_p를 사용하여 예산이 초과하지 않았을 때 증가시켰으므로,
            # 증가 전의 max_p가 상한액. ll - 1이 되며
            # 현재 ll보다 rr가 작아졌다는 뜻은
            # ll = rr에서 1을 뺀 것이니
            # 현재 rr = ll - 1 = (마지막으로 초과하지 않은 max_p)가 된다.
            rr = max_p - 1
    print(rr)

"""
현 시점 실버3. 제출 40042, 정답률 34.177 %.
실버라고 하기엔 상당히 어렵다.
맞힌 사람 중 풀이를 제대로 이해하고 푼 사람이 얼마나 될지 심히 의심스럽다.
이진탐색이지만 target을 찾는 것이 아니기에 ll, rr, mid 어느 쪽이 상한액인지 파악하기 힘들다.

평소와 같이 수학적 증명은 어렵지만 우연히 대충 때려맞춘 사람들에겐 쉽게 느껴지는 문제.
풀이를 검색해보면 mid가 아니라 rr를 출력하는 이유에 대한 설명을 적어놓은 사람이 아무도 없다.
ll == rr인 경우에도 while문을 작동시키는 이유도 아무도 안적어놨다.
대충 인터넷에서 베꼈거나 이해하지 못한 채로 때려맞춘 것일 확률이 매우 매우 매우 높다.
만약 테케 통과 여부를 보여주지 않는 코테에 나왔다면 대부분의 사람들이 틀렸을 것이다.
"""