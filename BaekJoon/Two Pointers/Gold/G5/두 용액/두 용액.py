# https://www.acmicpc.net/problem/2470
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
n은 2~10만
각 용액의 특성값은 -10억~10억. 각 값은 모두 다르다.
특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 오름차순으로 출력.
케이스가 둘 이상일 경우 아무거나 하나 출력.
"""
n = int(input())
datas = sorted(list(map(int, input().split())))  # 정렬해야 투포인터 가능
ll, rr = 0, n - 1  # 양 끝에서 시작
min_dif = float('inf')
ans = []
while ll < rr:
    dif = datas[ll] + datas[rr]
    if abs(dif) < min_dif:  # 최소값 갱신
        min_dif = abs(dif)
        ans = [datas[ll], datas[rr]]
    if dif < 0:  # 음수면 왼쪽 포인터를 오른쪽으로(마이너스값 작게)
        ll += 1
    else:  # 양수면 오른쪽 포인터를 왼쪽으로(플러스값 작게)
        rr -= 1
print(*ans)

"""
현 시점 골드5. 제출 38224, 정답률 30.284 %
투 포인터 문제다. 좌우 포인터 이동 조건을 생각해내지 못해서 다른 풀이들을 참고했다.
포인터 이동 조건이 말이 안되는 것 같아서 위쪽을 다시 보니 리스트를 정렬해뒀다.
그렇게 되면 좌우 끝에서 시작하면 투포인터로 합이 0에 가까운 값을 찾을 수 있다.
전처리가 필요하다는 생각은 안해봤었다. 참고할만한 부분.
"""