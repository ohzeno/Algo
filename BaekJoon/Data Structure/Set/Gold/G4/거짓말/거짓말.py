# https://www.acmicpc.net/problem/1043
import sys
sys.stdin = open("input.txt")
def input():
    return sys.stdin.readline().rstrip()

"""
사람 수 n과 파티 수 m이 주어진다. (1 ≤ n ≤ 50, 0 ≤ m ≤ 50)
이야기의 진실을 아는 사람의 수(0~50)와 번호(1~n)가 주어진다.
이후 각 파티에 오는 사람들 번호가 주어진다.
모든 파티에 참가하면서 들키지 않게 과장된 이야기를 할 수 있는 최대 파티 수를 출력하라.
"""

n, m = map(int, input().split())
truth = set(map(int, input().split()[1:]))
parties = [set(map(int, input().split()[1:])) for _ in range(m)]
for _ in range(m):  # 매 순회 각 파티가 truth에 업데이트 됨.
    for party in parties:
        if truth & party:  # 진실 멤버가 파티에 있으면
            truth |= party  # 현 파티 멤버들 진실 멤버에 추가
# 모든 파티 순회하며 진실멤버가 없는 파티 카운트
print(sum(not bool(truth & party) for party in parties))


"""
현 시점 골드 4. 제출 29061. 정답률 45.029 %
유니온 파인드로 풀었던 문제인데, set를 사용해서 풀어봤다.
훨씬 간결해짐.
"""
