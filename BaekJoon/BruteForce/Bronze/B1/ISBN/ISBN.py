# https://www.acmicpc.net/problem/14626
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
"""

s = input()
weights = [1, 3] * 7
star_idx = 0
acc = 0
l_s = len(s)
for i, c in enumerate(s):
    if c == '*':
        star_idx = i
    else:
        weight = weights[i] if i != l_s - 1 else 1
        acc += int(c) * weight
for x in range(10):
    total = acc + x * weights[star_idx]
    if total % 10 == 0:
        print(x)
        break

"""
현 시점 Bronze I. 제출 8748. 정답률 37.584 %

신장결석 쇄석 후 정상이 아닌 상태로 풀었다. 
star_scaler = 1
acc = 0
scalers = [1, 3]
cur_scale_idx = 0
이렇게 두고 acc+m%10에 
다시 star_scaler * x를 더해서 나눠보는 식으로 풀었는데

가중치 배열을 두고 그냥 처음부터 브루트포스로 
acc + star_scaler * x + m % 10 = 0을 만족하는 x를 찾는 게 더 간단하다.

아파서 집중 못하는 상태라 그런지 오랜만이라 그런지 무뎌진듯.
"""
