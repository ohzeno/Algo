# https://www.acmicpc.net/problem/1708
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
    v1 X v2의 z값: x1 * y2 - x2 * y1
    """
    x1, y1 = b[0] - a[0], b[1] - a[1]
    x2, y2 = c[0] - a[0], c[1] - a[1]
    return x1 * y2 - x2 * y1

n = int(input())
trees = sorted([tuple(map(int, input().split())) for _ in range(n)])
upper, lower = [], []
for tree in trees:
    """
    볼록 껍질의 변에 점이 여러 개 있는 경우에는 가장 양 끝 점만 개수에 포함한다.
    위 조건을 만족시키기 위해 ccw가 0인 경우(일직선)도 제거한다.
    """
    while len(upper) >= 2 and ccw(upper[-2], upper[-1], tree) >= 0:  # 위쪽은 우회전이 필요하다. 좌회전 요소 제거
        upper.pop()
    while len(lower) >= 2 and ccw(lower[-2], lower[-1], tree) <= 0:  # 아래쪽은 좌회전이 필요하다. 우회전 요소 제거
        lower.pop()
    upper.append(tree)
    lower.append(tree)
print(len(set(upper + lower)))
