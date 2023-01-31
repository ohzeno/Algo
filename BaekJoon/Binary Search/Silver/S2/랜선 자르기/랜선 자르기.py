# https://www.acmicpc.net/problem/1654
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

k, n = map(int, input().split())  # k개 랜선 잘라서 n개 이상 만들기
datas = [int(input()) for _ in range(k)]
datas.sort()
ll, rr = 1, datas[-1]
while ll <= rr:
    mid = (ll + rr) // 2
    count = 0
    for data in datas:
        count += data // mid
    if n <= count:  # 조건 충족하면 길이 늘려보기
        ll = mid + 1  # 늘리고 끝나면 늘리기 전이 최대임. 즉 rr이 최대.
    else:  # n개 안되면 길이 줄이기
        # n개를 만들 수 없는 경우는 없으니 줄이고 끝나면 줄인 rr이 최댓값.
        rr = mid - 1
print(rr)

"""
현 시점 실버2. 제출 152319 정답률 21.102 %
datas가 1만이라 매번 순회하는게 좀 꺼려졌는데 통과되긴 했다.
"""