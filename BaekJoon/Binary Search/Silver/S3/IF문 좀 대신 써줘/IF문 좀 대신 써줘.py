# https://www.acmicpc.net/problem/19637
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
title = []
tmp = set()
for _ in range(n):
    name, maximum = input().split()
    if maximum not in tmp:
        tmp.add(maximum)
        title.append((name, int(maximum)))
title.sort(key=lambda x: x[1])  # 비 내림차순으로 주어짐. 오름차순이라고 말하지 않음.
l_title = len(title)
for _ in range(m):
    power = int(input())
    ll, rr = 0, l_title - 1
    while ll < rr:  # 칭호가 없는 전투력은 입력으로 주어지지 않음. ll = rr이면 그게 칭호.
        mid = (ll + rr) // 2
        if title[mid][1] < power:  # 상한 초과하면 범위 제외. 오른쪽 탐색.
            ll = mid + 1
        else:  # 초과 아니면 정답인지 아닌지 모름. 범위 포함한 채로 왼쪽 탐색.
            rr = mid
    # mid는 첫 if문을 통과했을 경우 범위에서 제외되므로 정답이 아닌 케이스가 생긴다.
    # ll = mid + 1로 종료된 경우 ll = rr이다.
    # rr = mid로 종료조건이 된 경우는 rr = ll + 1이었다는 뜻이다. 결국 ll과 같아진다.
    # 결국 모든 케이스에서 ll = rr이 만들어지므로 ll이다 rr 위치를 출력하면 된다.
    print(title[ll][0])

"""
현 시점 실버3. 제출 3539 정답률 35.690 %
로직에 딱히 문제가 없는데 시간초과가 계속 나서 이게 실버3 난이도가 맞나 불평중이었다.
알고보니 input()이 느려서 sys.stdin.readline().rstrip()으로 바꾸니 통과됐다...
백준 문제는 이런 면에서 시간제한이 좀 현실과 동떨어진 면이 있는 듯 하다.
"""