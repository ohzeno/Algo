# https://www.acmicpc.net/problem/20150
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

from heapq import heappush as hpush, heappop as hpop, heapify
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
    하지만 위처럼 세 점이 일직선을 이뤄도 교차하지 않는 경우가 있어 on_segment를 사용한다.
    """
    ccw1, ccw2 = ccw(a, b, c), ccw(a, b, d)
    ccw3, ccw4 = ccw(c, d, a), ccw(c, d, b)
    con1, con2 = ccw1 * ccw2, ccw3 * ccw4
    if con1 < 0 and con2 < 0:  # 끝이 아닌 한 점에서 교차
        return 2
    elif ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:  # abcd가 일직선 상에 있는 경우
        a, b = min(a, b), max(a, b)
        c, d = min(c, d), max(c, d)
        if c < b and a < d:  # 겹치는 경우
            return 3
        elif b == c or d == a:  # 끝점에서 만남
            return 1
        return 0  # 겹치지 않으면 교차하지 않음
    elif con1 <= 0 and con2 <= 0:
        """
        con1 < 0 and con2 == 0:  # a나 b가 cd 내부에 있는 경우
        con1 == 0 and con2 < 0:  # c나 d가 ab 내부에 있는 경우
        con1 == 0 and con2 == 0:  # 두 선분의 끝점 하나가 일치함
        """
        return 1
    return 0

n = int(input())
lines = []
for _ in range(n):
    x, y, p, q = map(int, input().split())
    if x > p:
        x, y, p, q = p, q, x, y
    hpush(lines, (x, y, p, q))
for i in range(n):
    a = (lines[i][0], lines[i][1])
    b = (lines[i][2], lines[i][3])
    for j in range(i + 1, n):
        c = (lines[j][0], lines[j][1])
        if b[0] < c[0]:
            break
        d = (lines[j][2], lines[j][3])
        if is_inter(a, b, c, d):
            print(1)
            exit()
print(0)



"""
현 시점 다이아5. 제출 553, 정답률 12.459%
샤모스-호이 알고리즘을 구현해야 하는데, python으로 구현된 자료가 없다.
알고리즘 자체에 대한 설명을 한 블로그가 둘 있는데,
명확한 변수 설명, 주술 호응이 없어서 과정을 이해할 수가 없다.
"""