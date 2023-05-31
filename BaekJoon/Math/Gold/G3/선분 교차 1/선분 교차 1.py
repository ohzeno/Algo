# https://www.acmicpc.net/problem/17386
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

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
    """
    con1 = ccw(a, b, c) * ccw(a, b, d)
    con2 = ccw(c, d, a) * ccw(c, d, b)
    if con1 < 0 and con2 < 0:
        return 1
    return 0

x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))
inter = is_inter((x1, y1), (x2, y2), (x3, y3), (x4, y4))
if inter:
    print(1)
else:
    print(0)

"""
현 시점 골드3. 제출 9150, 정답률 35.131%
D5 달팽이 문제에서 로직이 문제인지 float연산 오류가 문제인지 확인하기 위해
선분 교차판정 문제를 찾아서 따로 테스트 해보는 중.
세 점이 일직선인 경우가 없는 문제라 편했다.
"""