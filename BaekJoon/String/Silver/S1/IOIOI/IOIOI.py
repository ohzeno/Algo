# https://www.acmicpc.net/problem/5525
import sys
sys.stdin = open("input.txt")
def input():
    return sys.stdin.readline().rstrip()
"""
n+1개의 I와 n개의 O로 이루어져 있음.
I로 시작해서 O와 번갈아가며 I로 끝나는 문자열을 Pn이라고 함.
P1 = IOI
P2 = IOIOI
I와 O m개로 이루어진 문자열 s와 정수 n이 주어졌을 때, 
S안에 Pn이 몇 군데 포함되어 있는지 구하라.
1 <= n <= 100_0000
2n + 1 <= m <= 100_0000
서브태스크 조건
n <= 100, m <= 1_0000
"""

n = int(input())
m = int(input())
s = input()
pattern_cnt = 0
pos = 0
while pos < m - 2:
    if s[pos] == "I":
        ioi_cnt = 0
        while pos+2 < m and s[pos + 1] == 'O' and s[pos + 2] == 'I':
            ioi_cnt += 1
            if ioi_cnt == n:
                pattern_cnt += 1
                ioi_cnt -= 1
            pos += 2
    pos += 1
print(pattern_cnt)


"""
현 시점 실버 1. 제출 36455. 정답률 29.957 %
슬라이싱으로 순회했다가 50점. 일부 케이스에서 시간초과 발생했을 것.
이후 패턴체크. 100점이나 베스트 풀이들이 100ms 근처임에 비해 내 풀이는 588ms.
베스트 풀이들이 어떻게 풀었나 살펴봄. find를 사용해서 패턴 시작 부분을 찾음.
이후 패턴이 존재하면 내 로직과 비슷하게 패턴을 찾고, 찾은 패턴을 슬라이싱으로 제거하고 다시 탐색.
찾는 과정과 세는 과정이 따로 있어 중복순회고, 슬라이싱을 통해 문자열을 잘라내는 과정까지 있다.
하지만 find는 c로 구현되어 있어서 더 빠르다. 
그런 풀이들은 꼼수를 이용한 풀이라 알고리즘 취지와는 맞지 않다.
"""
