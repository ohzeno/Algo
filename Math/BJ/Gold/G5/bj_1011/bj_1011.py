# https://www.acmicpc.net/problem/1011
import sys
sys.stdin = open("input.txt")

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    c = b - a
    """
    규칙을 찾아보면 c가 an~d, bn~e에 속하면 각 res가 답이된다.
    res를 1씩 증가시키면서 구간을 찾아나가면 된다. j는 두 구간마다 1 증가
    d, e는 각 an, bn에 j를 더하면 된다.
    an d    res j    
    1  1    1   0
    bn e
    2  2    2    
    -------------
    3  4    3   1
    5  6    4
    -------------
    7  9    5   2
    10 12   6
    -------------
    13 16   7   3
    17 20   8
    -------------
    21 25   9   4
    26 30   10 
    -----------------
    31 36   11  5
    37 42   12
    """
    an = 1
    j = 0
    res = 1
    bn = an + j + 1
    while True:
        d = an + j
        e = bn + j
        if an <= c <= d:
            print(res)
            break
        elif bn <= c <= e:
            print(res + 1)
            break
        an = e + 1
        j += 1
        res += 2
        bn = an + j + 1

