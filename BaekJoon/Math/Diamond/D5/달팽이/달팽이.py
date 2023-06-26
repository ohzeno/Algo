# https://www.acmicpc.net/problem/6990
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

from typing import Optional
from decimal import Decimal, ROUND_HALF_UP
from math import sqrt
def dist(p1: tuple, p2: tuple) -> float:
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return sqrt(a ** 2 + b ** 2)

def ccw(a: tuple, b: tuple, c: tuple) -> int:
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
    z = x1 * y2 - y1 * x2
    # return x1 * y2 - y1 * x2
    if abs(z) < 1e-7:  # 처리 안해주면 틀림...
        return 0
    elif z > 0:
        return 1
    return -1

def get_cross_point(a: tuple, b: tuple, c: tuple, d: tuple) -> tuple:
    """
    선분 ab, cd의 교차점 반환. 교차가 확정됐거나 세 점이 일직선일 때 사용.
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
    # if 0 <= x <= l and 0 <= y <= l:  # 교차점이 울타리 안에 있을 때만 반환.
    #     return x, y
    # else:
    #     return False

def get_meet_point(a: tuple, b: tuple, c: tuple, d: tuple) -> tuple:
    """
    abcd가 일직선 상에 있고, ab와 cd가 겹치는 경우에만 사용.
    """
    Ax, Ay = a[0], a[1]
    Bx, By = b[0], b[1]
    Cx, Cy = c[0], c[1]
    Dx, Dy = d[0], d[1]
    AB = [Bx - Ax, By - Ay]
    AC = [Cx - Ax, Cy - Ay]
    CD = [Dx - Cx, Dy - Cy]
    if dot_product(AB, CD) > 0:  # 선분이 겹치고 내적이 양수면 AB와 CD가 같은 방향을 가리킴.
        if dot_product(AB, AC) > 0:  # 내적이 양수면 AB와 AC가 같은 방향을 가리킴. 즉 a가 c를 향함.
            return c  # c는 출발점이므로 항상 울타리 내임.
        # 내적이 음수면 c가 a를 기준으로 반대편임. ab, cd는 같은 방향이므로 c는 a를 향함.
        return a  # a는 출발점이므로 항상 울타리 내임.
    else:  # 선분이 겹치고(내적이 0일 수 없음) 내적이 음수이면 a와 c는 서로를 향함.
        mid_x = (Ax + Cx) / 2
        mid_y = (Ay + Cy) / 2
        return mid_x, mid_y  # a, c의 중간점은 울타리 내에 있음.

def is_inter(a: tuple, b: tuple, c: tuple, d: tuple) -> Optional[tuple]:
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
        return get_cross_point(a, b, c, d)
    elif ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:  # abcd가 일직선 상에 있는 경우
        if is_overlap(a, b, c, d):  # 겹치는 경우
            return get_meet_point(a, b, c, d)
        return False  # 겹치지 않으면 교차하지 않음
    elif con1 <= 0 and con2 <= 0:
        """
        con1 < 0 and con2 == 0:  # a나 b가 cd 내부에 있는 경우
        con1 == 0 and con2 < 0:  # c나 d가 ab 내부에 있는 경우
        con1 == 0 and con2 == 0:  # 두 선분의 끝점 하나가 일치함
        """
        return get_cross_point(a, b, c, d)
    return False

def dot_product(a: tuple, b: tuple) -> int:
    return a[0] * b[0] + a[1] * b[1]

def is_overlap(a: tuple, b: tuple, c: tuple, d: tuple) -> bool:
    """
    abcd가 일직선 상에 있는 경우만 가정
    a   b
      c   d
        a   b
    어느 경우라도 아래 조건으로 겹침이 확인된다.
    """
    return min(a, b) <= max(c, d) and min(c, d) <= max(a, b)

def find_crashes() -> list[tuple]:
    walls = [
        [[0, 0], [0, l]],
        [[0, 0], [l, 0]],
        [[l, 0], [l, l]],
        [[0, l], [l, l]]
    ]
    cases = []
    for a in range(n):
        a_pos, b_pos = snail[a]['st'], snail[a]['ed']
        for c in range(a + 1, n):
            c_pos, d_pos = snail[c]['st'], snail[c]['ed']
            crashed = is_inter(a_pos, b_pos, c_pos, d_pos)
            if not crashed:
                continue
            t_ap = dist(a_pos, crashed)
            t_cp = dist(c_pos, crashed)
            if t_ap == t_cp:  # a, c가 동시에 부딪힘
                cases.append((a, c, 1, t_ap))
            elif t_ap < t_cp:
                cases.append((a, c, 2, t_cp))
                snail[c]['crash'][t_cp] = crashed
            else:  # a가 c의 경로에 부딪힘
                cases.append((c, a, 2, t_ap))
                snail[a]['crash'][t_ap] = crashed
        for c_pos, d_pos in walls:
            crashed = is_inter(a_pos, b_pos, c_pos, d_pos)
            if not crashed:
                continue
            t_ap = dist(a_pos, crashed)
            cases.append((-1, a, 3, t_ap))
    return sorted(cases, key=lambda x: x[3])

def solve() -> str:
    for a, c, c_type, time in cases:
        if 0 < snail[c]['stop'] < time:  # c가 더 일찍 정지되었으면 무시
            continue
        if c_type == 1:  # 두 달팽이가 동시에 충돌
            if 0 < snail[a]['stop'] < time:  # a가 더 일찍 정지되었으면 무시
                continue
            max_t = time  # 이전 충돌이 없으면 최대 시간 갱신
            snail[a]['stop'] = time
            snail[c]['stop'] = time
        elif c_type == 2:  # c가 다른 a의 흔적에 충돌
            cur_d = dist(snail[a]['st'], snail[c]['crash'][time])  # 현재 충돌까지의 거리
            if not snail[a]['stop'] or snail[a]['stop'] >= cur_d:  # 이전 충돌이 더 멀리 갔다면 유효
                max_t = time
                snail[c]['stop'] = time
        elif c_type == 3:  # c가 경계에 도달한 경우
            max_t = time
            snail[c]['stop'] = time
    # num = Decimal(str(max_t))  # str를 사용하지 않으면 Decimal로 변환하는 과정에서 손실생김.
    # return num.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    return f'{max_t:.2f}'

n, l = map(int, input().split())
snail = {
    i: {
        'st': None,
        'ed': None,
        'crash': {},
        'stop': 0,
    } for i in range(n)
}
for i in range(n):
    x, y, p, q = map(int, input().split())
    snail[i]['st'] = (x, y)
    # dx, dy = p - x, q - y
    # snail[i]['ed'] = (x + dx * l * 2, y + dy * l * 2)
    if x == p:
        nx = x
        if q > y:
            ny = l
        else:
            ny = 0
    else:
        a = (q - y) / (p - x)  # 기울기
        """
        y = ax + b
        b = y - ax
        b = q - ap
        b = q - (q - y) / (p - x) * p
        b = q(p - x)/(p - x) + (y - q)p/(p - x)
        b = (qp - qx)/(p - x) + (py - pq)/(p - x)
        b = (qp - qx + py - pq)/(p - x)
        b = (py - qx)/(p - x)
        """
        b = (p * y - q * x) / (p - x)  # y절편
        if x < p:  # 오른쪽으로 이동
            ty = a * l + b  # y = ax + b에 l 대입
            if ty >= l:  # y가 l보다 크면 울타리 상단
                nx, ny = (l - b) / a, l  # l = ax + b
            elif ty <= 0:  # y가 0보다 작으면  울타리 하단
                nx, ny = -b / a, 0  # 0 = ax + b
            else:  # y가 0 ~ l 사이에 있으면 울타리 오른쪽
                nx, ny = l, ty
        else:  # 왼쪽으로 이동
            ty = b  # y = ax + b에 0 대입
            if ty >= l:  # y가 l보다 크면 울타리 상단
                nx, ny = (l - b) / a, l  # l = ax + b
            elif ty <= 0:  # y가 0보다 작으면  울타리 하단
                nx, ny = -b / a, 0  # 0 = ax + b
            else:  # y가 0 ~ l 사이에 있으면 울타리 왼쪽
                nx, ny = 0, b
    snail[i]['ed'] = (nx, ny)
cases = find_crashes()
print(solve())
# 교점이 존재할 경우 p라고 하자.
# 1. 두 달팽이가 동시에 부딪힐 경우
#   ap, cp의 거리가 같음
# 2. 한 달팽이가 다른 달팽이의 흔적에 부딪힐 경우
#   ap < cp이면 cp가 나중에 도달하므로 cp의 시간을 계산.
# 3. 달팽이가 울타리에 부딪힐 경우
#   4변에 대해 교차판별.
# 충돌 지점이 울타리 밖이면 무시.
# 하나의 충돌을 (a, b, type, time)로 표현하여 time순 정렬.
# 실제 충돌이 아닌 것들을 걸러내고, 충돌이 유효하다면 정지 시간을 max_t와 비교하여 갱신.
# type1: a, c가 모두 더 빠른 시간의 충돌에 의해 정지되지 않았다면 유효
# type2: a의 더 빠른 시간대의 충돌을 고려해도 a가 p보다 멀리 갔다면 유효
# type3: a가 더 빠른 시간대의 충돌로 정지되지 않았다면 유효

"""
현 시점 다이아5. 제출 731, 정답률 8.824%
엄청 고생했다.
첫 풀이에서 선분 끝점을 방향벡터에 2l을 곱한 점으로 잡았다.
시작점은 울타리 내부이고, 울타리 내부에서 최대 이동거리는 l * 2**0.5이다.
방향벡터는 정수이므로 이렇게 하면 항상 울타리 바깥에 끝점을 두게 된다.
get_cross_point는 항상 울타리 내부의 교차점만 반환하도록 해뒀었다.
하지만 98%쯤에서 틀렸다.

ccw는 절댓값이 1e-7보다 작으면 0을 반환하도록 해야 정답처리된다.
float연산 오차가 있는 케이스가 있는듯.
플래티넘 문제도 오차 범위를 명시하는데 여긴 없다...
수정 솔루션은 선분 끝점을 울타리와의 교점으로 잡았다.
그래서 float연산 오차 말고 생각나는게 없는데
오히려 수정 솔루션이 float이 되고 이전 풀이가 끝점이 정수인데
float연산에 오차가 생긴다는게 말이 되나...?

정답을 float연산을 이용해 만들어서 오차가 생기고, 추가적으로 오차범위를 고려해 채점하더라도
정수를 이용한 내 풀이의 정답이 오차범위 밖인 이상한 상황이면 채점 케이스의 오류라는 가설이...

그리고 소숫점 이하 셋째 자리에서 반올림 해서 출력하라고 하고, 
round만 사용하면 반올림이 제대로 되지 않는다.
나는 decimal 모듈을 사용했지만
웃기게도 그냥 내림으로 .2f 출력하면 정답이 된다.
반올림 케이스가 없는듯.

올림피아드 기출인데 여러모로 허술한듯 하다.

더 빠른 추가 풀이를 작성했다. 코드가 길어 다른 파일로 분리했다.
"""