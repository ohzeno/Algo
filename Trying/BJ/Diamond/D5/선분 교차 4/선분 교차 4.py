# https://www.acmicpc.net/problem/20150
import sys
sys.stdin = open("input.txt")
def input():
    return sys.stdin.readline().rstrip()

from bisect import bisect_left

class Line:
    def __init__(self, x, y, p, q):
        self.st = (x, y)
        self.ed = (p, q)

    # sort를 위한 비교 연산자
    def __lt__(self, other):
        return self.st[1] < other.st[1]


def ccw(a, b, c):
    x1, y1 = b[0] - a[0], b[1] - a[1]
    x2, y2 = c[0] - a[0], c[1] - a[1]
    return x1 * y2 - y1 * x2


def intersect(l1, l2):
    a, b = l1.st, l1.ed
    c, d = l2.st, l2.ed
    ccw1, ccw2 = ccw(a, b, c), ccw(a, b, d)
    ccw3, ccw4 = ccw(c, d, a), ccw(c, d, b)
    con1, con2 = ccw1 * ccw2, ccw3 * ccw4
    if con1 == 0 and con2 == 0:  # abcd가 일직선 상에 있는 경우
        return a <= d and c <= b
    return con1 <= 0 and con2 <= 0

def sweep(lines):
    events = []
    for i, line in enumerate(lines):
        events.append((line.st[0], "a_start", line))
        events.append((line.ed[0], "b_end", line))
    events.sort()
    active_lines = []
    for p, typ, line in events:
        if typ == "a_start":
            # 선분 추가 전, 바로 위와 바로 아래 선분을 찾아 교차 판정 수행
            pos = bisect_left(active_lines, line)
            # 바로 위 선분과의 교차 검사
            if pos < len(active_lines) and intersect(line, active_lines[pos]):
                return True
            # 바로 아래 선분과의 교차 검사
            if pos > 0 and intersect(line, active_lines[pos-1]):
                return True
            # 선분을 활성 선분 집합에 삽입
            active_lines.insert(pos, line)
        else:
            # 선분 제거
            active_lines.remove(line)
    return False


n = int(input())
lines = []
for i in range(n):
    x, y, p, q = map(int, input().split())
    if x > p:
        x, y, p, q = p, q, x, y
    elif x == p and y > q:
        y, q = q, y
    lines.append(Line(x, y, p, q))
print(1 if sweep(lines) else 0)


"""
현 시점 다이아5. 제출 553, 정답률 12.459%
샤모스-호이 알고리즘을 시도해봤다.
하지만 sorted list를 백준에서 사용할 수 없고, 
sorted list는 직접 구현하기엔 너무 복잡하다. 코드만 1600줄 가량.
그래서 bisect_left로 삽입, 제거 했는데 시간초과.

아마 이 로직 그대로 cpp로 구현하면 통과하지 않을까...
pypy 통과자가 있긴 하니 더 나은 방법이 있다는 것인데, 당장은 떠오르지 않는다.
"""
