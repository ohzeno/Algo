# https://www.acmicpc.net/problem/20040
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
점의 개수 n과 m번째 차례까지의 게임 진행 상황이 주어지면
사이클이 완성된다면 몇번째 차례에서 완성됐는지,
아니라면 0을 출력한다.
홀수번과 짝수번 차례는 다른 플레이어다.
매 차례에 플레이어는 이어진 적 없는 두 점을 잇는다.
"""
def find_p(x):
    if p[x] != x:
        p[x] = find_p(p[x])
    return p[x]

def union(x, y):
    nx, ny = find_p(x), find_p(y)
    if nx != ny:
        p[max(nx, ny)] = min(nx, ny)

n, m = map(int, input().split())
p = [i for i in range(n)]
for i in range(1, m+1):
    a, b = map(int, input().split())
    if find_p(a) == find_p(b):
        print(i)
        break
    union(a, b)
else:
    print(0)



"""
현 시점 골드 4. 제출 17264. 정답률 50.381 %
초보적인 union-find 문제.
"""