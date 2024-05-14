# https://www.acmicpc.net/problem/1644
import sys
# sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()
"""
자연수가 주어지면, 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하시오.
1 <= N <= 4,000,000
"""
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i**2, n+1, i):
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]

n = int(input())
primes = sieve_of_eratosthenes(n)
ll, rr, sums, cnt = 0, 0, 0, 0
while rr <= len(primes):
    """
    rr이 이미 len(primes)이더라도 마지막 원소가 n과 일치할 수 있으므로
    sums >= n이면 ll을 한 번 더 증가시켜야 한다. 
    while종료조건에 =를 넣은 이유.
    """
    if sums >= n:  # sums와 일치하더라도 다른 경우 체크해야 해서 ll증가.
        sums -= primes[ll]
        ll += 1
    else:
        if rr < len(primes):
            sums += primes[rr]
        rr += 1
    if sums == n:  # 첫 sums는 0이라 포인터 옮긴 후 체크해도 됨.
        cnt += 1
print(cnt)


"""
현 시점 골드 3. 제출 47513. 정답률 	41.207 %
일단 에라토스테네스의 체로 소수를 구하고
투 포인터로 연속된 소수의 합을 구하면 된다.
투포인터 부분이 좀 까다로웠다.
"""