# https://www.acmicpc.net/problem/1929
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
m이상 n이하 소수 모두 출력.
"""

m, n = map(int, input().split())
for i in range(m, n + 1):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):  # 제곱근 이후는 대칭.
        if i % j == 0:
            break
    else:
        print(i)


"""
현 시점 실버3. 제출 229325, 정답률 26.621%
오랜만에 보는 소수 찾기. 제곱근까지 확인하면 된다는 사실을 잊고 있었다.
이걸 왜 외워야 하나 싶긴 한데...
"""