# https://www.acmicpc.net/problem/1956
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
볼록껍질을 이루는 점들을 이미 찾았다. 반시계 방향으로 순서를 매겨라.
중복되는 점은 없고 모든 점이 한 직선 위에 있는 경우도 없다.
첫째 줄에 볼록껍질을 이루는 점의 개수를 출력하라.
이어서 반 시계 방향 순서로 매 줄 x y형태로 점의 좌표를 출력하라.
첫 점은 x좌표가 가장 작은 점이다. x좌표가 같다면 y좌표가 작은 점이다.
"""
def ccw(a, b, c):
    """
    Counter Clock Wise.
    v1: a -> b    v2: a -> c
    a -> b -> c의 회전 방향.
    v1과 v2의 외적의 z값이 양이면 좌회전, 음이면 우회전, 0이면 일직선.
    v1 X v2 =   |i   j   k|
                |x1 y1  z1|
                |x2 y2  z2|
    v1 X v2의 z값: x1 * y2 - x2 * y1
    """
    x1, y1 = b[0] - a[0], b[1] - a[1]
    x2, y2 = c[0] - a[0], c[1] - a[1]
    return x1 * y2 - x2 * y1

points = []
for _ in range(int(input())):
    x, y, is_convex = input().split()
    if is_convex == 'Y':
        points.append((int(x), int(y)))
points.sort()
print(len(points))
upper, lower = [], []
for p in points:
    # 윗껍질인데 좌회전이면 제거
    while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) > 0:
        upper.pop()
    # 아랫껍질인데 우회전이면 제거
    while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) < 0:
        lower.pop()
    upper.append(p)
    lower.append(p)
lo_set = set(lower)
for p in lower:  # 반시계로 x, y 작은 순서대로면 아랫껍질부터 출력해야 한다.
    print(*p)
for p in reversed(upper):
    if p not in lo_set:  # 중복되는 점은 출력하지 않는다.
        print(*p)

"""
현 시점 플래5. 제출 3115, 정답률 21.067%
평범한 convex_hull 문제. 8분도 안썼다.
"""