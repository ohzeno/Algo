# https://www.acmicpc.net/problem/9465
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
문방구에서 스티커 2n개를 구매했다. 스티커는 2행 n열로 배치되어 있다. 스티커를 이용해 책상을 꾸미려고 한다.

구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다. 즉, 뗀 스티커의 상하좌우에 있는 스티커는 사용할 수 없게 된다.

각 스티커에 점수를 매겼다. 뗄 수 있는 스티커 점수의 최댓값을 구하는 프로그램을 작성하시오. 즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.
"""
for _ in range(int(input())):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue
    stickers[0][1] += stickers[1][0]
    stickers[1][1] += stickers[0][0]
    for i in range(2, n):
        stickers[0][i] += max(stickers[1][i-1], stickers[1][i-2])
        stickers[1][i] += max(stickers[0][i-1], stickers[0][i-2])
    print(max(stickers[0][-1], stickers[1][-1]))


"""
현 시점 실버 1. 제출 67570. 정답률 46.734 %
최근에 코테에서 자주 봤던 주변 찢어지는 스티커 문제.
이전에도 dp로 풀었었고, 어려웠던 것으로 기억한다. 
여기선 그나마 2줄 제한이고 원형도 아니라서 쉬운 편이었다.
"""