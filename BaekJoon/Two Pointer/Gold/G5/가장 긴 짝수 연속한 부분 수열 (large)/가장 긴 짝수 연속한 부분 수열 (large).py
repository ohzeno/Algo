# https://www.acmicpc.net/problem/22862
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
길이 n인 수열 s. 1 이상 정수로 이루어짐.
원하는 위치에 있는 수를 골라 최대 k번 삭제 가능.
삭제 후 수열에서 짝수로 이루어진 최장 연속 부분 수열의 길이를 구하기
"""

n, k = map(int, input().split())
datas = list(map(int, input().split()))
ll, rr = 0, 0
max_l, deleted = 0, 0
while rr < n:  # rr이 범위 벗어나면 종료
    if not datas[rr] % 2:  # 짝수면 우포인터 이동
        rr += 1
    else:  # 홀수면
        if deleted < k:  # k번 안채웠으면 삭제, 우포인터 이동
            deleted += 1
            rr += 1
        else:  # k번 채웠으면
            # 좌 포인터가 우 포인터보다 작은 동안 홀수 나올 때까지 이동
            while ll < rr and not datas[ll] % 2:
                ll += 1
            ll += 1  # 홀수 도달하면 좌 포인터 이동으로 제외.
            deleted -= 1  # 삭제카운트 갱신
    # 기존 최대 길이, 현재 최대 길이 중 큰 값으로 갱신
    # rr은 아직 검사 안했으므로(rr은 이동 후 다음 순회에서 검사함)
    # (rr - 1) - (ll - 1) = rr - ll이고
    # 삭제된 원소 제거 위해 - deleted
    max_l = max(max_l, rr - ll - deleted)
print(max_l)  # 최대 길이 출력

"""
현 시점 골드5. 제출 1550 정답률 40.763 %
투 포인터에 약한 것 같아서 투 포인터 문제를 푸는 중이다.
이번에도 역시 포인터 이동 후 검사 전에 길이를 체크한다. 굉장히 어색하다.
"""