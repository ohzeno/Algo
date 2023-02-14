# https://www.acmicpc.net/problem/3079
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

"""
인원 M명, 입국심사대 N개. 입국심사대마다 심사시간이 다르다.
k번 심사대 한 명 심사시간 Tk
모든 사람이 심사를 받는데 걸리는 최소 시간?
1 <= n <= 10만, 1 <= m <= 10억, 1 <= t <= 10억
"""

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]
ll, rr = 0, max(times) * m  # 가장 시간이 긴 심사대에 모든 인원을 배치하면 최대가 된다.
while ll <= rr:
    mid = (ll + rr) // 2
    possible = 0
    # mid가 최대 시간이므로, mid // time는
    # mid를 넘지 않는 선에서 최대 몇 명이 들어갈 수 있는가이다.
    # mid동안 모든 테이블에서 심사가 병행 진행되므로
    # 이렇게 더해주면 mid동안 처리할 수 있는 최대 인원이 나온다.
    for time in times:
        possible += mid // time
    if possible >= m:  # 최대 인원이 실제 인원 이상이면 가능하다는 뜻. 줄여본다.
        # 이렇게 빠져나가면 mid까지는 가능했고 mid == ll이었다는 결론.
        rr = mid - 1
    else:  # 불가능해서 늘렸는데 while을 벗어나면 정답이 없다는 뜻이다. 여기서 빠져나갈 일은 없음.
        ll = mid + 1
print(ll)


"""
처음엔 for문 풀이를 만들고, 시간초과 발생.
이분탐색으로 수정 후 제출. 틀림.

조건을 검토해도 이상해서 정답 풀이들을 검색해서 넣어봤다.
3개월 전 정답풀이를 포함해 10개의 정답풀이를 넣어봤으나 모두 '틀렸습니다'가 나왔다.
채점에 오류가 있나 싶었지만 2일 전에도 파이썬으로 통과한 사람이 있었고
데이터 갱신이 있었나 했지만 가장 최근 재채점에서 '틀렸습니다'는 하나도 없었다.

뭔가의 오류가 아닌가 싶다. 다른 사람들도 계속 틀려서 질문까지 올라왔다.
-------
채점 오류가 맞았다. 하루 지나고 재채점 되어 통과됐다.
"""