# https://www.acmicpc.net/problem/1976
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n_city = int(input())
n_travel = int(input())

p = [i for i in range(n_city + 1)]
def find_set(x):
    fn = x
    while p[x] != x:
        x = p[x]
    p[fn] = x  # 최초 원소 부모 갱신. 경로단축. 이거 안하면 시간초과.
    return x

def union(x, y):
    if x == y:
        return
    nx = find_set(x)
    ny = find_set(y)
    p[max(nx, ny)] = min(nx, ny)

for i in range(1, n_city + 1):
    datas = list(map(int, input().split()))
    for j in range(n_city):
        if datas[j]:
            union(i, j+1)
travels = list(map(int, input().split()))
st = find_set(travels[0])  # 여행 시작위치 부모
for travel in travels:
    if find_set(travel) != st:  # 여행 경로 중 시작도시와 이어지지 않은 곳이 있으면
        print("NO")
        break
else:  # break 없었으면 전부 이어져있음.
    print("YES")

