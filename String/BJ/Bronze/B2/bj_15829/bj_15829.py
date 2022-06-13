# https://www.acmicpc.net/problem/15829
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

l = int(input())
data = input()
sum_l = 0
for i in range(l):
    dat = data[i]
    sum_l += (ord(dat) - ord('a') + 1) * 31 ** i  # 각 알파벳 a_i * r^i
print(sum_l % 1234567891)  # mod M
