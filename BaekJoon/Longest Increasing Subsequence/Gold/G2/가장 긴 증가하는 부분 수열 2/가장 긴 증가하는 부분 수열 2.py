# https://www.acmicpc.net/problem/12015
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
가장 긴 증가하는 부분 수열은 10 20 30 50 이고, 길이는 4이다.
"""
from bisect import bisect_left as bl, bisect_right as br
n = int(input())
datas = list(map(int, input().split()))
lis = [datas.pop(0)]
leng = 1
for data in datas:
    if lis[-1] < data:   # lis의 마지막 값보다 크면 lis에 추가
        lis.append(data)
        leng += 1
    else:  # lis의 마지막 값보다 작거나 같으면 이분탐색으로 업데이트
        # ll, rr = 0, leng - 1
        # while ll <= rr:
        #     mid = (ll + rr) // 2
        #     if lis[mid] < data:  # data보다 작으면 오른쪽 탐색.
        #         """
        #         여기서 탈출하면 ll=rr에서 나온 mid에 1을 더한 것이니 rr의 오른쪽이다.
        #         이전에 mid가 data보다 크거나 같아서 mid - 1이 rr이 됐을것.
        #         그러니 rr + 1는 이전의 mid가 된다.
        #         즉, lis[ll]이 data보다 크거나 같은 값이다.
        #         작은값 ~ 큰값에서 작은값 + 1 자리를 찾는 것이기에 ll이 정답.
        #         """
        #         ll = mid + 1
        #     else:  # data보다 크거나 같으면 왼쪽 탐색
        #         """
        #         여기서 탈출하면 ll=rr에서 나온 mid에 1을 빼서 rr이 mid보다 작아진 것이다.
        #         ll은 mid. 즉 lis[ll]은 data보다 크거나 같은 값이다.
        #         ll - 1은 이전에 data보다 작아서 제외되었을 것이기에 ll이 정답.
        #         """
        #         rr = mid - 1
        ll = bl(lis, data)  # 왼쪽부터 최초로 data보다 크거나 같은 idx.
        lis[ll] = min(lis[ll], data)  # 더 작은 값으로 업데이트. 수열이 겹친다.
print(leng)

"""
현 시점 골드2. 제출 37029, 정답률 41.419%
가장 긴 증가하는 부분 수열 1과 비교해서 n과 Ai의 상한이 높아졌다.
그래서 1처럼 2중 for문 dp로 풀면 시간초과가 발생할 것이다.
한참 고민했는데 lis 알고리즘이 따로 있었다. 배워서 풀었다.
lis 배열에는 여러 매물대가 겹쳐 존재하는 것 같은 느낌이다.
1 3 5
2 3 4
1 2
이런 경우 배열에 1 2 4가 저장된다. 왼쪽은 겹쳐서 존재하지만 어쨋든 리스트의 길이는 lis로 유지된다.

이분탐색을 쓸 때마다 느끼는 거지만 
while 조건, if 조건, while 빠져나온 후 ll, mid, rr 중 어느 값을 사용할 것인지 등
케이스가 너무 많다. 하나하나 논리적으로 체크하려면 시간이 너무 오래 걸린다.

bisect_left, bisect_right를 좀 익혀서 사용해야 할 듯 하다.
"""
