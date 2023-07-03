# https://www.acmicpc.net/problem/6990
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

from math import sqrt
INF = float('inf')
class Snail:
    def __init__(self, x, y, p, q):
        self.a = x
        self.b = y
        self.c = p
        self.d = q
    def meet_time(self, c: 'Snail') -> tuple[float, float]:
        """
        (a가 교차점으로 가는 시간, b가 교차점으로 가는 시간)을 반환
        만나지 않으면 (INF, INF) 반환
        달팽이는 1/s로 움직이므로 거리 = 시간.
        """
        avx, avy = self.c - self.a, self.d - self.b  # a의 방향벡터
        bvx, bvy = c.c - c.a, c.d - c.b  # b의 방향벡터
        dx, dy = c.a - self.a, c.b - self.b  # ast->bst 벡터
        if avx * bvy - avy * bvx == 0:  # a와 b가 평행이면
            if avx * dy - avy * dx == 0:  # a와 b가 같은 직선 위에 있으면
                toward = avx * dx + avy * dy > 0  # a가 b를 향하면
                towardb = bvx * dx + bvy * dy < 0  # b가 a를 향하면
                d = sqrt(dx ** 2 + dy ** 2)  # ast->bst 거리
                if toward and towardb:  # a와 b가 서로를 향하면
                    return d / 2, d / 2
                elif toward and not towardb:  # a만 b를 향하면
                    return d, 0
                elif not toward and towardb:  # b만 a를 향하면
                    return 0, d
                return INF, INF  # a와 b가 서로를 향하지 않으면
            return INF, INF  # a와 b가 같은 직선 위에 있지 않으면 만나지 않음.
        """
        a의 경로: (a.a, a.b) + r1 * (avx, avy)
        b의 경로: (b.a, b.b) + r2 * (bvx, bvy)
        교점 구하기 위해 연립
        (a.a, a.b) + r1 * (avx, avy) = (b.a, b.b) + r2 * (bvx, bvy)
        x, y에 대해 분리
        a.a + r1 * avx = b.a + r2 * bvx
        a.b + r1 * avy = b.b + r2 * bvy
        r1에 대해 정리
        r1 = (b.a - a.a + r2 * bvx) / avx  (1)
        r1 = (b.b - a.b + r2 * bvy) / avy  (2)
        연립
        (b.a - a.a + r2 * bvx) / avx = (b.b - a.b + r2 * bvy) / avy
        r2에 대해 정리
        r2 = (avy * (b.a - a.a) - avx * (b.b - a.b)) / (avx * bvy - avy * bvx)
           = (avy * dx - avx * dy) / (avx * bvy - avy * bvx)
        """
        r2 = (avy * dx - avx * dy) / (avx * bvy - avy * bvx)  # b 스케일러
        if self.c == self.a:  # a가 수직으로 움직이면
            r1 = (dy + r2 * bvy) / avy  # a 스케일러. avx가 0이므로 (2)사용
        else:  # 수직이 아니면
            r1 = (dx + r2 * bvx) / avx  # (1)사용
        if r1 < 0 or r2 < 0:  # 각 출발점에서 벡터 반대로 가야 만남. 만나지 않음.
            return INF, INF
        da = r1 * sqrt(avx ** 2 + avy ** 2)
        db = r2 * sqrt(bvx ** 2 + bvy ** 2)
        return da, db
    def wall_time(self) -> tuple[float, float]:
        """
        t가 INF가 아닌 경우에만 ts에 추가하면 가끔 2개가 들어간다.
        꼭지점을 향할 경우 그러는 것 같은데, INF가 아닌 경우 바로 반환하면 틀리고
        min으로 반환해야 통과한다. float연산 문제일듯.
        """
        ts = []
        for wall in walls:
            t, _ = self.meet_time(wall)
            ts.append(t)
        return min(ts), INF
n, l = map(int, input().split())
snails = [Snail(*map(int, input().split())) for _ in range(n)]
cases = []
walls = [
    Snail(0, 0, l, 0),
    Snail(l, 0, l, l),
    Snail(l, l, 0, l),
    Snail(0, l, 0, 0),
]
for a in range(n):  # 각 달팽이가 벽에 부딪히는 시간
    at, inf = snails[a].wall_time()
    cases.append((at, inf, a, -1))
for a in range(n):
    for c in range(a + 1, n):
        at, ct = snails[a].meet_time(snails[c])
        if at == INF:  # 만나지 않으면 다음
            continue
        # ct보다 at가 크면 a가 c의 경로에 부딪힌다는 뜻.
        if at >= ct:  # =은 둘 다 처리해야하니 위아래 다 넣는다.
            cases.append((at, ct, a, c))
        if at <= ct:  # c가 a의 경로에 부딪히는 경우.
            cases.append((ct, at, c, a))
cases.sort()  # 시간순으로 정렬하면 먼저 만나는 것부터 처리할 수 있다.
max_t = n_stop = 0  # 도착한 달팽이 수
stop = [INF] * n  # 각 달팽이가 도착하는 시간
for at, ct, a, c in cases:
    # a가 이미 도착했으면 다음
    # c가 벽이 아닌데 이미 도착했으면 다음
    if stop[a] != INF or (c != -1 and ct > stop[c]):
        continue
    max_t = at
    stop[a] = at
    n_stop += 1
    if n_stop == n:  # 모든 달팽이가 도착하면 중단
        break
print(f'{max_t:.2f}')


"""
현 시점 다이아5. 제출 731, 정답률 8.824%
meet_time()에서 만나는 지점이 범위를 벗어나면 만나지 않는 것으로 처리했더니 틀렸다.
float연산 문제인듯.

첫 풀이보다 2200B정도 짧고 5~600ms정도 빠르다.
두 풀이 모두 모든 달팽이, 벽에 대해 교차판정을 한다.
하지만 첫 코드는 
데이터 입력 과정에서 벽에 닿는 지점을 연산하는 과정이 있고
is_inter에서는 교차점을 찾아내고, 이후 교차점과 출발점 사이의 거리를 계산한다.
또한 충돌타입을 판정하여 케이스를 입력하고, 이후 충돌타입을 확인하며 연산한다.
그리고 첫 코드는 케이스들을 모두 순회한다. 
물론 is_inter에서 울타리 밖 충돌을 걸러냈다.
두번째 코드는 울타리 밖 충돌을 걸러내지 않았지만 n개의 달팽이가 모두 정지하면 순회를 종료한다.
첫 코드에도 n개의 달팽이가 정지하면 종료하도록 해봤는데, 틀렸다.
꼭지점에 접촉하는 케이스를 중복처리 하지 않아서 그런 건가 싶기도 한데,
두번째 코드는 꼭지점에 접촉하는 케이스를 중복처리하지 않아도 통과했다.

결론은 첫 코드에서 방향벡터를 사용하면 안되는 이유를 몰랐던 것처럼
두번째 코드도 완전히 이해한 것은 아니다.
두 코드를 작성하는 데에 4일 이상 소모했기에 더 분석하지는 않기로 했다.
150회 가까이 제출했고, 파이썬으로 푼 사람이 나 혼자라 참고할 코드도 없다.
"""