# https://www.acmicpc.net/problem/30804
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
N개의 정수로 이루어진 수열이 주어진다.
앞뒤로 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기려 한다.
그렇게 만들 수 있는, 과일을 두 종료 이하로 사용한 탕후루 중
과일 개수가 가장 많은 탕후루의 과일 개수를 출력하라.
"""

n = int(input())
fruits = list(map(int, input().split()))
max_fruits = 0
ll, rr = 0, 0
fruit_ridx = {}
while rr < n:
    if len(fruit_ridx) <= 2:
        fruit_ridx[fruits[rr]] = rr
        rr += 1
    if len(fruit_ridx) > 2:
        min_idx = min(fruit_ridx.values())
        ll = min_idx + 1
        del fruit_ridx[fruits[min_idx]]  # 가장 왼쪽 과일 삭제
    max_fruits = max(max_fruits, rr - ll)  # rr은 이미 다음 위치이므로 -1을 하지 않음.
print(max_fruits)


"""
현 시점 실버 2. 제출 3554. 정답률 35.048 %
엄청나게 졸린 상태로 풀어서 그런지 어려웠다.
정답률 보면 어려운거 맞을지도...
브루트포스 태그가 있길래 브루트포스로 투포인터를 돌렸다가 시간초과.
다른 방식의 브루트포스인 듯 하다.
"""