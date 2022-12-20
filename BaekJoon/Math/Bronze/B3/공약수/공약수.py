# https://www.acmicpc.net/problem/5618
import sys
from collections import deque

sys.stdin = open('input.txt')


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
data = deque(map(int, input().split()))
min_data = min(data)  # 둘/셋의 공약수가 존재한다면 가장 작은 수의 약수에 최대공약수가 포함될 것이다.
div_list = deque()
for i in range(2, min_data//2 + 1):  # 1은 어차피 공약수니 필요없음.
    # 약수는 어차피 절반까지만 체크하면 된다. 그 이상은 자기 자신 제외하면 약수가 될 수 없음.
    if min_data % i == 0:  # 약수라면 약수목록에 추가
        div_list.append(i)
div_list.append(min_data)  # for문 돌려서 최대공약수인지 체크하면 시간초과.
# 어차피 아래쪽에서 약수인지 체크할테니 그냥 넣음.
# 오름차순으로 출력되어야 하니 위쪽 for문 다음에 추가한 것.
print(1)  # 1은 무조건 약수.
for div_num in div_list:  # 약수 목록만 체크하면 됨.
    for dat in data:  # 각 약수가 리스트의 모든 수의 약수인가.
        if dat % div_num:  # 나머지가 있다 = 약수가 아니다. 그럼 다음 약수로
            break
    else:  # 모든 수 돌면서 브레이크 안됨 = 모든 수의 약수임. 출력.
        print(div_num)
