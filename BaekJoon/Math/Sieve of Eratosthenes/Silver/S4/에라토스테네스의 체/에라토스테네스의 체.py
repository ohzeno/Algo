# https://www.acmicpc.net/problem/2960
import sys


# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()


"""
에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.
이 알고리즘은 다음과 같다(아니다. 원본 알고리즘은 P를 지우지 않는다.)
    1. 2부터 N까지 모든 정수를 적는다.
    2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
    3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
    4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.
"""

def solution(n, k):
    primes = [1] * (n + 1)
    cnt = 0
    for i in range(2, n + 1):
        if not primes[i]:
            continue
        for j in range(i, n + 1, i):
            if not primes[j]:
                continue
            primes[j] = 0
            cnt += 1
            if cnt == k:
                return j

n, k = map(int, input().split())
print(solution(n, k))

"""
현 시점 실버 4. 제출 27958. 정답률 57.428 %
에라토스테네스의 체 변형.
에라토스테네스 알고리즘 정석 만들어보려고 찾은 연습문제인데,
원본 알고리즘 설명이라면서 원본이 아닌 설명을 해서 좀 당황했다.

원본은 지워지지 않은 소수 본인의 제곱부터 지워나가는데
여기선 소수 본인도 지운다.
원본은 i를 n의 제곱근까지만 체크하면 소수만 남길 수 있다.
여기서는 소수 본인도 지워야하고, 
k번째 지우는 수가 제곱근 위의 소수일 수 있어서 n까지 체크해야한다.
"""
