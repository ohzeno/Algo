# https://www.acmicpc.net/problem/2166
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
2차원 평면 상에 n(3 ≤ n ≤ 10,000)개의 점으로 이루어진 다각형이 있다. 이 다각형의 면적을 구하는 프로그램을 작성하시오.
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


n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
area = 0
for i in range(-1, n - 1):
    area += ccw([0, 0], points[i], points[i + 1])
print(round(abs(area) / 2, 1))


"""
현 시점 골드 5. 제출 29175. 정답률 28.937%
골드5길래 볼록껍질 다각형만 나올거라 생각해서 모노톤체인을 응용했었는데
그냥 다각형이 나와서 틀렸다. 점 하나를 점해서 정렬된 점들을 외적하려 했었는데
이렇게 무작위 점인 경우는 원점에서 각 점으로 가는 벡터를 모두 더해준 후
마지막에 절댓값으로 바꾸고 2로 나눠주면 된다. 

신발끈 공식이라고 한다.
증명은 까다로워서 하지 않았다.
x축과 평행한 정사각형 정도로 그림을 그려보면 
각 벡터에서 음, 양이 섞여도 최종적으로 정사각형 넓이만 남는걸 알 수 있다.
"""
