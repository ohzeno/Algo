# https://www.acmicpc.net/problem/2096
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
n줄에 0 이상 9 이하의 숫자 세 개씩 적혀있음.
내려가기 게임. 첫 줄에서 시작해서 마지막 줄에서 끝나는 게임.
첫 줄의 숫자 중 하나를 골라서 시작. 다음 줄로 내려갈 때는 제약이 있음.
바로 아래의 수로 넘어가거나 아래의 수와 인접한 수로만 이동 가능.
숫자표가 주어졌을 때 얻을 수 있는 최대 점수와 최소 점수를 구하라.
1 <= n <= 10_0000
"""
min_dp = [0] * 3
max_dp = [0] * 3
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    mi1, mi2, mi3 = min_dp
    mx1, mx2, mx3 = max_dp
    min_dp = [min(mi1, mi2) + a, min(mi1, mi2, mi3) + b, min(mi2, mi3) + c]
    max_dp = [max(mx1, mx2) + a, max(mx1, mx2, mx3) + b, max(mx2, mx3) + c]
print(max(max_dp), min(min_dp))


"""
현 시점 골드 5. 제출 40058. 정답률 36.748 %
간단한 dp라고 생각하고 바로 작성해서 제출했더니 메모리 초과.
n이 10만까지라 숫자표, dp표 둘을 다루면 메모리 초과.
결국 dp표는 1차원 배열로 관리하면서 한 줄씩 처리했다.
골드5 치고는 쉬운 문제인듯.
"""
