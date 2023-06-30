# https://www.acmicpc.net/problem/2699
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
정수좌표를 갖는 점을 격자점이라고 한다. 
격자 다각형은 모든 꼭짓점이 격자점으로 이루어진 다각형이다.

만약, 다각형의 두 꼭짓점을 잇는 모든 선분이 다각형 내부(또는 경계)에 있다면, 
이 다각형을 볼록 다각형이라고 한다. 즉, 다각형의 내부각이 모두 180도 보다 작은 것이다.

격자점으로 이루어진 집합 S가 주어졌을 때, S의 모든 격자점을 포함하는 
가장 작은 볼록 (격자) 다각형을 컨벡스 헐이라고 한다. 
컨벡스 헐의 꼭짓점은 모두 S에 포함된 격자점이어야 한다. 
만약, 모든 점이 같은 일직선 상에 있다면, 컨벡스 헐은 선분이 될 것이다. (오른쪽 그림)

아래 그림은 집합에 포함된 점은 굵은 점으로, 컨벡스 헐의 꼭짓점은 X로, 변은 선분으로 나타낸 그림이다.
https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/images/latice.png

격자 다각형의 꼭짓점의 일반적인 순서는 다음과 같다.

첫 번째 꼭짓점은 y좌표가 가장 큰 점이다. 
만약, 그러한 점이 2개라면, x가 작은 점이 첫 번째 점이다.
그 다음 점부터는 시계방향 순서이다.
격자점의 집합이 주어졌을 때, 컨벡스 헐을 일반적인 순서로 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 P(1 ≤ P ≤ 1000)가 주어진다. 
각 테스트 케이스의 첫째 줄에는 집합에 포함된 격자점의 수 N(3 ≤ N ≤ 50)이 주어진다. 
나머지 줄은 집합에 포함되어 있는 격자점의 좌표가 한 줄에 5개씩 주어진다. 
(마지막 줄은 이보다 적을 수 있다) 모든 점은 x와 y좌표가 순서대로 주어지며, 공백으로 구분되어 있다. 
좌표는 절댓값이 20보다 작거나 같은 정수이다.

각 테스트 케이스에 대해서, 첫째 줄에는 컨벡스 헐에 포함된 점의 수를 출력한다. 
그 다음 줄부터 컨벡스헐에 포함된 격자점을 한 줄에 하나씩 일반적인 순서대로 출한다. 
x와 y를 공백으로 구분하여 출력한다.
"""
from math import atan2, degrees
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

def getD(p1, p2):
    dy, dx = p2[1] - p1[1], p2[0] - p1[0]
    return degrees(atan2(dy, dx))

for _ in range(int(input())):
    points = set()  # 가끔 중복 있음.
    n = int(input())
    n, denom = divmod(n, 5)
    if denom:
        n += 1
    for i in range(n):
        datas = list(map(int, input().split()))
        for j in range(0, len(datas), 2):
            points.add((datas[j], datas[j+1]))
    # 그레이엄 스캔 방향 변형
    top = min(points, key=lambda x: (-x[1], x[0]))  # 기준점
    points.remove(top)  # 기준점은 빼고 정렬
    points = sorted(points, key=lambda x: (
        -getD(top, x),  # 기준점과의 각도. 왼쪽 0도 아래 90도 오른쪽 180도라 음수로 정렬
        x[1] if x[0] <= top[0] else -x[1],  # 오른쪽 반원은 y값이 큰게 먼저. 왼쪽 반원은 y값이 작은게 먼저
        x[0])  # 이게 필요한가 싶지만 top 수평 오른쪽 상에 2개 점 있으면 필요함. 각과 y값이 같은데 x값이 다른건 다른 곳에는 없다.
    )
    conv = [top]  # top부터 시작
    for p in points:
        # 일직선이나 좌회전은 빼줌.
        while len(conv) >= 2 and ccw(conv[-2], conv[-1], p) >= 0:
            conv.pop()
        conv.append(p)
    # -2, -1, top 이게 일직선이 되는 경우를 위에서 체크하지 못한다.
    # -1, top, 1의 경우, top이 (-y, x) 정렬 가장 앞이므로 -1이 top과 일직선상에 있을 수 없다.
    while len(conv) >= 3 and ccw(conv[-2], conv[-1], top) == 0:
        conv.pop()
    print(len(conv))  # 점의 개수
    for r in conv:
        print(*r)  # 점 출력


"""
현 시점 플래 5. 제출 1171. 정답률 55.847%
맞힌 사람 python그룹 4등, 숏코딩 모든 언어 1등

위 꼭지점을 기준으로 하므로 변형이긴 하지만 그레이엄 스캔을 처음 써봤다.
모노톤 체인에서는 윗껍질, 아랫껍질만 검사하므로 
왼쪽 끝 3점이나 오른쪽 끝 3점에 대한 검사가 불가한데,
그레이엄 스캔도 마찬가지로 끝부분 근처 검사가 되지 않아서 추가 검사를 해줬다.
모노톤 체인과 다르게 
ccw 외에 atan2, degrees를 사용하여 각도를 구하는 함수를 만들어 줘야 한다.

문제 설명이 개판이다. '컨벡스헐에 포함된 격자점'의 정의가 없다.
'집합에 포함된 점은 굵은 점'이라는 말 때문에 처음엔 껍질 내부의 점까지 출력하려 했다.
예시 케이스부터 계속 틀려서 살펴보다보니 
그냥 '컨벡스 헐의 꼭지점'을 시계방향 순으로 출력하는 것이고
'꼭지점'이므로 일직선 상의 점이 있다면 양끝 점만 컨벡스 헐에 포함된다.
"""