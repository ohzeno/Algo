# https://www.acmicpc.net/problem/27718
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
lines = [list(map(int, input().split())) for _ in range(n)]
mat = [[0] * n for _ in range(n)]
for i in range(n):
    mat[i][i] = 3
    a = (lines[i][0], lines[i][1])
    b = (lines[i][2], lines[i][3])
    for j in range(i + 1, n):
        c = (lines[j][0], lines[j][1])
        d = (lines[j][2], lines[j][3])
        mat[i][j] = is_inter(a, b, c, d)
        mat[j][i] = mat[i][j]
for row in mat:
    print(*row, sep='')

"""
현 시점 플래5. 제출 234, 정답률 30.435%
조건이 상당히 까다롭다.
끝점끼리 만나는 경우를 판정하는 함수에서
선분의 방향 단위벡터를 계산해서 비교했으나, 
float연산의 오차로 인해 기울기가 같더라도 방향벡터가 다르게 나오는 경우가 있었다.
그래서 방향벡터가 같은지를 확인하는 함수를 따로 만들었다.
예제 케이스를 전부 통과했으나 틀렸다.

그냥 ccw랑 con1, con2, min, max를 이용하여 분기를 잘 정리해주니 통과했다.
pypy로 통과했으나 python으로는 시간초과가 발생했다. 
python으로 통과한 사람이 한 명 있던데 어떻게 한건지 좀 궁금하다.
"""