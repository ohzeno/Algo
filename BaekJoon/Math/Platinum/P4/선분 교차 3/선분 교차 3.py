# https://www.acmicpc.net/problem/20149
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def get_cross_point(a, b, c, d):
    """
    선분 ab, cd의 교차점 반환. 교차가 확정됐을 때 사용.
        기울기가 같은 경우(교차하므로 평행은 제외됨. 겹치는 경우),
        교점이 없는 경우는 고려하지 않음.
    B-A = A에서 B로 향하는 벡터.
    P = A + s(B-A) 이 벡터방정식은 AB위의 점을 나타내는 식이다.
    s = 0일 때 A, s = 1일 때 B를 가리킨다.
    Q = C + t(D-C)

    교차점 벡터는 P, Q를 모두 만족할 것이다.
    A + s(B-A) = C + t(D-C)
    t(D-C) = A-C + s(B-A)
    t = (A-C + s(B-A)) / (D-C)

    ABCD는 모두 벡터이므로 x, y값을 각각 대입하면 두 식이 성립한다.
    t = (Ax-Cx + s(Bx-Ax)) / (Dx-Cx)
    t = (Ay-Cy + s(By-Ay)) / (Dy-Cy)
    (Ax-Cx + s(Bx-Ax)) / (Dx-Cx) = (Ay-Cy + s(By-Ay)) / (Dy-Cy)
    (Ax-Cx + s(Bx-Ax))(Dy-Cy) = (Ay-Cy + s(By-Ay))(Dx-Cx)
    (Ax-Cx)(Dy-Cy) + s(Bx-Ax)(Dy-Cy) = (Ay-Cy)(Dx-Cx) + s(By-Ay)(Dx-Cx)
    s{(Bx-Ax)(Dy-Cy) - (By-Ay)(Dx-Cx)} = (Ay-Cy)(Dx-Cx) - (Ax-Cx)(Dy-Cy)
    s = {(Ay-Cy)(Dx-Cx) - (Ax-Cx)(Dy-Cy)} / {(Bx-Ax)(Dy-Cy) - (By-Ay)(Dx-Cx)}

    이 s를 P에 대입하면 교차점이 나온다.
    교차 확정이므로 아래 케이스들은 고려하지 않는다.
        s값이 0~1을 벗어나면 교차점이 없는 경우다.
        분모가 0인 경우는
            (Bx-Ax)(Dy-Cy) = (By-Ay)(Dx-Cx)
            (Dy-Cy) / (Dx-Cx) = (By-Ay) / (Bx-Ax)
            즉, 두 선분의 기울기가 같은 경우이다.
    """
    Ax, Ay = a[0], a[1]
    Bx, By = b[0], b[1]
    Cx, Cy = c[0], c[1]
    Dx, Dy = d[0], d[1]
    denom = (Bx - Ax) * (Dy - Cy) - (By - Ay) * (Dx - Cx)
    s = ((Ay - Cy) * (Dx - Cx) - (Ax - Cx) * (Dy - Cy)) / denom
    x = Ax + s * (Bx - Ax)
    y = Ay + s * (By - Ay)
    return x, y

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
        return 2, get_cross_point(a, b, c, d)
    elif ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:  # abcd가 일직선 상에 있는 경우
        a, b = min(a, b), max(a, b)
        c, d = min(c, d), max(c, d)
        if c < b and a < d:  # 겹치는 경우
            return 3, ()
        elif b == c:  # 끝점에서 만남
            return 1, b
        elif d == a:
            return 1, d
        return 0, ()  # 겹치지 않으면 교차하지 않음
    elif con1 <= 0 and con2 <= 0:
        """
        con1 < 0 and con2 == 0:  # a나 b가 cd 내부에 있는 경우
        con1 == 0 and con2 < 0:  # c나 d가 ab 내부에 있는 경우
        con1 == 0 and con2 == 0:  # 두 선분의 끝점 하나가 일치함
        """
        return 1, get_cross_point(a, b, c, d)
    return 0, ()

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
a, b = (l1[0], l1[1]), (l1[2], l1[3])
c, d = (l2[0], l2[1]), (l2[2], l2[3])
inter, pos = is_inter(a, b, c, d)
if inter:
    print(1)
    if inter != 3:
        print(*pos)
else:
    print(0)

"""
현 시점 플래4. 제출 6286, 정답률 20.764%
교차 여부 뿐만 아니라 교차점도 구하는 문제.
한 점에서 만날 때 벡터방정식으로 교점을 구해주면 된다.
"""