# https://www.acmicpc.net/problem/6850
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
일부 나무의 위치가 주어지면 농부들이 가능한 한 가장 큰 목초지를 만들도록 도와야 합니다.
소가 생존하려면 최소 50평방미터의 목초지가 필요하다는 것은 잘 알려져 있습니다.
사용 가능한 나무를 사용하여 구성할 수 있는 가장 큰 필드에서 생존할 수 있는 소의 수를 출력하라.
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
    v1 X v2의 z값: x1 * y2 - y1 * x2
    """
    x1, y1 = b[0] - a[0], b[1] - a[1]
    x2, y2 = c[0] - a[0], c[1] - a[1]
    return x1 * y2 - y1 * x2

trees = sorted([tuple(map(int, input().split())) for _ in range(int(input()))])
upper, lower = [], []
for tree in trees:
    """
    ccw가 0인 경우(일직선인 경우)를 제거해줘야 정답이 된다. 이걸 몰라서 몇십번 틀렸다.
    정확한 원인은 모르겠다. 
    아마 나중에 넓이를 계산할 때 나눠서 계산하면 부동소수점 오차가 생기는게 아닐까 싶다. 
    하지만 ccw에 epsilon을 사용해도 틀렸기에 확실하진 않다.
    """
    # 위쪽 껍질인데 좌회전이면 제거
    while len(upper) >= 2 and ccw(upper[-2], upper[-1], tree) >= 0:
        upper.pop()
    # 아래 껍질인데 우회전이면 제거
    while len(lower) >= 2 and ccw(lower[-2], lower[-1], tree) <= 0:
        lower.pop()
    upper.append(tree)
    lower.append(tree)
area = 0
for i in range(2,len(upper)):
    area -= ccw(upper[0], upper[i-1], upper[i])
for i in range(2,len(lower)):
    area += ccw(lower[0], lower[i-1], lower[i])
print(int(area // 100))

"""
현 시점 플래 5. 제출 1842. 정답률 39.623%
맞힌 사람 python그룹 2등, 숏코딩 모든 언어 1등
1등이 60ms인데 아마 upper, lower를 나누는 monotone chain을 사용해서 그런 듯 하다.
하나의 리스트에 시계/반시계 방향으로 다 담고 나중에 순회 한번 돌면 60ms 나오지 않을까 싶은데
나는 monotone chain 말고는 몰라서 그냥 넘어간다.
"""