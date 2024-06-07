# https://www.acmicpc.net/problem/2473
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
산성 용액은 1~10^9, 알칼리성 용액은 -10^9~-1
용액 n개. 3 <= n <= 5,000
서로 다른 세 용액을 혼합하여 0에 가장 가까운 값을 만들고
해당 세 용액을 오름차순으로 출력하라.
케이스가 여럿이면 아무거나 출력해도 됨.
특성값 중복 없음.
"""

def search():
    min_sum = 3 * 10**9 + 1
    min_trip = (0, 0, 0)
    for i in range(n - 2):
        ll, rr = i + 1, n - 1
        while ll < rr and min_sum:
            cur_sum = liqs[i] + liqs[ll] + liqs[rr]
            if abs(cur_sum) < min_sum:
                min_sum = abs(cur_sum)
                min_trip = (liqs[i], liqs[ll], liqs[rr])
            if cur_sum < 0:
                ll += 1
            else:  # 0과 같으면 어차피 while조건 안맞아서 깨지니 따로 처리x
                rr -= 1
    return min_trip


n = int(input())
liqs = sorted(map(int, input().split()))
if liqs[0] > 0:
    print(*liqs[:3])
elif liqs[-1] < 0:
    print(*liqs[-3:])
else:
    print(*search())


"""
현 시점 골드 3. 제출 33324. 정답률 26.897 %
두 용액 문제에서 세 용액으로 확장한 문제.
어떻게 해야할 지 고민했는데 그냥 for문으로 하나 정하고 투포인터 돌렸더니 해결됐다...
첫 제출 두번에서 틀려서 뭐가 잘못된건가 했는데 그냥 * 하나 빼먹었었다.
"""