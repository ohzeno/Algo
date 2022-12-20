# https://www.acmicpc.net/problem/1158
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
요세푸스. 11866때 로직 그대로 써도 통과되긴 한다.
최적화 체감 난이도는 플레 이상...11866때도 그랬지만 
요세푸스 모르는 채로 인덱스 규칙찾기 너무 힘들다.
찾은 줄 알았는데 n, k 1 ~ 14로 돌려보니 예외 딱 하나 나왔다.
그 예외 수정했더니 기존 케이스들이 망가졌다.
"""
def solution():
    people = [i for i in range(1, n + 1)]
    now = 0
    print('<', end='')
    for i in range(n):
        # k가 아니라 k - 1을 더해주는 이유는 now를 pop해서 한 자리가 사라지기 때문.
        # 최초에는 그냥 인덱스가 0부터라 -1이 적용됨.
        # n - i == 남은 원소 수
        now = (now + k - 1) % (n - i)
        print(people.pop(now), end='')
        if i != n - 1:
            print(', ', end='')
    print('>')

n, k = map(int, input().split())
solution()

