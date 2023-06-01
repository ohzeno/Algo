# https://www.acmicpc.net/problem/17387
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
    if con1 == 0 and con2 == 0:  # abcd가 일직선 상에 있는 경우
        return is_overlap(a, b, c, d)
    elif con1 == 0:  # abc 혹은 abd가 일직선 상에 있는 경우
        if ccw1 == 0:  # abc가 일직선 상에 있는 경우
            return on_segment(a, b, c)
        else:  # abd가 일직선 상에 있는 경우
            return on_segment(a, b, d)
    elif con2 == 0:  # cda 혹은 cdb가 일직선 상에 있는 경우
        if ccw3 == 0:  # cda가 일직선 상에 있는 경우
            return on_segment(c, d, a)
        else:  # cdb가 일직선 상에 있는 경우
            return on_segment(c, d, b)
    return con1 < 0 and con2 < 0

def on_segment(a, b, c):
    """
    abc가 일직선 상에 있을 때만 사용.
    ab 위에 c가 있는지 확인
    """
    return min(a, b) <= c <= max(a, b)

def is_overlap(a, b, c, d):
    """
    abcd가 일직선 상에 있는 경우만 가정
    a   b
      c   d
        a   b
    어느 경우라도 아래 조건으로 겹침이 확인된다.
    """
    return min(a, b) <= max(c, d) and min(c, d) <= max(a, b)

x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))
inter = is_inter((x1, y1), (x2, y2), (x3, y3), (x4, y4))
if inter:
    print(1)
else:
    print(0)

"""
현 시점 골드2. 제출 13348, 정답률 26.316%
선분 교차 1 다음으로 풀었다. 
세 점이 일직선인 경우도 생겨서 조건이 더 복잡해졌다.
달팽이 풀 때와 is_inter 로직이 좀 달라졌다.
on_segment도 새로 만들었다.
"""