# https://www.acmicpc.net/problem/1789
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

def acc_sum(target):
    acc = 1
    count = 1
    while True:
        if acc == target:
           return count
        if acc < target:
            count += 1
            acc += count
        elif acc > target:
            return count - 1

"""
서로 다른 자연수이므로 1부터 체크해보면 규칙이 보인다.
ex) 15는 12345의 합. 16은 15의 합에서 마지막 5만 6으로 바꾸면 된다.
21은 1 2 3 4 11이 아니라 123456이 더 많다. 그러니 위와같이 자연수를 순서대로 더하고 범위를 판별하면 된다. 
"""
n = int(input())
print(acc_sum(n))








