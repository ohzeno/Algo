# https://www.acmicpc.net/problem/11663
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
datas = list(map(int, input().split()))
datas.sort()  # 정렬해줘야 이분탐색 가능.
leng = len(datas)
for _ in range(m):
    st, ed = map(int, input().split())
    left, right = 0, 0
    ll, rr = 0, leng - 1
    while ll <= rr:  # 왼쪽 한계 찾기
        mid = (ll + rr) // 2
        if st <= datas[mid]:  # st보다 크거나 같으면 왼쪽으로.
            # 만약 이렇게 하고 빠져나왔으면 rr을 바꾸기 전에 ll = rr이었다는 뜻.
            # 그러니 바뀌지 않은 ll이 한계선.
            rr = mid - 1
        else:  # st보다 작으면 오른쪽으로.
            ll = mid + 1
    left = ll
    ll, rr = 0, leng - 1
    while ll <= rr:  # 오른쪽 한계 찾기.
        mid = (ll + rr) // 2
        if datas[mid] <= ed:  # ed보다 작거나 같으면 오른쪽으로.
            # 만약 이렇게 하고 빠져나왔으면 ll을 바꾸기 전에 ll = rr이었다는 뜻.
            # 그러니 바뀌지 않은 rr이 한계선.
            ll = mid + 1
        else:  # ed보다 크면 왼쪽으로.
            rr = mid - 1
    right = rr
    print(right - left + 1)



"""
현 시점 실버3. 제출 1763 정답률 35.655 %
처음엔 한 번의 이분탐색으로 left, right를 찾자고 생각했는데, 
범위가 두 곳이라 조건을 생각하기 힘들었다.
그냥 두 번의 이분탐색으로 각각의 한계를 찾았다.
"""