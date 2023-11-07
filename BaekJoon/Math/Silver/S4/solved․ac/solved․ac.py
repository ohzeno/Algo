# https://www.acmicpc.net/problem/18110
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다.
의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균으로 결정한다.
절사평균이란 극단적인 값들이 평균을 왜곡하는 것을 막기 위해 가장 큰 값들과 가장 작은 값들을 제외하고 평균을 내는 것을 말한다. 30% 절사평균의 경우 위에서 15%, 아래에서 15%를 각각 제외하고 평균을 계산한다. 따라서 20명이 투표했다면, 가장 높은 난이도에 투표한 3명과 가장 낮은 난이도에 투표한 3명의 투표는 평균 계산에 반영하지 않는다는 것이다.

제외되는 사람의 수는 위, 아래에서 각각 반올림한다. 25명이 투표한 경우 위, 아래에서 각각 3.75명을 제외해야 하는데, 이 경우 반올림해 4명씩을 제외한다.

마지막으로, 계산된 평균도 정수로 반올림된다. 절사평균이 16.7이었다면 최종 난이도는 17이 된다.

사용자들이 어떤 문제에 제출한 난이도 의견 목록이 주어질 때, solved.ac가 결정한 문제의 난이도를 계산하는 프로그램을 작성하시오.
"""
def round(num):
    if num % 1 >= 0.5:
        return int(num) + 1
    return int(num)

diffis = [int(input()) for _ in range(int(input()))]
len_d = len(diffis)
if not len_d:
    print(0)
    exit()
diffis.sort()
bound = round(len_d * 0.15)
lb, rb = bound, len_d - bound
sums = sum(diffis[lb:rb])
print(round(sums / (len_d - 2 * bound)))


"""
현 시점 실버 4. 제출 18843. 정답률 25.951 %
백준 2클래스의 금 휘장이 사라졌길래 다시 보니 새로운 문제가 추가되어 있었다.
실버 4면서 내장 round를 쓰면 틀리는 귀찮은 문제.
"""