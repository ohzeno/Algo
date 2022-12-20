# https://www.acmicpc.net/problem/2744
import sys
sys.stdin = open('input.txt')
def input():
    return sys.stdin.readline().rstrip()

# 1. lamda식 사용.
data = input()
# data = list(map(lambda x: x.upper() if x.islower() else x.lower(), data))

# 2. swapcase 사용
print(data.swapcase())