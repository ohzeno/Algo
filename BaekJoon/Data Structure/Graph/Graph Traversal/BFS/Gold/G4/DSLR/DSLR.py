# https://www.acmicpc.net/problem/1956
import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().rstrip()


"""
계산기의 레지스터에 0 이상 1만 미만의 십진수를 저장할 수 있다.
명령어 DSLR은 각각 레지스터에 저장된 n을 다음과 같이 변환한다. n의 네 자릿수를 d1, d2, d3, d4라고 했을 때,
D: 2n mod 10000
S: n-1 (if n == 0: n = 9999)
L: d2d3d4d1
R: d4d1d2d3
서로 다른 두 정수 A, B에 대해 최소한의 명령으로 A를 B로 바꾸는 명령어를 출력하라.
"""
from collections import deque

def D(s):
    return s * 2 % 10000

def S(s):
    return (s - 1) % 10000

def L(s):
    return s * 10 % 10000 + s // 1000

def R(s):
    return s % 10 * 1000 + s // 10


def bfs(a, b):
    q = deque([(a, "")])
    visited = {a}
    while q:
        s, cmd = q.popleft()
        for f, c in [(D, "D"), (S, "S"), (L, "L"), (R, "R")]:
            tmp = f(s)
            if tmp not in visited:
                if tmp == b:
                    return cmd + c
                q.append((tmp, cmd + c))
                visited.add(tmp)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bfs(a, b))


"""
현 시점 골드 4. 제출 75592. 정답률 20.789 %
G4치고는 5분도 안걸리고 풀었는데, 내 코드의 풀이시간은 17초를 넘었다.
시간순 1페이지 다른 풀이들이 3초 이하인 것을 보면 원래 내 풀이 방법은 의도가 아니었나보다.
str 인덱싱을 했었는데 int와 %10000을 이용하도록 바꿨고, 실행시간이 8초로 줄었다.
베스트 풀이들을 보니 a에서 b로 가는 과정과 b에서 a로 가는 과정을 모두 기록하며 
서로 방문처리를 해줬다. 시간이 줄어들긴 하는데 그나마 직관적인 풀이는 2.5초이고 60줄은 되었다.
풀이에 투자하는 시간과 노력에 비해 결과가 극단적으로 좋아지는 편이 아니라 
코테에서 그렇게 풀 이유는 없을 듯 하다.
실제 서비스에서 필요하다면 병렬처리를 해야할 듯 하고.
"""
