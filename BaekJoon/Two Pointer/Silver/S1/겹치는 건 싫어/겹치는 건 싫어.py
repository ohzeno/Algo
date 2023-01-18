# https://www.acmicpc.net/problem/20922
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
datas = list(map(int, input().split()))
ll, rr = 0, 0
count = [0] * 10_0001
max_l = 1  # k는 1 이상이므로 1부터 시작.
while rr < n:  # rr이 리스트 벗어나면 종료.
    # rr으로 0부터 체크하므로 rr에 해당하는 수만 체크하면 됨.
    if count[datas[rr]] < k:  # k 이하인 수열이므로, 더하기 전에 k 미만이어야 함.
        count[datas[rr]] += 1  # rr 위치 수 카운트 증가
        rr += 1  # 오른쪽 포인터 확장
    else:  # rr 위치 수 카운트가 이미 k라면 왼쪽 포인터 이동해서 범위 줄여준다.
        count[datas[ll]] -= 1  # ll 위치 수 카운트 감소
        ll += 1
    # 각 포인터 이동 후(rr - ll + 1)에는 체크 아직 안했으니 길이는 rr - ll이다.
    # 기존 최장 길이와 비교해서 갱신.
    max_l = max(max_l, rr - ll)
print(max_l)

"""
실버1. 풀이 당시 제출 4646, 정답율 34.367 %.
투포인터인데 ll을 이동시키는 기준을 생각해내는데 좀 걸렸다.
처음엔 포인터 범위의 count에 max사용하는 방법부터 생각났다.
투포인터 문제에 약한 듯.
포인터 이동 후 체크 전에 길이를 갱신하게 되어 특이한 진행이 되었다.
"""