# https://www.acmicpc.net/problem/2467
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
용액 특성: -10^9 ~ 10^9
양수면 산성, 음수면 알칼리성
같은 양의 두 용액을 혼합한 용액의 특성은 숫자 합.
0에 가까운 용액을 만들고 싶다.
용액들이 주어지면(오름차순으로 들어온다) 
서로 다른 두 용액을 혼합하여 0에 가장 가까운 값을 만들고
해당 두 용액을 오름차순으로 출력하라.
케이스가 여럿이면 아무거나 출력해도 됨.
용액 n개. 2 <= n <= 100,000
"""
def search():
    ll, rr = 0, n - 1
    min_sum = 2 * 10**9 + 1
    min_pair = (0, 0)
    while ll < rr and min_sum:
        cur_sum = liqs[ll] + liqs[rr]
        if abs(cur_sum) < min_sum:
            min_sum = abs(cur_sum)
            min_pair = (liqs[ll], liqs[rr])
        if cur_sum < 0:
            ll += 1
        else:  # 0과 같으면 어차피 while조건 안맞아서 깨지니 따로 처리x
            rr -= 1
    return min_pair


n = int(input())
liqs = list(map(int, input().split()))
if liqs[0] > 0:
    print(liqs[0], liqs[1])
elif liqs[-1] < 0:
    print(liqs[-2], liqs[-1])
else:
    print(*search())

"""
현 시점 골드 5. 제출 10928. 정답률 36.565 %
몇 번 비슷한 문제 풀어봤던 것 같은데도 
보자마자 생각난건 완전 탐색과
각 원소에 대한 이분탐색이었다.
하지만 리스트가 이미 정렬되어 있어서 투포인터로 O(n)으로 풀 수 있다.
지금 보니 두 용액 문제에서 정렬만 되어있는 문제다.
"""