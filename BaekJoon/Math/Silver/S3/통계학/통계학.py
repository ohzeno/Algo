# https://www.acmicpc.net/problem/2108
from collections import Counter
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
1. 산술평균: n개의 수들의 합을 n으로 나눈 값
2. 중앙값: n개의 수들을 증가하는 순서로 나열했을 때, 중앙에 위치하는 값
3. 최빈값: n개의 수들 중 가장 많이 나타나는 값
4. 범위: n개의 수들 중 최댓값과 최솟값의 차이
n개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하라.
"""

datas = [int(input()) for _ in range(int(input()))]
leng = len(datas)
print(round(sum(datas) / leng))  # 산술평균 첫 자리에서 반올림.
datas.sort()
print(datas[leng // 2])  # 중앙값
cnt = Counter(datas).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    """
    len이 1보다 커야 최빈값이 2개 이상일 가능성이 있다.
    sort 후에 Count와 most_common()을 사용했기에 (값, 빈도)에서 값이 작은 순으로 들어있다.
    따라서 첫 원소와 두번째 원소의 빈도가 같다면 최빈값이 2개 이상인 것이고
    두번째 원소가 두번째로 작은 값이다.
    """
    print(cnt[1][0])
else:  # 최빈값이 1개인 경우
    print(cnt[0][0])
print(datas[-1] - datas[0])  # 정렬했었기에 -1에는 최댓값, 0에는 최솟값이 있다.

"""
현 시점 실버3. 제출 133521, 정답률 25.526%
Counter를 처음 써봤다. 
Counter는 리스트의 각 원소를 순서대로 key로 사용하고 빈도를 value로 딕셔너리 형태의 Counter를 만들어 반환한다.
Counter.most_common()은 빈도가 높은 순서대로 (key, value)를 원소로 넣은 리스트를 반환한다.
이름과 달리 최빈값만 반환하지는 않는다.
빈도가 같은 경우 key값은 리스트의 순서를 따른다.
"""