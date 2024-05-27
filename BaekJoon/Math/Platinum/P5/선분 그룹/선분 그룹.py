# https://www.acmicpc.net/problem/16566
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
N개 선분들이 2차원 평면상에 주어진다. 
두 선분이 접촉하는 경우 같은 그룹에 속한다고 정의한다.
그룹의 크기는 그룹에 속한 선분의 개수이다.
n개 선분이 주어지면
첫 줄에 그룹의 개수를
둘째 줄에 가장 큰 그룹의 크기를 출력하라.
1 <= N <= 3000
각 좌표의 절댓값은 5000을 넘지 않는다.
"""
from collections import defaultdict


def ccw(a, b, c):
    """
    Counter Clock Wise.
    v1: a -> b    v2: a -> c
    a -> b -> c의 회전 방향.
    v1과 v2의 외적의 z값이 양이면 좌회전, 음이면 우회전, 0이면 일직선.
    v1 X v2 =   |i   j   k|
                |x1 y1  z1|
                |x2 y2  z2|
    v1 X v2의 z값: x1 * y2 - y1 * x2
    """
    x1, y1 = b[0] - a[0], b[1] - a[1]
    x2, y2 = c[0] - a[0], c[1] - a[1]
    return x1 * y2 - y1 * x2


def is_inter(a, b, c, d):
    """
    con1이 음수면 ab를 기준으로 c, d가 서로 다른 방향에 있음.
            c
    a   b
            d
    con1만으로는 위와 같은 경우가 생길 수 있다.
    con2까지 음수면 cd를 기준으로 a, b가 서로 다른 방향에 있으므로 교차가 된다.

    con1이 0인 경우 c나 d가 ab와 일직선을 이룬다.
    a   b   c
            d
    con2가 0이 아닌 경우 이와 같이 3개의 점만 일직선이 된다.
    즉, con1과 con2 둘 중 하나만 0일 때 세 점이 일직선을 이룬다.
    다른 하나가 음수이면
    a   c   b
        d
    위와 같이 교차한다.(con1==0, con2<0)
    """
    ccw1, ccw2 = ccw(a, b, c), ccw(a, b, d)
    ccw3, ccw4 = ccw(c, d, a), ccw(c, d, b)
    con1, con2 = ccw1 * ccw2, ccw3 * ccw4
    if con1 < 0 and con2 < 0:  # 끝이 아닌 한 점에서 교차
        return True
    elif ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:  # abcd가 일직선 상에 있는 경우
        a, b = min(a, b), max(a, b)
        c, d = min(c, d), max(c, d)
        if c <= b and a <= d:  # 겹치는 경우
            return True
    elif con1 <= 0 and con2 <= 0:
        """
        con1 < 0 and con2 == 0:  # a나 b가 cd 내부에 있는 경우
        con1 == 0 and con2 < 0:  # c나 d가 ab 내부에 있는 경우
        con1 == 0 and con2 == 0:  # 두 선분의 끝점 하나가 일치함
        """
        return True
    return False


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        p[max(px, py)] = min(px, py)


n = int(input())
lines = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append(((x1, y1), (x2, y2)))

p = [i for i in range(n)]
# 교차하는 선분들을 같은 그룹으로 묶음.
for i in range(n):
    for j in range(i + 1, n):
        if is_inter(*lines[i], *lines[j]):
            union(i, j)

# 그룹 개수 계산. p는 아직 갱신 안된 경우도 있으므로 find를 다 돌려줘야 한다.
group_cnt = len(set(find(i) for i in range(n)))

# 가장 큰 그룹 크기 계산
group_sizes = defaultdict(int)
for i in range(n):
    parent = find(i)
    group_sizes[parent] += 1
max_group_size = max(group_sizes.values())

print(group_cnt)
print(max_group_size)


"""
현 시점 플래 5. 제출 16406. 정답률 28.192 %
선분 교차판정과 분리 집합을 함께 사용하면 쉽게 풀리는 문제.
"""
