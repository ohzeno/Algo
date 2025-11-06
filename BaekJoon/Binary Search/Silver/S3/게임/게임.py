# https://www.acmicpc.net/problem/1072
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
"""

x, y = map(int, input().split())
# z = int(y/x * 100)
z = int(100 * y / x)
ll, rr = 0, int(1e9)
changed = -1
while ll <= rr:
    mid = (ll + rr) // 2
    # new_z = int((y+mid)/(x+mid) * 100)
    new_z = int(100 * (y+mid) / (x+mid))
    if new_z > z:
        changed = mid
        rr = mid - 1
    else:
        ll = mid + 1
print(changed)



"""
현 시점 Silver III. 제출 58439. 정답률 25.220 %
나누고 100 곱하면 부동소수점 오차때문에 틀린다.
"""
