# https://www.acmicpc.net/problem/2805
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def solution(datas, minimal):  # 이분탐색 안쓰면 시간초과.
    hh = max(datas) - 1
    lh = 1
    while lh <= hh:
        mid = (hh + lh) // 2
        acc = 0
        for i in range(n):
            if datas[i] > mid:
                acc += datas[i] - mid
                if acc >= minimal:  # 시간초과때문에 넣음. 이상이면 더 볼 필요 없음.
                    break
        if acc < minimal:
            hh = mid - 1
        elif acc >= minimal:
            lh = mid + 1
    return hh
"""
일반적 이분탐색에선 mid가 일치하면 답이지만 이 문제는 acc가 minimal 이상인 경우 중 최대 높이를 골라야 한다.
acc가 minimal 초과한 경우 lh를 올리는데, lh가 올라가서 hh를 넘었다면 이전 mid는 hh와 같을것이다.
하지만 acc < minimal이라 hh를 줄인 후 lh가 hh를 넘었다면 mid에서는 acc가 minimal보다 작다는 것. 
하지만 이분탐색은 끝났으니 hh로 내려가면 minimal 이상이 될 것이기에 hh를 리턴.
(acc는 잘려나간 나무 길이라서 절단높이가 낮아질수록 커진다.)
"""

n, m = map(int, input().split())
heights = list(map(int, input().split()))
print(solution(heights, m))
